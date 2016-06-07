import re, sys
import requests
from bs4 import BeautifulSoup

def 요소추출(대상, 선택자):
    if re.match(r'(http|https)://', 대상):
        응답 = requests.get(대상)
        if 응답.status_code == 200:
            html = 응답.text
    else:
        html = open(대상)

    soup = BeautifulSoup(html, 'lxml')
    선택된요소 = soup.select(선택자)
    return 선택된요소

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)

    대상 = sys.argv[1]
    선택자 = sys.argv[2]

    선택된요소 = 요소추출(대상, 선택자)

    for 요소 in 선택된요소:
        print(요소)
