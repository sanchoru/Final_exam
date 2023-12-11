def solution(letter):
    morse = {                                                           #모스코드 라이브러리
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
        '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
        '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
        '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
        '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
        '--..': 'z'
    }

    morses = letter.split(' ')                                          #모스코드 공백인식
    text = ''

    for morsetarget in morses:                                          #모스코드 해독
        if morsetarget in morse:
            text += morse[morsetarget]
    return text

def lenth(letter):                                                      #문자열의 길이 제한
    if 1 <= len(letter) <= 1000:
        return solution(letter)
    else:
        return "입력된 문자열의 길이는 1에서 1000 사이여야 합니다."


letter = "-. --- .--. .- .. -. -. --- --. .- .. -."                     #출력
result = lenth(letter)
print(result)                                                           