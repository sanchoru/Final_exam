def solution(age):
    if 0 <= age <= 1000:  # age를 1000이하로 제한
        answer = ""
        while age > 0:    # age는 자연수로 제한
            digit = age % 10
            answer = chr(ord('a') + digit) + answer # ASCII코드값을 구한뒤 chr함수로 문자 변환
            age //= 10

        return answer if answer else 'a'  # age가 0인 경우에는 a를 반환

age = 248                    #출력
result = solution(age)
print(result)
