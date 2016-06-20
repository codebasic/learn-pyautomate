from imapclient import IMAPClient
import email
from email.header import decode_header

class EmailClient:
    def __init__(self,
        host,
        port=None,
        use_uid=True,
        ssl=False,
        stream=False,
        ssl_context=None,
        timeout=None):

        self._imapclient = IMAPClient(host, ssl=ssl)

    def oauth2_login(self, user, access_token):
        result = self._imapclient.oauth2_login(user, access_token)
        if 'Success' in result[0].decode('utf-8'):
            self.select_folder()
        return result

    def select_folder(self, folder='INBOX', readonly=True):
        return self._imapclient.select_folder(folder, readonly=readonly)

    def search(self, criteria, charset='utf-8'):
        message_ids = self._imapclient.search(criteria, charset=charset)
        return message_ids

    def get_messages(self, message_ids):
        raw_messages = self._imapclient.fetch(message_ids, ['BODY[]'])
        messages=[]
        for mid, content in raw_messages.items():
            body = email.message_from_bytes(content[b'BODY[]'])
            messages.append((mid, body))
        return messages

    def get_subjects(self, message_ids):
        messages= self.get_messages(message_ids)
        subject_list = []
        for mid, msg in messages:
            message_header = dict()
            message_header['ID'] = mid
            message_header['FROM'] = self._decode_header(msg.get('FROM'))
            message_header['Subject'] = self._decode_header(msg.get('Subject'))[0]
            subject_list.append(message_header)
        return subject_list

    def _decode_header(self, header):
        content_list = []
        for field in email.header.decode_header(header):
            #if field is None: continue
            content, encoding = field
            if isinstance(content, bytes):
                content = content.decode(encoding if encoding else 'utf-8')
            content_list.append(content)
        return content_list
