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