"""
CalculatorController 테스트
"""
import pytest
from src.calculator_controller import CalculatorController
from src.arithmetic import Arithmetic


class TestCalculatorController:
    """CalculatorController 테스트 클래스"""
    
    def setup_method(self):
        """각 테스트 전에 실행"""
        self.controller = CalculatorController()
    
    # 숫자 입력 처리 테스트
    def test_input_number_basic(self):
        """기본 숫자 입력 테스트"""
        self.controller.input_number("5")
        assert self.controller.get_display_value() == "5"
    
    def test_input_number_multiple_digits(self):
        """여러 자리 숫자 입력 테스트"""
        self.controller.input_number("1")
        self.controller.input_number("2")
        self.controller.input_number("3")
        assert self.controller.get_display_value() == "123"
    
    def test_input_number_after_operator(self):
        """연산자 후 숫자 입력 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("+")
        self.controller.input_number("3")
        assert self.controller.get_display_value() == "3"
    
    def test_input_number_after_calculate(self):
        """계산 후 숫자 입력 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("+")
        self.controller.input_number("3")
        self.controller.calculate()
        assert self.controller.get_display_value() == "8"
        self.controller.input_number("2")
        assert self.controller.get_display_value() == "2"
    
    # 연산자 선택 처리 테스트
    def test_set_operator_add(self):
        """덧셈 연산자 설정 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("+")
        assert self.controller.get_display_value() == "5"
    
    def test_set_operator_subtract(self):
        """뺄셈 연산자 설정 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("-")
        assert self.controller.get_display_value() == "5"
    
    def test_set_operator_multiply(self):
        """곱셈 연산자 설정 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("×")
        assert self.controller.get_display_value() == "5"
    
    def test_set_operator_divide(self):
        """나눗셈 연산자 설정 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("/")
        assert self.controller.get_display_value() == "5"
    
    def test_set_operator_chain(self):
        """연속 연산자 설정 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("+")
        self.controller.input_number("3")
        self.controller.set_operator("-")
        # 이전 연산이 먼저 계산되어야 함
        assert self.controller.get_display_value() == "8"
    
    # 등호(=) 처리 테스트
    def test_calculate_add(self):
        """덧셈 계산 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("+")
        self.controller.input_number("3")
        self.controller.calculate()
        assert self.controller.get_display_value() == "8"
    
    def test_calculate_subtract(self):
        """뺄셈 계산 테스트"""
        self.controller.input_number("1")
        self.controller.input_number("0")
        self.controller.set_operator("-")
        self.controller.input_number("3")
        self.controller.calculate()
        assert self.controller.get_display_value() == "7"
    
    def test_calculate_multiply(self):
        """곱셈 계산 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("×")
        self.controller.input_number("3")
        self.controller.calculate()
        assert self.controller.get_display_value() == "15"
    
    def test_calculate_divide(self):
        """나눗셈 계산 테스트"""
        self.controller.input_number("1")
        self.controller.input_number("0")
        self.controller.set_operator("/")
        self.controller.input_number("2")
        self.controller.calculate()
        assert self.controller.get_display_value() == "5"
    
    def test_calculate_divide_decimal(self):
        """소수점 포함 나눗셈 계산 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("/")
        self.controller.input_number("2")
        self.controller.calculate()
        assert self.controller.get_display_value() == "2.5"
    
    def test_calculate_divide_by_zero(self):
        """0으로 나누기 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("/")
        self.controller.input_number("0")
        self.controller.calculate()
        assert self.controller.get_display_value() == "Error"
    
    def test_calculate_without_operator(self):
        """연산자 없이 계산 테스트"""
        self.controller.input_number("5")
        self.controller.calculate()
        # 연산자가 없으면 아무 일도 일어나지 않음
        assert self.controller.get_display_value() == "5"
    
    # 초기화(Clear) 처리 테스트
    def test_clear(self):
        """Clear 테스트"""
        self.controller.input_number("123")
        self.controller.set_operator("+")
        self.controller.input_number("456")
        self.controller.clear()
        assert self.controller.get_display_value() == "0"
        # 상태 확인
        assert self.controller._operator is None
        assert self.controller._previous_value is None
        assert self.controller._waiting_for_operand is False
    
    def test_clear_after_error(self):
        """에러 후 Clear 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("/")
        self.controller.input_number("0")
        self.controller.calculate()
        assert self.controller.get_display_value() == "Error"
        self.controller.clear()
        assert self.controller.get_display_value() == "0"
    
    # 부호 변경(+/-) 처리 테스트
    def test_toggle_sign_positive_to_negative(self):
        """양수에서 음수로 변경 테스트"""
        self.controller.input_number("5")
        self.controller.toggle_sign()
        assert self.controller.get_display_value() == "-5"
    
    def test_toggle_sign_negative_to_positive(self):
        """음수에서 양수로 변경 테스트"""
        self.controller.input_number("5")
        self.controller.toggle_sign()
        self.controller.toggle_sign()
        assert self.controller.get_display_value() == "5"
    
    def test_toggle_sign_zero(self):
        """0의 부호 변경 테스트 (변경되지 않아야 함)"""
        self.controller.toggle_sign()
        assert self.controller.get_display_value() == "0"
    
    def test_toggle_sign_after_calculate(self):
        """계산 결과의 부호 변경 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("-")
        self.controller.input_number("1")
        self.controller.input_number("0")
        self.controller.calculate()
        assert self.controller.get_display_value() == "-5"
        self.controller.toggle_sign()
        assert self.controller.get_display_value() == "5"
    
    # 소수점 처리 테스트
    def test_input_decimal(self):
        """소수점 입력 테스트"""
        self.controller.input_number("5")
        self.controller.input_decimal()
        assert self.controller.get_display_value() == "5."
        self.controller.input_number("2")
        assert self.controller.get_display_value() == "5.2"
    
    def test_input_decimal_after_operator(self):
        """연산자 후 소수점 입력 테스트"""
        self.controller.input_number("5")
        self.controller.set_operator("+")
        self.controller.input_decimal()
        assert self.controller.get_display_value() == "0."
        self.controller.input_number("5")
        assert self.controller.get_display_value() == "0.5"
    
    def test_input_decimal_duplicate(self):
        """중복 소수점 입력 테스트 (무시되어야 함)"""
        self.controller.input_number("5")
        self.controller.input_decimal()
        self.controller.input_decimal()  # 두 번째 소수점은 무시
        assert self.controller.get_display_value() == "5."
    
    def test_calculate_decimal_result(self):
        """소수점 결과 계산 테스트"""
        self.controller.input_number("1")
        self.controller.input_decimal()
        self.controller.input_number("5")
        self.controller.set_operator("+")
        self.controller.input_number("2")
        self.controller.input_decimal()
        self.controller.input_number("5")
        self.controller.calculate()
        assert self.controller.get_display_value() == "4"
    
    # 복합 시나리오 테스트
    def test_complex_calculation(self):
        """복잡한 계산 시나리오 테스트"""
        # 10 + 5 - 3 * 2 / 4
        self.controller.input_number("1")
        self.controller.input_number("0")
        self.controller.set_operator("+")
        self.controller.input_number("5")
        self.controller.calculate()  # 15
        self.controller.set_operator("-")
        self.controller.input_number("3")
        self.controller.calculate()  # 12
        self.controller.set_operator("×")
        self.controller.input_number("2")
        self.controller.calculate()  # 24
        self.controller.set_operator("/")
        self.controller.input_number("4")
        self.controller.calculate()  # 6
        assert self.controller.get_display_value() == "6"
    
    def test_continuous_operator_change(self):
        """연속 연산자 변경 테스트"""
        self.controller.input_number("1")
        self.controller.input_number("0")
        self.controller.set_operator("+")
        self.controller.set_operator("-")
        self.controller.set_operator("×")
        self.controller.input_number("2")
        self.controller.calculate()
        assert self.controller.get_display_value() == "20"
    
    # 에러 처리 테스트
    def test_error_recovery(self):
        """에러 복구 테스트"""
        # 0으로 나누기로 에러 발생
        self.controller.input_number("5")
        self.controller.set_operator("/")
        self.controller.input_number("0")
        self.controller.calculate()
        assert self.controller.get_display_value() == "Error"
        
        # Clear로 복구
        self.controller.clear()
        assert self.controller.get_display_value() == "0"
        
        # 정상 계산 가능
        self.controller.input_number("5")
        self.controller.set_operator("+")
        self.controller.input_number("3")
        self.controller.calculate()
        assert self.controller.get_display_value() == "8"
    
    def test_display_callback(self):
        """디스플레이 콜백 테스트"""
        callback_values = []
        
        def callback(value: str):
            callback_values.append(value)
        
        self.controller.set_display_callback(callback)
        self.controller.input_number("5")
        assert "5" in callback_values
        
        self.controller.set_operator("+")
        self.controller.input_number("3")
        assert "3" in callback_values
        
        self.controller.calculate()
        assert "8" in callback_values

