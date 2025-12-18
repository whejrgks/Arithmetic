"""
계산기 컨트롤러 클래스
계산기 상태 관리 및 연산 실행을 담당합니다.
"""
from typing import Optional, Callable
from src.arithmetic import Arithmetic
from src.operations.factory import OperationFactory
from src.operations.base import OperationStrategy


class CalculatorController:
    """
    계산기 상태 관리 및 연산 실행 컨트롤러
    
    책임:
    - 계산기 상태 관리 (현재 값, 이전 값, 연산자, 입력 모드)
    - 연산 실행 및 결과 계산
    - 예외 처리 및 에러 상태 관리
    """
    
    def __init__(self, arithmetic: Optional[Arithmetic] = None):
        """
        CalculatorController 초기화
        
        Args:
            arithmetic: Arithmetic 인스턴스 (의존성 주입, None일 경우 새로 생성)
        """
        self._arithmetic = arithmetic or Arithmetic()
        # 상태 관리 변수
        self._current_value: str = "0"  # 현재 입력/표시 값
        self._previous_value: Optional[float] = None  # 이전 값
        self._operator: Optional[str] = None  # 선택된 연산자
        self._waiting_for_operand: bool = False  # 새 피연산자 입력 대기 여부
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
        # 에러 상태일 경우 Clear 처리
        if self._current_value == "Error":
            self.clear()
            self._current_value = digit
            self._update_display()
            return
        
        # 숫자 검증
        if not digit.isdigit() or len(digit) != 1:
            return
        
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
        """
        소수점 입력을 처리합니다.
        """
        # 에러 상태일 경우 Clear 처리
        if self._current_value == "Error":
            self.clear()
            self._current_value = "0."
            self._update_display()
            return
        
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
            operator: 연산자 문자열 (+, -, ×, *, /, ÷ 등 UI 표시용 기호 포함)
        """
        # 에러 상태일 경우 무시
        if self._current_value == "Error":
            return
        
        # UI 표시용 기호를 내부 기호로 정규화
        operator = self._normalize_operator(operator)
        
        if not OperationFactory.is_supported(operator):
            return
        
        # 이전 연산이 있고, 피연산자를 기다리는 상태가 아니면 먼저 계산
        if self._operator is not None and not self._waiting_for_operand:
            self.calculate()
            # 계산 후 에러 상태면 연산자 설정 중단
            if self._current_value == "Error":
                return
        
        try:
            # 현재 값을 이전 값으로 저장
            self._previous_value = float(self._current_value)
            self._operator = operator
            self._waiting_for_operand = True
        except (ValueError, OverflowError):
            self._current_value = "Error"
            self._update_display()
    
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
            
            # Strategy 패턴을 사용하여 연산 실행 (if-elif 체인 제거)
            # Arithmetic 클래스도 내부적으로 Strategy 패턴을 사용하므로
            # 일관성 있게 Strategy를 직접 사용
            result = operation.execute(self._previous_value, current)
            
            # 결과를 문자열로 변환 (정수면 정수로, 소수면 소수로)
            # 오버플로우 체크
            if abs(result) > 1e15:
                self._current_value = "Error"
            elif result == int(result):
                self._current_value = str(int(result))
            else:
                # 소수점 이하 불필요한 0 제거
                self._current_value = str(result).rstrip('0').rstrip('.')
                if not self._current_value or self._current_value == "-":
                    self._current_value = "0"
            
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
        """
        현재 값의 부호를 변경합니다 (+/-).
        """
        # 에러 상태일 경우 무시
        if self._current_value == "Error":
            return
        
        if self._current_value != "0" and self._current_value != "0.":
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
    
    def _normalize_operator(self, operator: str) -> str:
        """
        UI 표시용 연산자 기호를 내부 연산자 기호로 정규화합니다.
        
        Args:
            operator: UI 표시용 연산자 기호 (예: "−", "×", "÷")
            
        Returns:
            내부 연산자 기호 (예: "-", "*", "/")
        """
        # UI 표시용 기호를 내부 기호로 매핑
        operator_map = {
            "−": "-",  # 빼기 기호 (U+2212) → 하이픈 마이너스
            "×": "*",  # 곱하기 기호 (U+00D7) → 별표
            "÷": "/",  # 나누기 기호 (U+00F7) → 슬래시
        }
        
        # 매핑에 있으면 변환, 없으면 그대로 반환
        return operator_map.get(operator, operator)

