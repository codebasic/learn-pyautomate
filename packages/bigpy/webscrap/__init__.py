# coding: utf-8
from . import io, html

import pip
import platform, sys, os, stat, zipfile
import requests
import time

def get_browser(browser='Chrome', driverpath=None):
    driver_map = {'Chrome': 'chromedriver'}

    try:
        from selenium import webdriver
    except ImportError:
        setup_webdriver()
        try:
            from selenium import webdriver
        except:
            raise
    else:
        if driverpath is None:
            driverpath = os.path.join('.', driver_map[browser])
        driver = getattr(webdriver, browser)(driverpath)
        return driver


def setup_webdriver():
    # selenium package 설치
    pip.main(['install', 'selenium'])

    print('chromedriver 다운로드')
    downloaded_file = download_chromedriver()
    print(downloaded_file)

    # 압축 해제
    print('다운로드 받은 파일 압축 해제 ...')
    driverzip = zipfile.ZipFile(downloaded_file)
    driverzip.extractall()
    driverfile = driverzip.namelist()[0]
    driverzip.close()

    # 실행권한 설정
    st = os.stat(driverfile)
    os.chmod(driverfile, st.st_mode | stat.S_IEXEC)

    print('설정 테스트 ...', end=' ')
    test_webdriver(driverfile)
    print('완료')

def download_chromedriver():
    driverfile_map = {'Windows': 'chromedriver_win32.zip',
        'Darwin': 'chromedriver_mac32.zip'}
    download_target = driverfile_map.get(platform.system(), None)
    if download_target is None:
        sys.exit('No chromedriver for {0}'.format(platform.system()))

    chromedriver_url = 'http://chromedriver.storage.googleapis.com/2.22/'
    chromedriver_url = chromedriver_url + download_target

    driverfilepath = http_download(chromedriver_url, download_target)
    return driverfilepath

def test_webdriver(driverfile):
    from selenium import webdriver
    chrome = webdriver.Chrome(os.path.join('.',driverfile))
    chrome.get('http://www.gogle.com')
    time.sleep(5)
    search_box = chrome.find_element_by_name('q')
    search_box.send_keys('파이썬')
    time.sleep(5)
    search_box.submit()
    time.sleep(10)
    chrome.quit()

def http_download(url, 파일경로):
    응답 = requests.get(url)
    if os.path.exists(파일경로):
        print('File already exists')
        return 파일경로

    with open(파일경로, 'wb') as 파일:
        for 조각 in 응답.iter_content(100000):
            파일.write(조각)

    return 파일경로

if __name__ == '__main__':
    setup_webdriver()
