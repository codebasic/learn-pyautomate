# coding: utf-8
from urllib.parse import urlparse
import pandas as pd
from bs4 import BeautifulSoup
from . import io

def get_soup(url):
    # TODO: check if url or filepath
    res = io.http_download(url)
    src = res.text
    return BeautifulSoup(src, 'html.parser')

def extract_tables(table_elements):
    table_frames = pd.read_html(str(table_elements))
    return table_frames
