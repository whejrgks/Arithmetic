# GREEN 단계 최소 단위 구현 시나리오

## 구현 범위
**중요도 높음 (필수 구현)** 항목만 구현
- 모듈 구조 생성
- 덧셈 기능 (`add` 메서드)
- 뺄셈 기능 (`subtract` 메서드)
- 나눗셈 기능 (`divide` 메서드)

## 구현 단계

### 1단계: 모듈 구조 생성

#### 1.1 파일 생성
- **파일 경로**: `src/arithmetic.py`
- **작업 내용**: 
  - 빈 파일 생성 또는 기본 클래스 구조만 생성

#### 1.2 Arithmetic 클래스 정의
```python
class Arithmetic:
    """사칙연산 클래스"""
    pass
```

**예상 결과**: 
- `ModuleNotFoundError` 해결
- 클래스 인스턴스 생성 가능 (`Arithmetic()`)

---

### 2단계: 덧셈 기능 구현 (`add` 메서드)

#### 2.1 테스트 케이스 분석
- `test_add_1_plus_10`: `add(1, 10) == 11`
- `test_add_0_plus_1`: `add(0, 1) == 1`
- `test_add_negative_numbers`: `add(-1, -10) == -11`

#### 2.2 최소 구현 코드
```python
def add(self, a, b):
    """덧셈 연산"""
    return a + b
```

**예상 결과**: 
- 3개 덧셈 테스트 모두 통과
- 양수, 0, 음수 모두 처리 가능

---

### 3단계: 뺄셈 기능 구현 (`subtract` 메서드)

#### 3.1 테스트 케이스 분석
- `test_subtract_5_minus_2`: `subtract(5, 2) == 3`

#### 3.2 최소 구현 코드
```python
def subtract(self, a, b):
    """뺄셈 연산"""
    return a - b
```

**예상 결과**: 
- 1개 뺄셈 테스트 통과

---

### 4단계: 나눗셈 기능 구현 (`divide` 메서드)

#### 4.1 테스트 케이스 분석
- `test_divide_integer_5_by_2`: `divide(5, 2) == 2` (정수 나눗셈, 소수점 버림)
- `test_divide_negative_10_by_2`: `divide(-10, 2) == -5` (음수 나눗셈)
- `test_divide_by_zero_exception`: `divide(0, 0)` → `ArithmeticError` 발생

#### 4.2 최소 구현 코드
```python
def divide(self, a, b):
    """나눗셈 연산 (정수 나눗셈, 소수점 버림)"""
    if b == 0:
        raise ArithmeticError("Division by zero")
    return a // b  # 정수 나눗셈 (소수점 버림)
```

**예상 결과**: 
- 정수 나눗셈 테스트 통과 (5 // 2 = 2)
- 음수 나눗셈 테스트 통과 (-10 // 2 = -5)
- 0으로 나누기 예외 처리 테스트 통과

---

## 최종 구현 코드 구조

```python
# src/arithmetic.py

class Arithmetic:
    """사칙연산 클래스"""
    
    def add(self, a, b):
        """덧셈 연산"""
        return a + b
    
    def subtract(self, a, b):
        """뺄셈 연산"""
        return a - b
    
    def divide(self, a, b):
        """나눗셈 연산 (정수 나눗셈, 소수점 버림)"""
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b
```

---

## 테스트 실행 계획

### 단계별 테스트 실행
1. **1단계 후**: `python -m pytest tests/test_arithmetic.py::TestArithmetic::test_add_1_plus_10 -v`
   - 예상: `AttributeError: 'Arithmetic' object has no attribute 'add'`

2. **2단계 후**: `python -m pytest tests/test_arithmetic.py -k "add" -v`
   - 예상: 3개 덧셈 테스트 모두 통과

3. **3단계 후**: `python -m pytest tests/test_arithmetic.py -k "subtract" -v`
   - 예상: 1개 뺄셈 테스트 통과

4. **4단계 후**: `python -m pytest tests/test_arithmetic.py -k "divide" -v`
   - 예상: 3개 나눗셈 테스트 모두 통과 (예외 처리 포함)

### 최종 통합 테스트
```bash
python -m pytest tests/test_arithmetic.py -v
```

**예상 결과**:
- ✅ 덧셈 테스트 3개 통과
- ✅ 뺄셈 테스트 1개 통과
- ✅ 나눗셈 테스트 3개 통과 (예외 처리 포함)
- ⏸️ 곱셈 테스트 2개 스킵 (구현 범위 외)
- ⏸️ 몫 계산 테스트 1개 스킵 (구현 범위 외)

**총 7개 테스트 통과 예상**

---

## 구현 원칙

### 최소 단위 구현 원칙
1. **테스트를 통과하는 최소한의 코드만 작성**
   - 불필요한 검증 로직 추가하지 않음
   - 엣지 케이스 처리 최소화
   - 문서화는 최소한만 (docstring만)

2. **TDD GREEN 단계 원칙 준수**
   - RED 단계에서 작성된 테스트를 통과시키는 것이 목표
   - 리팩토링은 REFACTOR 단계에서 수행

3. **구현 범위 엄수**
   - 중요도 높음 항목만 구현
   - 곱셈(`multiply`)과 몫 계산(`divide_quotient`)은 제외

---

## 검증 체크리스트

- [ ] `src/arithmetic.py` 파일 생성 확인
- [ ] `Arithmetic` 클래스 정의 확인
- [ ] `add` 메서드 구현 및 테스트 통과 확인
- [ ] `subtract` 메서드 구현 및 테스트 통과 확인
- [ ] `divide` 메서드 구현 및 테스트 통과 확인
- [ ] 0으로 나누기 예외 처리 확인
- [ ] 전체 테스트 실행 결과 확인 (7개 통과 예상)

---

## 주의사항

1. **정수 나눗셈 연산자 사용**
   - Python의 `//` 연산자 사용 (소수점 버림)
   - `/` 연산자는 부동소수점 결과 반환하므로 사용하지 않음

2. **예외 처리**
   - `ArithmeticError` 사용 (테스트에서 기대하는 예외 타입)
   - 메시지는 선택사항이지만 명확성을 위해 추가 권장

3. **구현 범위 준수**
   - 곱셈과 몫 계산 기능은 이번 단계에서 구현하지 않음
   - 해당 테스트는 실패할 것으로 예상되지만 정상임

---

**시나리오 작성일**: 2024-12-16  
**구현 예상 시간**: 약 10-15분  
**승인 대기 중**: ⏳

