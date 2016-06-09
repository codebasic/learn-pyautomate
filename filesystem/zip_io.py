# coding: utf-8
import zipfile
import sys, platform, os, shutil
from bigpy.wZip import wZipFile

print('예제 파일 생성')
컴퓨터위인 = {'튜링': '앨런 튜링', '잡스': '스티브 잡스'}
파일목록 = []
for 제목, 내용 in 컴퓨터위인.items():
    파일명 = 제목 + '.txt'
    with open(파일명, 'w', encoding='utf-8') as 파일:
        파일.write(내용)
    print('파일 {} 생성'.format(파일명))
    파일목록.append(파일명)

print('압축 생성 ...', end=' ')
with wZipFile('컴퓨터 위인.zip', 'w') as wz:
    for 파일명 in 파일목록:
        wz.write(파일명)
print('완료')

print('압축 파일 내부 출력')
wz = wZipFile('컴퓨터 위인.zip')
파일목록 = wz.namelist()
for 파일명 in 파일목록:
    print(파일명)
    info = wz.getinfo(파일명)
    print('파일크기: {0}'.format(info.file_size))

print('압축 해제')
for 파일명 in 파일목록:
    shutil.move(파일명, 파일명 + '.old')
wz.extractall()
wz.close()

# print('윈도우 zip 폴더')
# with wZipFile('위인2.zip') as wz:
#     for 파일명 in wz.namelist():
#         print(파일명)
#         info = wz.getinfo(파일명)
#         print('{0}, 파일크기: {1}'.format(info.filename, info.file_size))
#
#     print('압축 해제')
#     wz.extractall()
