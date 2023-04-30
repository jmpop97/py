import os
from collections import defaultdict

os.system("cls")

N=5; stages=[2,1,2,6,2,4,3,3]

# N=4; stages=[4,4,4,4,4]

##############함수 로직################
'''
1.input값과 result값을 보기
-input
N   :총 스테이지 수
stages : .element 플레이어의 도전중인 스테이지

-result
실패율이 높은 스테이지 순으로 스테이지의 번호가 list값으로 나와야한다.
=>스테이지별 실패율 구하고, 역순 정렬하기


스테이지별 실패율 = 도전 중인 플레이어 수/ 도전중인 플레이어수+지나간 플레이어수
도전 중인 플레이어수+지나간 플레이어수= 총 플레이어수 - 도전 못한 플레이어수

도전 중인 플레이어 수는 dict로 구하기 → key값을 통해서 시간복잡도 낮추기 위해서이다.

각 스테이지 별 실패율을 for문과 key를 통해서 구한후
실패율(key)에 해당되는 스테이지(value)를 list값으로 저장 (이때 list는 정렬되며 저장된다.)

key값으로 역순정렬 후 그에 대한 스테이지(value)를 for문으로 순차적으로 합쳐줌으로써 결과값을 구했다.

'''


# key:머물고있는 스테이지 value:도전중인 플에이어 수 dict에 저장
# key:stage value:challenger수 dict에 저장
challenger_dic=defaultdict(int)
for player_stage in stages:
    challenger_dic[player_stage] += 1
#전체 도전자 수 구하기 
players=len(stages)

# 실패율을 저장할 dict 선언
fail_rates=defaultdict(list)

#스테이지 수만큼 for반복문 실행
for stage in range(1,N+1):
    #실패율 계산
    fail_rate=challenger_dic[stage]/players #실패율 = 특정스테이지에 있는 플레이어수/특정스테이지를 겪은 플레이어수
    players-=challenger_dic[stage] #이전 스테이지의 도전자 수만큼 줄여라 :챠밍했던 포인트

    #실패율 dict에 저장 
    fail_rates[fail_rate]+=[stage]

#실패율이 높은순으로 정렬
fail_vals=sorted(fail_rates.keys(),reverse=True) # sorted(dict,reverse=True) 의 경우 value값으로 1차 정렬, key값으로 2차 정렬
#실패율에 해당

result=[]
for fail_val in fail_vals:
    result+=fail_rates[fail_val]




# key:stage value:fail_rate
#도전중인사람/players-전스테이지까지 도전중인 사람 뺴기
                       
#while문으로 14번째걸 돌려서 players-전스테이지=0 이면 break
#그 값들을 list로 저장 내림차순으로 정렬 후 반환


