def solution(list):
    for i in range(1000,9999):
        for digit in range(len(list)):
            a = digit
            b = i
            if not (b%10 >= a 
