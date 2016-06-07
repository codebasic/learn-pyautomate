import requests
import sys

def 웹페이지_다운로드(url, 파일명):
    응답 = requests.get(url)
    웹문서파일 = open('.'.join([파일명, 'html']), 'wb')
    for 조각 in 응답.iter_content(100000):
        웹문서파일.write(조각)
    웹문서파일.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('다운로드 받을 URL과 스냅샷 파일명을 입력해 주세요.')
        sys.exit(1)

    url = sys.argv[1]
    파일명 = sys.argv[2]
    웹페이지_다운로드(url, 파일명)
