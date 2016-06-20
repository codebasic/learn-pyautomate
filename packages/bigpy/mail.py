import os
import configparser
import email
from email.header import decode_header
import subprocess

from imapclient import IMAPClient

class EmailConfig:
    def __init__(self, configpath, debug=False):
        self.configpath = configpath
        self.config = self._get_config()
        self.debug=debug

    def _get_config(self):
        config = configparser.ConfigParser()
        config.read(self.configpath)
        return config

    def get_access_token(self, section, refresh=False):
        config = self.config
        if refresh:
            return self.refresh_access_token(section)
        self.access_token = config[section]['access_token']
        return self.access_token

    def refresh_access_token(self, section):
        config = self.config
        self.user = config[section]['user']
        client_id = config[section]['client_id']
        client_secret = config[section]['client_secret']
        refresh_token = config[section]['refresh_token']
        # gmail oauth2.py is written for python 2
        ps = subprocess.run([
            os.path.join(os.path.dirname(__file__), './gmail/oauth2.py'),
            '--user={}'.format(self.user),
            '--client_id={}'.format(client_id),
            '--client_secret={}'.format(client_secret),
            '--refresh_token={}'.format(refresh_token)],
            stdout=subprocess.PIPE)
        access_token = ps.stdout.decode('utf-8').split('\n')[0].split(':')[1]
        if self.debug:
            print('접근 토큰: {}'.format(access_token))

        # update config file
        config[section]['access_token'] = access_token
        self.update_config(verbose=self.debug)

        self.access_token = access_token
        return access_token

    def update_config(self, verbose=False):
        config = self.config
        with open(self.configpath, 'w') as cf:
            config.write(cf)
        if verbose:
            print('Config file {} updated.'.format(self.configpath))


class EmailClient:
    def __init__(self,
        host,
        port=None,
        use_uid=True,
        ssl=False,
        stream=False,
        ssl_context=None,
        timeout=None,
        method=None,
        debug=False):
        self.debug = debug
        self._imapclient = IMAPClient(host, ssl=ssl)
        if method:
            if 'oauth2' in method:
                oauth2_config = method['oauth2']
                self.mailconfig = EmailConfig(oauth2_config['configfile'],
                    debug=self.debug)
                self.mailconfig.get_access_token('GMAIL', refresh=True)
                login_result = self.oauth2_login(self.mailconfig.user,
                    self.mailconfig.access_token)
                print(login_result)

    def oauth2_login(self, user, access_token):
        result = self._imapclient.oauth2_login(user, access_token)
        if 'Success' in result[0].decode('utf-8'):
            self.select_folder()
        return result

    def logout(self):
        return self._imapclient.logout()

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
