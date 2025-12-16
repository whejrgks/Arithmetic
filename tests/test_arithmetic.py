"""
사칙연산 모듈 테스트
TC-CMM-001 / TC-AO-001
"""
import pytest
from src.arithmetic import Arithmetic


class TestArithmetic:
    """사칙연산 테스트 클래스"""
    
    def setup_method(self):
        """각 테스트 메서드 실행 전 초기화"""
        self.arithmetic = Arithmetic()
    
    # 덧셈 테스트
    def test_add_1_plus_10(self):
        """덧셈 테스트: 1 + 10 = 11"""
        assert self.arithmetic.add(1, 10) == 11
    
    def test_add_0_plus_1(self):
        """덧셈 테스트: 0 + 1 = 1"""
        assert self.arithmetic.add(0, 1) == 1
    
    def test_add_negative_numbers(self):
        """덧셈 테스트: -1 + (-10) = -11"""
        assert self.arithmetic.add(-1, -10) == -11
    
    # 뺄셈 테스트
    def test_subtract_5_minus_2(self):
        """뺄셈 테스트: 5 - 2 = 3"""
        assert self.arithmetic.subtract(5, 2) == 3
    
    # 곱셈 테스트
    def test_multiply_negative_numbers(self):
        """곱셈 테스트: -5 * -3 = 15"""
        assert self.arithmetic.multiply(-5, -3) == 15
    
    def test_multiply_by_zero(self):
        """곱셈 테스트: 0 * 10 = 0"""
        assert self.arithmetic.multiply(0, 10) == 0
    
    # 나눗셈 테스트 (정수)
    def test_divide_integer_5_by_2(self):
        """나눗셈 테스트 (정수): 5 / 2 = 2"""
        assert self.arithmetic.divide(5, 2) == 2
    
    # 나눗셈 테스트 (몫 - 소수점)
    def test_divide_quotient_5_by_2(self):
        """나눗셈 테스트 (몫): 5 ÷ 2 = 2.5"""
        assert self.arithmetic.divide_quotient(5, 2) == 2.5
    
    def test_divide_negative_10_by_2(self):
        """나눗셈 테스트: -10 / 2 = -5"""
        assert self.arithmetic.divide(-10, 2) == -5
    
    # 예외 처리 테스트
    def test_divide_by_zero_exception(self):
        """예외 처리 테스트: 0 / 0 → ArithmeticException"""
        with pytest.raises(ArithmeticError):
            self.arithmetic.divide(0, 0)

