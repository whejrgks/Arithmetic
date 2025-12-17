# GREEN 단계 곱셈 기능 최소 단위 구현 시나리오

## 구현 범위
**곱셈 기능 (`multiply` 메서드)** 구현
- 음수 × 음수: `multiply(-5, -3) = 15`
- 0 포함: `multiply(0, 10) = 0`

## 구현 단계

### 1단계: 곱셈 기능 구현 (`multiply` 메서드)

#### 1.1 테스트 케이스 분석
- `test_multiply_negative_numbers`: `multiply(-5, -3) == 15`
  - 음수 × 음수 = 양수 검증
- `test_multiply_by_zero`: `multiply(0, 10) == 0`
  - 0을 포함한 곱셈 검증

#### 1.2 최소 구현 코드
```python
def multiply(self, a, b):
    """곱셈 연산"""
    return a * b
```

**예상 결과**: 
- 2개 곱셈 테스트 모두 통과
- Python의 기본 곱셈 연산자(`*`)로 충분히 처리 가능
- 음수 × 음수, 0 포함 곱셈 모두 자동 처리

---

## 최종 구현 코드 구조

### 추가될 메서드
```python
def multiply(self, a, b):
    """곱셈 연산"""
    return a * b
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
    
    def multiply(self, a, b):  # 새로 추가
        """곱셈 연산"""
        return a * b
    
    def divide(self, a, b):
        """나눗셈 연산 (정수 나눗셈, 소수점 버림)"""
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b
```

---

## 테스트 실행 계획

### 구현 후 테스트 실행
```bash
python -m pytest tests/test_arithmetic.py -k "multiply" -v
```

**예상 결과**:
- ✅ `test_multiply_negative_numbers` 통과
- ✅ `test_multiply_by_zero` 통과

### 전체 테스트 실행
```bash
python -m pytest tests/test_arithmetic.py -v
```

**예상 결과**:
- ✅ 덧셈 테스트 3개 통과
- ✅ 뺄셈 테스트 1개 통과
- ✅ 곱셈 테스트 2개 통과 (새로 통과)
- ✅ 나눗셈 테스트 3개 통과
- ⏸️ 몫 계산 테스트 1개 스킵 (구현 범위 외)

**총 9개 테스트 통과 예상** (기존 7개 + 곱셈 2개)

---

## 추가 작업 (선택사항)

### 실행 예제 업데이트
`if __name__ == "__main__":` 블록에 곱셈 예제 추가

```python
# 곱셈 예제
print("【곱셈 연산】")
print(f"  -5 * -3 = {arithmetic.multiply(-5, -3)}")
print(f"  0 * 10 = {arithmetic.multiply(0, 10)}")
print()
```

**위치**: 나눗셈 예제 다음, 예외 처리 예제 전

---

## 구현 원칙

### 최소 단위 구현 원칙
1. **테스트를 통과하는 최소한의 코드만 작성**
   - Python의 기본 곱셈 연산자(`*`) 사용
   - 추가 검증 로직 불필요
   - 음수와 0 처리는 Python이 자동으로 처리

2. **TDD GREEN 단계 원칙 준수**
   - RED 단계에서 작성된 테스트를 통과시키는 것이 목표
   - 리팩토링은 REFACTOR 단계에서 수행

3. **일관성 유지**
   - 기존 `add`, `subtract` 메서드와 동일한 패턴
   - 간단하고 명확한 구현

---

## 검증 체크리스트

- [ ] `multiply` 메서드 구현 확인
- [ ] `test_multiply_negative_numbers` 테스트 통과 확인
- [ ] `test_multiply_by_zero` 테스트 통과 확인
- [ ] 전체 테스트 실행 결과 확인 (9개 통과 예상)
- [ ] (선택) 실행 예제에 곱셈 추가 확인

---

## 주의사항

1. **구현 단순성**
   - 곱셈은 덧셈, 뺄셈과 마찬가지로 Python 기본 연산자로 충분
   - 특별한 예외 처리 불필요 (0 곱하기는 자연스럽게 0 반환)

2. **일관성**
   - 기존 메서드들과 동일한 스타일 유지
   - docstring 형식 통일

3. **구현 범위 준수**
   - 곱셈 기능만 구현
   - 몫 계산 기능(`divide_quotient`)은 이번 단계에서 구현하지 않음

---

**시나리오 작성일**: 2024-12-16  
**구현 예상 시간**: 약 2-3분  
**승인 대기 중**: ⏳

