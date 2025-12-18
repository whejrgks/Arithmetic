"""
연산자 전략 팩토리 클래스
"""
from typing import Optional
from src.operations.base import OperationStrategy
from src.operations.add import AddOperation
from src.operations.subtract import SubtractOperation
from src.operations.multiply import MultiplyOperation
from src.operations.divide import DivideOperation


class OperationFactory:
    """연산자 문자열을 전략 객체로 변환하는 팩토리 클래스"""
    
    # 연산자 문자열과 전략 클래스 매핑
    _operations: dict[str, type[OperationStrategy]] = {
        "+": AddOperation,
        "-": SubtractOperation,
        "×": MultiplyOperation,
        "*": MultiplyOperation,  # 별표도 곱셈으로 처리
        "/": DivideOperation,
        "÷": DivideOperation,  # 나눗셈 기호도 처리
    }
    
    @classmethod
    def create(cls, operator: str) -> Optional[OperationStrategy]:
        """
        연산자 문자열에 해당하는 전략 객체를 생성합니다.
        
        Args:
            operator: 연산자 문자열 (+, -, ×, *, /, ÷)
            
        Returns:
            OperationStrategy 인스턴스, 지원하지 않는 연산자일 경우 None
        """
        operation_class = cls._operations.get(operator)
        if operation_class:
            return operation_class()
        return None
    
    @classmethod
    def is_supported(cls, operator: str) -> bool:
        """
        연산자가 지원되는지 확인합니다.
        
        Args:
            operator: 연산자 문자열
            
        Returns:
            지원되는 연산자일 경우 True, 그렇지 않으면 False
        """
        return operator in cls._operations
    
    @classmethod
    def get_supported_operators(cls) -> list[str]:
        """
        지원되는 모든 연산자 목록을 반환합니다.
        
        Returns:
            지원되는 연산자 문자열 리스트
        """
        return list(cls._operations.keys())

