import sys, webbrowser
import requests
from bs4 import BeautifulSoup

def 구글검색(키워드, 탭수=5):
    URL양식 = 'http://google.com/search?q={0}'
    응답 = requests.get(URL양식.format(키워드))
    if not 응답.status_code == 200:
        print('HTTP 응답 코드: {}'.format(응답.status_code))
    else:
        스프 = BeautifulSoup(응답.text, 'lxml')

    결과링크 = 스프.select('.r a')
    for 링크 in 결과링크[:탭수]:
        webbrowser.open('http://google.com' + 링크.get('href'))

if __name__ == '__main__':
    사용법 = """사용법
    $ python {0} 검색문구
    """
    if len(sys.argv) < 2:
        sys.exit(사용법.format(sys.argv[0]))

    검색문구 = sys.argv[1]
    구글검색(검색문구)
