def solution(r1, r2):
    answer = 0

    for x in range(-r2, r2 + 1): #정수 좌표의 대한 반복문
        for y in range(-r2, r2 + 1):
            distance_squared = x**2 + y**2 # 현재 좌표까지의 거리 제곱 계산

            if r1**2 <= distance_squared <= r2**2:  # 두 원의 반지름 제곱 값 사이에 속하면 answer + 1
                answer += 1

    return answer



r1 = 6  #출력
r2 = 8
result = solution(r1, r2)
print(result)
