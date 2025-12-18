"""
간단한 사칙연산 콘솔 프로그램
"""
import sys
from src.arithmetic import Arithmetic


def main() -> None:
    """
    메인 함수
    
    콘솔에서 사용자 입력을 받아 사칙연산을 수행합니다.
    """
    arithmetic = Arithmetic()
    
    try:
        # 첫 번째 정수값 입력
        first_num = int(input("첫번째 정수값 >>"))
        
        # 연산자 입력
        operator = input("연산자 >>").strip()
        
        # 두 번째 정수값 입력
        second_num = int(input("두번째 정수값 >>"))
        
        # 결과 뷰 화면
        print("=" * 50)
        
        # 연산자에 따른 계산
        if operator == "+":
            result = arithmetic.add(first_num, second_num)
            print(f"{first_num} + {second_num}을 계산합니다.")
        elif operator == "-":
            result = arithmetic.subtract(first_num, second_num)
            print(f"{first_num} - {second_num}을 계산합니다.")
        elif operator == "*":
            result = arithmetic.multiply(first_num, second_num)
            print(f"{first_num} * {second_num}을 계산합니다.")
        elif operator == "/":
            result = arithmetic.divide_quotient(first_num, second_num)
            print(f"{first_num} / {second_num}을 계산합니다.")
        elif operator == "//":
            result = arithmetic.divide(first_num, second_num)
            print(f"{first_num} // {second_num}을 계산합니다.")
        else:
            print(f"지원하지 않는 연산자입니다: {operator}")
            return
        
        print("=" * 50)
        
        # 결과 출력
        print(f"{first_num}{operator}{second_num}={result}입니다.")
            
    except ValueError:
        print("오류: 정수값을 입력해주세요.")
    except ArithmeticError as e:
        print(f"오류: {e}")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()

