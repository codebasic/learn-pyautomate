# 윈도우 메모장의 UTF8은 utf-8-sig 인코딩을 사용해야 합니다.
파일 = open('튜링_utf8.txt', encoding='utf-8-sig')
내용 = 파일.read()
print(내용)
