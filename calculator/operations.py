# 더하기
def add(a, b):
    return a + b


# 빼기
def minus(a, b):
    return a - b


# 곱하기
def multiply(a, b):
    return a * b

    
# 나누기
def divide(a, b):
    if b == 0:
        raise ValueError("0은 나눌 수 없습니다.")
    return a / b


# 몫
def quotient(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a // b


# 제곱
def power(a, b):
    return a ** b


# 퍼센트 구하기
def percent(a, b):
    # a의 b퍼센트 값
    return (a * b) / 100

