# Q.4 10점
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
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