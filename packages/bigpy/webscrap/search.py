# coding: utf-8
import webbrowser
import requests
from bs4 import BeautifulSoup


def search(keyword, engine='google', open_top_links=5):
    search_url = 'http://google.com/search?q={0}'
    try:
        res = requests.get(search_url.format(keyword))
    except requests.ConnectionError:
        print('도메인 또는 인터넷 연결을 확인')
        return

    if not res.status_code == 200:
        print('HTTP 응답 코드: {}'.format(res.status_code))

    if open_top_links is not None:
        soup = BeautifulSoup(res.text, 'lxml')
        if engine=='google':
            tags = soup.select('.r a')
        else:
            raise NotImplementedError('잘 모르는 검색엔진이네요 ;;')
        for a in tags[:open_top_links]:
            webbrowser.open('http://google.com' + a.get('href'))
