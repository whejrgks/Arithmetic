class Arithmetic:
    """사칙연산 클래스"""
    
    def add(self, a, b):
        """덧셈 연산"""
        return a + b
    
    def subtract(self, a, b):
        """뺄셈 연산"""
        return a - b
    
    def multiply(self, a, b):
        """곱셈 연산"""
        return a * b
    
    def divide(self, a, b):
        """나눗셈 연산 (정수 나눗셈, 소수점 버림)"""
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b


if __name__ == "__main__":
    """직접 실행 시 예제 실행"""
    arithmetic = Arithmetic()
    
    print("=" * 50)
    print("사칙연산 모듈 실행 예제")
    print("=" * 50)
    print()
    
    # 덧셈 예제
    print("【덧셈 연산】")
    print(f"  1 + 10 = {arithmetic.add(1, 10)}")
    print(f"  0 + 1 = {arithmetic.add(0, 1)}")
    print(f"  -1 + (-10) = {arithmetic.add(-1, -10)}")
    print()
    
    # 뺄셈 예제
    print("【뺄셈 연산】")
    print(f"  5 - 2 = {arithmetic.subtract(5, 2)}")
    print()
    
    # 곱셈 예제
    print("【곱셈 연산】")
    print(f"  -5 * -3 = {arithmetic.multiply(-5, -3)}")
    print(f"  0 * 10 = {arithmetic.multiply(0, 10)}")
    print()
    
    # 나눗셈 예제
    print("【나눗셈 연산】")
    print(f"  5 / 2 = {arithmetic.divide(5, 2)} (정수 나눗셈)")
    print(f"  -10 / 2 = {arithmetic.divide(-10, 2)}")
    print()
    
    # 예외 처리 예제
    print("【예외 처리】")
    try:
        result = arithmetic.divide(0, 0)
        print(f"  0 / 0 = {result}")
    except ArithmeticError as e:
        print(f"  0 / 0 → ArithmeticError: {e}")
    print()
    
    print("=" * 50)
    print("실행 완료")
    print("=" * 50)
