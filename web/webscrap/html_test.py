# coding: utf-8
from . import io
from . import html
from bs4 import BeautifulSoup
import os

def test_extract_table():
    url = 'https://ko.wikipedia.org/wiki/%EC%95%A8%EB%9F%B0_%ED%8A%9C%EB%A7%81'
    filename = io.snapshot_webpage(url, 'turing_wiki.html')
    with open(filename) as f:
        soup = BeautifulSoup(f, 'html.parser')
    # 파일 삭제
    os.unlink(filename)

    tables = soup.select('table.wikitable')

    table_frames = html.extract_tables(tables)
    assert table_frames[0].ix[0,0] == '1912년'

def test_get_soup():
    # source is url
    url = 'https://ko.wikipedia.org/wiki/%EC%95%A8%EB%9F%B0_%ED%8A%9C%EB%A7%81'
    soup = html.get_soup(url)
    assert soup.title.text == "앨런 튜링 - 위키백과, 우리 모두의 백과사전"

    # source is file
    filename = io.snapshot_webpage(url, 'turing_wiki.html')
    soup = html.get_soup(filename)
    # 파일 삭제
    os.unlink(filename)

    assert soup.title.text == "앨런 튜링 - 위키백과, 우리 모두의 백과사전"
