import os

# 1. 부서별 폴더 생성
부서목록 = ['기획', '개발', '아트', '교육']
for 부서 in 부서목록:
    # 부서별 폴더 생성 구문
    if not os.path.exists(부서):    
        os.makedirs(부서)

# 2. 각 부서별 폴더 경로 획득
for 부서 in 부서목록:    
    # 3. 각 부서별 경로 내 리드미 파일 생성
    경로 = os.path.join(부서, 'README.txt')
    print(경로)

    # 경로에 파일이 존재하면, 즉시 목록의 다음 항목을 진행한다.
    if os.path.exists(경로):
        continue

    # 경로에 파일이 존재하지 않는 경우에만 실행
    리드미 = open(경로, 'w')
    리드미.write('NCSOFT2016')
    리드미.write('\n')
    리드미.write('업무자동화를 위해 생성된 파일입니다.')
    리드미.write('\n')
    리드미.write('{0}, {1}'.format('이성주', 'seongjoo@codebasic'))
    리드미.write('\n')
    리드미.write('{0} 부서용'.format(부서))
    리드미.close()


