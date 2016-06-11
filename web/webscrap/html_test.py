# coding: utf-8
from . import io as webio
from . import html
from bs4 import BeautifulSoup

def test_extract_table():
    url = 'https://ko.wikipedia.org/wiki/%EC%95%A8%EB%9F%B0_%ED%8A%9C%EB%A7%81'
    웹문서스냅샷파일 = webio.snapshot_webpage(url, '앨런튜링_위키.html')
    f = open(웹문서스냅샷파일)
    soup = BeautifulSoup(f, 'html.parser')
    tables = soup.select('table.wikitable')

    table_frames = html.표추출(tables)
    assert table_frames[0].ix[0,0] == '1912년'
