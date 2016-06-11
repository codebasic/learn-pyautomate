import sys
from urllib.parse import urlparse, unquote, unquote_plus
import requests

def snapshot_webpage(url, filename=None, mode='wb', data=None):
    res = http_download(url, data=data)

    # 파일명 설정
    if filename is None:
        path = urlparse(url).path
        path = unquote_url(path)
        filename = os.path.basename(path)

    # 파일로 저장
    with open(filename, mode) as f:
        if mode[-1] == 'b':
            for chunk in res.iter_content(100000):
                f.write(chunk)
        else:
            f.write(res.text)

    return filename

def http_download(url, method='get', data=None):
    if method == 'get':
        res = requests.get(url, params=data)
    res.raise_for_status()
    return res

def unquote_url(url):
    if '+' in url:
        return unquote_plus(url)
    return unquote(url)
