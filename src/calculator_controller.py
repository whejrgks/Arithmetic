"""
계산기 컨트롤러 클래스
계산기 상태 관리 및 연산 실행을 담당합니다.
"""
from typing import Optional, Callable
from src.arithmetic import Arithmetic
from src.operations.factory import OperationFactory
from src.operations.base import OperationStrategy


class CalculatorController:
    """계산기 상태 관리 및 연산 실행 컨트롤러"""
    
    def __init__(self, arithmetic: Optional[Arithmetic] = None):
        """
        CalculatorController 초기화
        
        Args:
            arithmetic: Arithmetic 인스턴스 (의존성 주입, None일 경우 새로 생성)
        """
        self._arithmetic = arithmetic or Arithmetic()
        self._current_value: str = "0"
        self._previous_value: Optional[float] = None
        self._operator: Optional[str] = None
        self._waiting_for_operand: bool = False
        self._display_callback: Optional[Callable[[str], None]] = None
    
    def set_display_callback(self, callback: Callable[[str], None]) -> None:
        """
        디스플레이 업데이트 콜백 함수를 설정합니다.
        
        Args:
            callback: 디스플레이 값을 업데이트하는 함수
        """
        self._display_callback = callback
    
    def _update_display(self) -> None:
        """디스플레이를 업데이트합니다."""
        if self._display_callback:
            self._display_callback(self._current_value)
    
    def input_number(self, digit: str) -> None:
        """
        숫자 입력을 처리합니다.
        
        Args:
            digit: 입력된 숫자 문자열 (0-9)
        """
        if self._waiting_for_operand:
            self._current_value = digit
            self._waiting_for_operand = False
        else:
            if self._current_value == "0":
                self._current_value = digit
            else:
                self._current_value += digit
        self._update_display()
    
    def input_decimal(self) -> None:
        """소수점 입력을 처리합니다."""
        if self._waiting_for_operand:
            self._current_value = "0."
            self._waiting_for_operand = False
        elif "." not in self._current_value:
            self._current_value += "."
        self._update_display()
    
    def set_operator(self, operator: str) -> None:
        """
        연산자를 설정합니다.
        
        Args:
            operator: 연산자 문자열 (+, -, ×, /)
        """
        if not OperationFactory.is_supported(operator):
            return
        
        if self._operator and not self._waiting_for_operand:
            # 이전 연산이 있으면 먼저 계산
            self.calculate()
        
        self._previous_value = float(self._current_value)
        self._operator = operator
        self._waiting_for_operand = True
    
    def calculate(self) -> None:
        """현재 연산을 실행합니다."""
        if self._operator is None or self._previous_value is None:
            return
        
        try:
            current = float(self._current_value)
            operation: Optional[OperationStrategy] = OperationFactory.create(self._operator)
            
            if operation is None:
                self._current_value = "Error"
                self._update_display()
                return
            
            # Arithmetic 클래스를 사용하여 연산 실행
            if self._operator == "+":
                result = self._arithmetic.add(self._previous_value, current)
            elif self._operator == "-":
                result = self._arithmetic.subtract(self._previous_value, current)
            elif self._operator in ("×", "*"):
                result = self._arithmetic.multiply(self._previous_value, current)
            elif self._operator in ("/", "÷"):
                result = self._arithmetic.divide_quotient(self._previous_value, current)
            else:
                result = operation.execute(self._previous_value, current)
            
            # 결과를 문자열로 변환 (정수면 정수로, 소수면 소수로)
            if result == int(result):
                self._current_value = str(int(result))
            else:
                self._current_value = str(result)
            
            self._operator = None
            self._previous_value = None
            self._waiting_for_operand = True
            self._update_display()
            
        except ArithmeticError as e:
            self._current_value = "Error"
            self._operator = None
            self._previous_value = None
            self._waiting_for_operand = True
            self._update_display()
        except Exception as e:
            self._current_value = "Error"
            self._update_display()
    
    def clear(self) -> None:
        """계산기를 초기화합니다."""
        self._current_value = "0"
        self._previous_value = None
        self._operator = None
        self._waiting_for_operand = False
        self._update_display()
    
    def toggle_sign(self) -> None:
        """현재 값의 부호를 변경합니다."""
        if self._current_value != "0":
            if self._current_value.startswith("-"):
                self._current_value = self._current_value[1:]
            else:
                self._current_value = "-" + self._current_value
            self._update_display()
    
    def get_display_value(self) -> str:
        """
        현재 디스플레이 값을 반환합니다.
        
        Returns:
            현재 디스플레이 값 문자열
        """
        return self._current_value

