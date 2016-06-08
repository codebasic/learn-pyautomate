import pip
import platform, sys, os,zipfile
import requests

def setup_webdriver():
    pip.main(['install', 'selenium'])


    driverfile_map = {'Windows': 'chromedriver_win32.zip',
        'Darwin': 'chromedriver_mac32.zip'}
    driverfile = driverfile_map.get(platform.system(), None)
    if driverfile is None:
        sys.exit('No chromedriver for {0}'.format(platform.system()))

    chromedriver_url = 'http://chromedriver.storage.googleapis.com/2.22/'
    chromedriver_url = chromedriver_url + driverfile

    print('Downloading chromedriver ...')
    http_download(chromedriver_url, driverfile)

    # 압축 해제
    print('Extracting downloaded driver file ...')
    if os.path.exists(driverfile):
        driverzip = zipfile.ZipFile(driverfile)
        driverzip.extractall()
        driverzip.close()

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
