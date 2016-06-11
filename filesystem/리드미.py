import os

def 리드미파일생성(경로, 부서명):
    본문 = 'NCSOFT2016\n'
    본문 += '업무자동화를 위해 생성된 파일입니다.\n'
    본문 += '{0}, {1}\n'.format('이성주', 'seongjoo@')
    본문 += '{0} 부서용'.format(부서)

    리드미파일 = open(경로, 'w', encoding='utf-8')    
    리드미파일.write(본문)
    리드미파일.close()
    

부서목록 = ['기획', '개발', '아트', '교육']
print('부서별 폴더 생성 ...')
for 부서 in 부서목록:
    if not os.path.exists(부서):
        os.makedirs(부서)

    # 현재 부서 폴더에 리드미 파일 생성
    경로 = os.path.join(부서, 'README.txt')
    # 해당 경로로 README 파일 생성
    리드미파일생성(경로, 부서)
    
    
