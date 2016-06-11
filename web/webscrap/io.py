import sys
from urllib.parse import urlparse, unquote, unquote_plus
import requests

def snapshot_webpage(url, filename=None, data=None):
    try:
        res = http_download(url, data=data)
    except requests.ConnectionError as e:
        sys.exit('HTTP이 통신에 문제가 있습니다: {0}'.format(e))
    except requests.HTTPError as e:
        sys.exit('응답 비정상: {0}'.format(e))
    except:
        raise

    # 파일명 설정
    if filename is None:
        path = urlparse(url).path
        path = unquote_url(path)
        filename = os.path.basename(path)

    # 파일로 저장
    with open(filename, 'wb') as f:
        for chunk in res.iter_content(100000):
            f.write(chunk)
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
