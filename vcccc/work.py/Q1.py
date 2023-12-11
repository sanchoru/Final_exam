import os
import time

def q1(my_string, target):
    if my_string.islower() and target.islower():                   #target, my_string의 영소문자 유무 제한
        if 1 <= len(my_string) <= 100 and 1 <= len(target) <=100:  #target, my_string의 단어의 길이를 제한
            if target in my_string:                                #target이 my_string의 부분문자열이면 1을 반환 그렇지 않을경우 0을 반환
                return 1
            else:
                return 0