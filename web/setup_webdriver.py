import pip
import platform, sys, os, stat, zipfile
import requests
import time

def setup_webdriver():
    pip.main(['install', 'selenium'])


    driverfile_map = {'Windows': 'chromedriver_win32.zip',
        'Darwin': 'chromedriver_mac32.zip'}
    download_target = driverfile_map.get(platform.system(), None)
    if download_target is None:
        sys.exit('No chromedriver for {0}'.format(platform.system()))

    chromedriver_url = 'http://chromedriver.storage.googleapis.com/2.22/'
    chromedriver_url = chromedriver_url + download_target

    print('Downloading chromedriver ...')
    http_download(chromedriver_url, download_target)

    # 압축 해제
    if os.path.exists(download_target):
        print('Extracting downloaded driver file ...')
        driverzip = zipfile.ZipFile(download_target)
        driverzip.extractall()
        driverfile = driverzip.namelist()[0]
        driverzip.close()

    # 실행권한 설정
    st = os.stat(driverfile)
    os.chmod(driverfile, st.st_mode | stat.S_IEXEC)
    test_webdriver(driverfile)

def test_webdriver(driverfile):
    from selenium import webdriver
    print(driverfile)
    chrome = webdriver.Chrome(driverfile)
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
        return

    파일 = open(파일경로, 'wb')
    for 조각 in 응답.iter_content(100000):
        파일.write(조각)
    파일.close()

if __name__ == '__main__':
    setup_webdriver()
