import streamlit as st
import numpy as np

# st.image('이승학.jpg', width=300)
col1, col2 = st.columns(2)
with col1:
    st.image('이승학.jpg', width=300)

with col2:
    st.write('놓치면 후회할 인재)')
    '이름 : 이승학'
    '전화번호 : 010-8126-7843'
    'email :  ak173133@naver.com'
    '주소 : 충남 논산시 대학로 121'

st.link_button("instagram(🌏)", "https://www.instagram.com/seung.__.pago/")

'자기소개서'
'저의 성장 과정에서 성실함과 도전은 절대 빠질 수 없는 요소들입니다. 학창 시절, 저는 학업뿐만 아니라 봉사단체에 가입하여 매달 한번씩 봉사활동에 참여하고, 체력을 기르고 자기관리를 하고자 축구와 배드민턴 동아리 활동, 제 자신의 생활력을 기르고 부모님의 지원을 조금이라도 줄여보고자 아르바이트를 하는 등 다양한 역할을 동시에 수행하였습니다. 이러한 다양한 활동들을 함으로써 지금의 저의 성실함과 시간 관리하는 방법을 터득하고 향상시킬수 있게 되었습니다.'
'또한, 본드와 같은 끈끈함의 상징인 협력이 저의 장점이라고 자부할 수 있습니다. 저는 주어진 일주일이라는 짧은 기간 안에 조별 활동을 통해 전공과 관련된 논문을 작성해야하는 고난을 겪었습니다. 한 학기 동안 연구했던 내용을 시험하고 분석한 결과를 토대로 논문을 작성해야하는 임무였지만 시간이 너무 짧았기에 어려움이 있었습니다. 하지만, 저는 조원들에게 현재 논문 주제와 관련된 사고 현황과 문제에 대한 부족한 해결방안을 조사하는 역할을 부여하였고, 저는 조원들이 제시한 의견들을 모두 들어보고 조원들간의 토의를 하면서 다양한 방안을 모색해낼 수 있었고 주어진 기간안에 논문을 작성할수 있었습니다.'







# import matplotlib.pyplot as plt


# fig, ax = plt.subplots()

# x = [-10, -9, -8, -7, -6]
# x

# x = []
# 'x', x
# for iter in range(-10, 11, 5):
    # 'iter', iter
    # x.append(iter)
    # 'x', x

# st.pyplot(fig)




# n = 3
# arr = np.full((n,n), '나머지')
# arr
# for i in range(n):
    # for j in range(n):
        #  arr[i, j] = '나머지'
        # if i == j or i + j ==n-1:
            # arr[i, j] = '대'
            #  if i + j == n-1:
            # arr[i, j] = '대'


    
# n1 = np.zeros((4,5))
# n1
# for i in range(4):
    # for j in range(5):
        # n1[i, j] = 10






# list1 = [[10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10]]
# i = np.array(list1)
# i
 




#list1 = [[1, 2, 3, 4], [3, 5, 7, 9]]
#a = np.array(list1)
#a
#a.shape
#s = a.sum(axis=0)
#s
#mn = a.min(axis=1)
#mn







    


# def sta(arr):
#     # sum = 0
#     mx = -1e10
#     mn = 1e10
#     for i in arr: 
#         sum = sum + i
#         if mx < i:
#             mx = i
#         if mn > i:
#             mn = i
#     arr
#     'sum = ', sum, 'min = ', mn, 'max = ', mx

# sta([5, 13, 7, 4, 11])




# s = 0
# for i in range(1, 100+1):
    # s = s + i
# s




# list_1 = [1, 2, 7, 4, 50]
# le = len(list_1)

# for i in list_1:
    # i
    # sum = 0 # 초기값
    # sume = sum + i




# streamlit run tt.py



# 거북이 사각형
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(1)


# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)



# 거북이 사각형 4개 그리기 
# for i in range(4):
#     t.forward(100)
#     t.left(90)

# t.up()
# t.goto(-200,0)
# t.down()

# for i in range(4):
#     t.forward(100)
#     t.left(90)

# t.up()
# t.goto(-200,-200)
# t.down()

# for i in range(4):
#     t.forward(100)
#     t.left(90)

# t.up()
# t.goto(0,-200)
# t.down()   

# for i in range(4):
#     t.forward(100)
#     t.left(90)

# t.up()
# t.goto(0,0)
# t.down()



# dict = {'name':'신수인',
#         'weight':69,
#         'height':172,
#         'address':'충남 논산시 대학로 121'}

# dict

# for key in dict.keys():
#     key

# for v in dict.values():
#     v

# "============================================"
# for k, v in dict.items():
#     k
#     v

# ty = type(dict)
# ty


# 딕셔너리 생성하기
# dict_1 = {'name':'우승덕', 'birth':2000, 'addr':'KR'}
# print(dict_1)
# print(dict_1['birth'])

# # 키와 값 추가하기
# dict_1['weight'] = 66.5
# dict_1['family'] = ['아빠', '나']
# print(dict_1)

# # 여러 키와 값을 동시에 추가하기
# dict_1.update({'weight': 67.8,'hobby': ['게임','독서']})
# print(dict_1)

# # 딕셔너리 값 변경하기
# dict_1['hoppy'] = ['축구','등산']
# print(dict_1)

# # 데이터 삭제하기
# del dict_1['weight']
# del dict_1['birth']
# del dict_1['addr']
# print(dict_1)

# li = [1, 2, 3, 4, 5, 1, 3]
# li.append(100)
# li
# c = li.count(0)
# c

# li.sort(reverse=True)
# li

# # 리스트 생성하기
# list_1 = [1, 2, 3, 4, 5, 1, 3]
# list_2 = []
# print(list_1)
# print(list_2)
# print(len(list_1))

# # 리스트 변경하기
# list_1[3] = 9999
# print(list_1)
# list_1.append(100)
# print(list_1)
# list_1.remove(9999)
# print(list_1)
# list_1.insert(0,777)
# print(list_1)

# # 리스트 복제하기
# list_2 = list_1.copy()
# print(list_2)

# list_1 = [897, 2, 1, 4, 99, 5.24, 17]
# print(list_1)

# # 뒤집기
# list_1.reverse()
# print(list_1)

# # 오름차순 정렬하기
# list_1.sort()
# print(list_1)

# # 내림차순 정렬하기
# list_1.sort(reverse=True)
# print(list_1)























# st.write("파이썬의 세계에 오신 것을 환영합니다.")
# "a" + "bcd" + str(5)
# "a" + "bcd" + "5"

# a = 6
# for a in range(2,10):
#     " "
#     a, "단 입니다"
#     for i in range(1,10,1):
#         b = str(a) + "X" + str(i) + "=" + str(a*i)
#         b


# grade = 52

# if grade >= 90: 
#     "A"
# elif grade >= 80:
#     "B"
# elif grade >= 70:
#     "C"
# elif grade >= 60:
#     "D"
# else:
#     "F"
