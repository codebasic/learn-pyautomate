# coding: utf-8
from urllib.parse import urlparse
import re
import pandas as pd
from bs4 import BeautifulSoup
import importlib

from . import io

def get_soup(src, encoding='utf-8'):
    # TODO: check if url or filepath
    scheme = urlparse(src).scheme
    if re.compile('(http|https)').match(scheme):
        res = io.http_download(src)
        doc = res.text
    else:
        doc = open(src, encoding='utf-8')

    parser = 'lxml' if importlib.find_loader('lxml') else 'html.parser'
    return BeautifulSoup(doc, parser)

def extract_tables(table_elements):
    table_frames = pd.read_html(str(table_elements))
    return table_frames
