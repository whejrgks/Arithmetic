"""
정수 나눗셈 연산 전략 (소수점 버림)
"""
from src.operations.base import OperationStrategy
from typing import Union


class DivideIntegerOperation(OperationStrategy):
    """정수 나눗셈 연산 전략 클래스 (소수점 버림)"""
    
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        정수 나눗셈 연산을 실행합니다 (소수점 버림).
        
        Args:
            a: 첫 번째 피연산자
            b: 두 번째 피연산자
            
        Returns:
            a // b의 결과 (정수 나눗셈)
            
        Raises:
            ArithmeticError: b가 0일 경우
        """
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b
    
    def get_symbol(self) -> str:
        """
        정수 나눗셈 연산자 기호를 반환합니다.
        
        Returns:
            "//" 문자열
        """
        return "//"

