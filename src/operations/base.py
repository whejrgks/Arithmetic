"""
연산자 전략 패턴의 추상 기본 클래스
"""
from abc import ABC, abstractmethod
from typing import Union


class OperationStrategy(ABC):
    """연산자 전략 추상 클래스"""
    
    @abstractmethod
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        연산을 실행합니다.
        
        Args:
            a: 첫 번째 피연산자
            b: 두 번째 피연산자
            
        Returns:
            연산 결과
            
        Raises:
            ArithmeticError: 연산 중 오류 발생 시 (예: 0으로 나누기)
        """
        pass
    
    @abstractmethod
    def get_symbol(self) -> str:
        """
        연산자 기호를 반환합니다.
        
        Returns:
            연산자 기호 문자열
        """
        pass

