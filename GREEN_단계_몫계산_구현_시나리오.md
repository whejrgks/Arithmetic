# GREEN 단계 몫 계산 기능 최소 단위 구현 시나리오

## 구현 범위
**몫 계산 기능 (`divide_quotient` 메서드)** 구현
- 소수점 포함 몫: `divide_quotient(5, 2) = 2.5`

## 구현 단계

### 1단계: 몫 계산 기능 구현 (`divide_quotient` 메서드)

#### 1.1 테스트 케이스 분석
- `test_divide_quotient_5_by_2`: `divide_quotient(5, 2) == 2.5`
  - 소수점을 포함한 나눗셈 결과 검증
  - 정수 나눗셈(`divide`)과 달리 소수점을 유지해야 함

#### 1.2 최소 구현 코드
```python
def divide_quotient(self, a, b):
    """몫 계산 연산 (소수점 포함)"""
    return a / b
```

**예상 결과**: 
- 1개 몫 계산 테스트 통과
- Python의 기본 나눗셈 연산자(`/`)로 소수점 결과 반환

#### 1.3 예외 처리 고려사항
- 테스트 케이스에 0으로 나누기 예외 처리가 없음
- 최소 단위 구현이므로 예외 처리는 선택사항
- 하지만 `divide` 메서드와의 일관성을 위해 예외 처리 추가 권장

**예외 처리 포함 버전**:
```python
def divide_quotient(self, a, b):
    """몫 계산 연산 (소수점 포함)"""
    if b == 0:
        raise ArithmeticError("Division by zero")
    return a / b
```

---

## 최종 구현 코드 구조

### 추가될 메서드

#### 옵션 1: 최소 구현 (예외 처리 없음)
```python
def divide_quotient(self, a, b):
    """몫 계산 연산 (소수점 포함)"""
    return a / b
```

#### 옵션 2: 예외 처리 포함 (권장)
```python
def divide_quotient(self, a, b):
    """몫 계산 연산 (소수점 포함)"""
    if b == 0:
        raise ArithmeticError("Division by zero")
    return a / b
```

### 전체 클래스 구조 (구현 후)
```python
class Arithmetic:
    """사칙연산 클래스"""
    
    def add(self, a, b):
        """덧셈 연산"""
        return a + b
    
    def subtract(self, a, b):
        """뺄셈 연산"""
        return a - b
    
    def multiply(self, a, b):
        """곱셈 연산"""
        return a * b
    
    def divide(self, a, b):
        """나눗셈 연산 (정수 나눗셈, 소수점 버림)"""
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b
    
    def divide_quotient(self, a, b):  # 새로 추가
        """몫 계산 연산 (소수점 포함)"""
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a / b
```

---

## 테스트 실행 계획

### 구현 후 테스트 실행
```bash
python -m pytest tests/test_arithmetic.py -k "divide_quotient" -v
```

**예상 결과**:
- ✅ `test_divide_quotient_5_by_2` 통과

### 전체 테스트 실행
```bash
python -m pytest tests/test_arithmetic.py -v
```

**예상 결과**:
- ✅ 덧셈 테스트 3개 통과
- ✅ 뺄셈 테스트 1개 통과
- ✅ 곱셈 테스트 2개 통과
- ✅ 나눗셈 테스트 3개 통과
- ✅ 몫 계산 테스트 1개 통과 (새로 통과)

**총 10개 테스트 모두 통과 예상**

---

## 추가 작업 (선택사항)

### 실행 예제 업데이트
`if __name__ == "__main__":` 블록에 몫 계산 예제 추가

```python
# 나눗셈 예제
print("【나눗셈 연산】")
print(f"  5 / 2 = {arithmetic.divide(5, 2)} (정수 나눗셈)")
print(f"  -10 / 2 = {arithmetic.divide(-10, 2)}")
print()

# 몫 계산 예제
print("【몫 계산 연산】")
print(f"  5 ÷ 2 = {arithmetic.divide_quotient(5, 2)} (소수점 포함)")
print()
```

**위치**: 나눗셈 예제 다음, 예외 처리 예제 전

---

## 구현 원칙

### 최소 단위 구현 원칙
1. **테스트를 통과하는 최소한의 코드만 작성**
   - Python의 기본 나눗셈 연산자(`/`) 사용
   - 소수점 결과 자동 반환

2. **일관성 유지**
   - `divide` 메서드와 유사한 구조
   - 예외 처리 추가 시 `divide`와 동일한 방식

3. **구현 차이점**
   - `divide`: 정수 나눗셈 (`//`) - 소수점 버림
   - `divide_quotient`: 일반 나눗셈 (`/`) - 소수점 유지

---

## 검증 체크리스트

- [ ] `divide_quotient` 메서드 구현 확인
- [ ] `test_divide_quotient_5_by_2` 테스트 통과 확인
- [ ] 전체 테스트 실행 결과 확인 (10개 모두 통과 예상)
- [ ] (선택) 예외 처리 구현 확인
- [ ] (선택) 실행 예제에 몫 계산 추가 확인

---

## 주의사항

1. **나눗셈 연산자 차이**
   - `divide`: `//` (정수 나눗셈, 소수점 버림)
   - `divide_quotient`: `/` (일반 나눗셈, 소수점 유지)

2. **예외 처리 일관성**
   - `divide` 메서드에 예외 처리가 있으므로 일관성을 위해 추가 권장
   - 하지만 테스트 케이스에 없으므로 최소 구현에서는 선택사항

3. **반환 타입**
   - 정수 나눗셈: `int` 반환
   - 몫 계산: `float` 반환 (소수점 포함)

---

## 구현 옵션 비교

### 옵션 1: 최소 구현 (예외 처리 없음)
- **장점**: 테스트 케이스를 통과하는 최소한의 코드
- **단점**: 0으로 나누기 시 Python 기본 예외 발생 (일관성 부족)

### 옵션 2: 예외 처리 포함 (권장)
- **장점**: `divide` 메서드와 일관성 유지, 명확한 예외 처리
- **단점**: 최소 구현보다 약간 더 많은 코드

**권장**: 옵션 2 (예외 처리 포함) - 일관성과 안정성을 위해

---

**시나리오 작성일**: 2024-12-16  
**구현 예상 시간**: 약 2-3분  
**승인 대기 중**: ⏳

