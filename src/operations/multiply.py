"""
곱셈 연산 전략
"""
from src.operations.base import OperationStrategy
from typing import Union


class MultiplyOperation(OperationStrategy):
    """곱셈 연산 전략 클래스"""
    
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        곱셈 연산을 실행합니다.
        
        Args:
            a: 첫 번째 피연산자
            b: 두 번째 피연산자
            
        Returns:
            a * b의 결과
        """
        return a * b
    
    def get_symbol(self) -> str:
        """
        곱셈 연산자 기호를 반환합니다.
        
        Returns:
            "×" 문자열
        """
        return "×"

