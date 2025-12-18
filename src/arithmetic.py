"""
사칙연산 클래스
Strategy 패턴을 사용하여 연산을 수행합니다.
"""
from typing import Union
from src.operations.add import AddOperation
from src.operations.subtract import SubtractOperation
from src.operations.multiply import MultiplyOperation
from src.operations.divide import DivideOperation
from src.operations.divide_integer import DivideIntegerOperation


class Arithmetic:
    """
    사칙연산 클래스
    Strategy 패턴을 사용하여 연산 로직을 분리합니다.
    기존 API는 유지하면서 내부적으로 Strategy 패턴을 활용합니다.
    """
    
    def __init__(self):
        """Arithmetic 클래스 초기화"""
        # Strategy 객체들을 미리 생성하여 재사용
        self._add_operation = AddOperation()
        self._subtract_operation = SubtractOperation()
        self._multiply_operation = MultiplyOperation()
        self._divide_operation = DivideOperation()
        self._divide_integer_operation = DivideIntegerOperation()
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        덧셈 연산
        
        Args:
            a: 첫 번째 피연산자
            b: 두 번째 피연산자
            
        Returns:
            a + b의 결과
        """
        return self._add_operation.execute(a, b)
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        뺄셈 연산
        
        Args:
            a: 첫 번째 피연산자
            b: 두 번째 피연산자
            
        Returns:
            a - b의 결과
        """
        return self._subtract_operation.execute(a, b)
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        곱셈 연산
        
        Args:
            a: 첫 번째 피연산자
            b: 두 번째 피연산자
            
        Returns:
            a * b의 결과
        """
        return self._multiply_operation.execute(a, b)
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        나눗셈 연산 (정수 나눗셈, 소수점 버림)
        
        Args:
            a: 첫 번째 피연산자
            b: 두 번째 피연산자
            
        Returns:
            a // b의 결과 (정수 나눗셈)
            
        Raises:
            ArithmeticError: b가 0일 경우
        """
        return self._divide_integer_operation.execute(a, b)
    
    def divide_quotient(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        몫 계산 연산 (소수점 포함)
        
        Args:
            a: 첫 번째 피연산자
            b: 두 번째 피연산자
            
        Returns:
            a / b의 결과 (소수점 포함)
            
        Raises:
            ArithmeticError: b가 0일 경우
        """
        return self._divide_operation.execute(a, b)


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
    
    # 몫 계산 예제
    print("【몫 계산 연산】")
    print(f"  5 ÷ 2 = {arithmetic.divide_quotient(5, 2)} (소수점 포함)")
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
