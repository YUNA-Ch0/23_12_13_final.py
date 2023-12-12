#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번: 20222093 이름 : 조유나

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target): # my_strung을 my_string으로 수정
    if target in my_string:
        return 1
    else:
        return 0
# answer = 0 answer은 불필요한 변수임으로 삭제
# return answer 사용되지 않고 필요없는 부분
# 예시
my_string1 = "asdfghjkl"
target1 = "asdf"
result1 = solution(my_string1, target1)
print(result1)  #  1

my_string2 = "qwertyuio"
target2 = "zxcvb"
result2 = solution(my_string2, target2)
print(result2)  # 0

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse_code_dict = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'} 
    morse_code_list = letter.split(' ')
    #입력 모스 부호들을 공백 기준 리스트 변환
    answer = '' # return answer에 저장할 빈 문자열
    for code in morse_code_list: # 코드가 morse_code_dict에 있는지 확인
        if code in morse_code_dict:
            answer += morse_code_dict[code] 
            # morse_code_dict에 모스 부호에 맞는 영어 소문자를 
            # answer에 넣는다.
        else: 
            answer += code # 공백일때
    return answer # 영어 소문자로 바꾼 문자열을 return
# 실행
result = solution('.... --- -- . ... .-- . . - .... --- -- .')
print(result)

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    age_planet_dict = {'0': 'a', '1': 'b', '2': 'c', '3': 'd','4': 'e',
                       '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'}
    answer = ''
    age_str = str(age)
    age_in_alpha = [age_planet_dict[char] for char in age_str]

    return ''.join(age_in_alpha)
    return answer
    #
age = 64
result = solution(age)
print(result)

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    # 두 원의 중심 사이의 거리
    distance = (r1**2 + r2**2)**0.5 # 두 원 중심 사이 거리 계산

    # 두 원이 완전히 겹칠때
    if distance == 0 and r1 == r2:
        return (r1 + 1)**2

    # 두 원이 겹치거나 내접
    if distance <= r1 + r2:
        # 두 원이 겹치는 부분 정수 좌표 개수
        count = 0 # 겹치는 부분 초기화
        for x in range(-r1, r1 + 1): # x좌표 반복문
            for y in range(-r1, r1 + 1): # y좌표 반복문
                if r2 - r1 <= x**2 + y**2 <= r1**2:
                    count += 1
        return count

    # 두 원이 겹치지 않는 경우
    return 0
# 실행
r1, r2 = 8, 12
result = solution(r1, r2)
print(result)

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    st_num =[]
    answer = '' # 마지막으로 반환 문자열
    for i in range(len(numbers)): # 입력된 numbers 리스트를 돌아본다
        st = str(numbers[i]) * 5 # 각각의 숫자 5번 비교
        st_num.append([st,i]) # 숫자와 인덱스 묶어서 리스트에 추가한다
    st_num.sort(reverse=True) # 문자열 기준 내림차순 정렬

    for i in range(len(st_num)):
        answer += str(numbers[st_num[i][1]])
    if len(set(answer)) == 1 and answer[0] == '0':
        return '0'
    # 숫자가 모두 '0'이면 '0' 반환
    return answer
# 실행
numbers = [8, 30, 17, 2, 23]
result = solution(numbers)
print (result)