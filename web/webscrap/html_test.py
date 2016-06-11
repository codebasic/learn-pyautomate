# coding: utf-8
from . import io as webio
from . import html
from bs4 import BeautifulSoup
import os

def test_extract_table():
    url = 'https://ko.wikipedia.org/wiki/%EC%95%A8%EB%9F%B0_%ED%8A%9C%EB%A7%81'
    웹문서스냅샷파일 = webio.snapshot_webpage(url, '앨런튜링_위키.html')
    with open(웹문서스냅샷파일) as f:
        soup = BeautifulSoup(f, 'html.parser')
    # 파일 삭제
    os.unlink(웹문서스냅샷파일)

    tables = soup.select('table.wikitable')

    table_frames = html.표추출(tables)
    assert table_frames[0].ix[0,0] == '1912년'
