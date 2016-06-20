# coding: utf-8
from . import io
import pytest
import requests
import os
from urllib.parse import quote_plus

def test_http_download():
    res = io.http_download('http://google.com')
    assert res.status_code == 200

    with pytest.raises(requests.ConnectionError):
        io.http_download('http://no-such-domain.com')

    with pytest.raises(requests.HTTPError):
        io.http_download('http://google.com/nosuchpath')

def test_unquote_url():
    url = 'https://ko.wikipedia.org/wiki/%EC%95%A8%EB%9F%B0_%ED%8A%9C%EB%A7%81'
    url_unquoted = io.unquote_url(url)
    basename = os.path.basename(url_unquoted)
    assert basename == '앨런_튜링'

    url_quote_plus = quote_plus(url_unquoted)
    url_unquoted = io.unquote_url(url_quote_plus)
    basename = os.path.basename(url_unquoted)
    assert basename == '앨런_튜링'

def test_snapshot_webpage():
    url = 'https://ko.wikipedia.org/wiki/%EC%95%A8%EB%9F%B0_%ED%8A%9C%EB%A7%81'
    filename = io.snapshot_webpage(url, '앨런튜링_위키.html')
    assert os.path.exists(filename)
    # cleanup
    os.unlink(filename)

    with pytest.raises(requests.ConnectionError):
        io.snapshot_webpage('http://no-such-domain.com', 'no.html')

    with pytest.raises(requests.HTTPError):
        io.http_download('http://google.com/nosuchpath')
