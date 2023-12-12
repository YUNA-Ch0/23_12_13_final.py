# Q.5 10점
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
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