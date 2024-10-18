from fastapi import FastAPI, HTTPException
from operations import add, minus, multiply, divide, quotient, percent, power

# 유효성 검사 함수들
def validate_operations(operations: str):
    if operations not in ['+', '-', '*', '/', '//', '**', '%']:
        raise ValueError("계산할 수 없는 수식을 넣으셨습니다.")
    
def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("입력값이 잘못됐습니다. 다시 입력해주세요.")

app = FastAPI()

@app.post("/calcultator")
async def calculator(operations: str, a:float, b:float):
    try:
        validate_operations(operations)
        validate_numbers(a, b)
        
        if operations == '+':
            result = add(a, b)
        elif operations == '-':
            result = minus(a, b)
        elif operations == '*':
            result = multiply(a, b)
        elif operations == '/':
            result = divide(a, b)
        elif operations == '//':
            result = quotient(a, b)
        elif operations == '**':
            result = power(a, b)
        elif operations == '%':
            result = percent(a, b)
            
        return {f"{a} {operations} {b} " : result}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))