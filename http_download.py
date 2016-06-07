import sys, os
import requests

def 웹페이지_다운로드(url, 파일경로):
    응답 = requests.get(url)
    if os.path.exists(파일경로):
        print('같은 이름의 파일이 존재합니다. 그냥 종료합니다.')
        return
        
    웹문서파일 = open(파일경로, 'wb')
    for 조각 in 응답.iter_content(100000):
        웹문서파일.write(조각)
    웹문서파일.close()

if __name__ == '__main__':
    사용법 = """사용법:
    $ python {0} URL 파일명"""

    if len(sys.argv) < 2:
        sys.exit(사용법.format(sys.argv[0]))

    url = sys.argv[1]
    파일명 = sys.argv[2]
    웹페이지_다운로드(url, 파일명)
