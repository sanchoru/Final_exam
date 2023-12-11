def solution(numbers):
    def funtion(x):
        return x * 4
    number = sorted(map(str, numbers), key=funtion, reverse=True)  # numbers를 문자열로 변환 후 정렬

    return ''.join(number) # 정렬된 숫자를 이어붙여 문자열로 반환


numbers = [8, 30, 17, 2, 23]  #출력
answer = solution(numbers)
print(answer)
