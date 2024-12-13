###################open_source_project_20211944###########

#import time

##타이머 시작점
#start = input("Enter를 누르면 타이머를 시작합니다.")
#begin = time.time()

##타이머 종료점
#stop = input("Enter를 누르면 측정을 종료합니다.")
#end = time.time()

##시간차
#result = end - begin

##여기서 round는 파이썬에서 소수점 자리수 조절에 활용됩니다.
#result = round(result,3)
#print("시작 후", result, "초의 시간이 흘렀습니다.")

###################--{https://datazzang.tistory.com/6} -- 코드 출처


import time
from datetime import datetime

# 타이머 시작
print("타이머를 시작하려면 Enter를 누르세요.")
input()  # 사용자로부터 입력 받음
start_time = time.time()
start_datetime = datetime.now()  # 시작 시각 기록
print(f"타이머가 시작되었습니다. 시작 시각: {start_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

# 타이머 종료
print("타이머를 종료하려면 Enter를 누르세요.")
input()  # 종료 입력 받음
end_time = time.time()
end_datetime = datetime.now()  # 종료 시각 기록

# 경과 시간 계산
elapsed_time = round(end_time - start_time, 3)

# 결과 출력
print(f"타이머 종료! 종료 시각: {end_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"총 경과 시간: {elapsed_time}초")
