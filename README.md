# Arithmetic Operations - 사칙연산 모듈

## 프로젝트 개요

사칙연산 기능의 정확도와 예외 처리를 검증하는 공통 모듈 프로젝트입니다.

## 테스트 정보

- **테스트 ID**: TC-CMM-001 (Common Module) / TC-AO-001 (Arithmetic Operations)
- **작성일**: 2020-09-01
- **버전**: v1.0
- **테스트 범위**: 공통 모듈
- **테스트 환경**: Python, PyCharm, Windows 10

## 테스트 케이스

### 기본 사칙연산 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|--------------|--------|--------|--------|------|
| 덧셈 | 1 + 10 | 11 | 중요 | 성공 |
| 덧셈 | 0 + 1 | 1 | 중요 | 성공 |
| 덧셈 | -1 + (-10) | -11 | 보통 | 성공 |
| 뺄셈 | 5 - 2 | 3 | 중요 | 성공 |
| 곱셈 | -5 * -3 | 15 | 보통 | 성공 |
| 곱셈 | 0 * 10 | 0 | 낮음 | 성공 |
| 나눗셈 (정수) | 5 / 2 | 2 | 중요 | 성공 |
| 나눗셈 (몫) | 5 ÷ 2 | 2.5 | 보통 | 성공 |
| 나눗셈 | -10 / 2 | -5 | 중요 | 성공 |

### 예외 처리 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|--------------|--------|--------|--------|------|
| 0으로 나누기 | 0 / 0 | ArithmeticException | 중요 | 성공 |

## 개발 방법론

이 프로젝트는 **TDD (Test-Driven Development)** 방식으로 진행됩니다:

1. **RED**: 실패하는 테스트 작성 -> ✅ 완료
2. **GREEN**: 테스트를 통과하는 최소한의 코드 작성 -> ⏳ 진행 예정
3. **REFACTOR**: 코드 개선 및 리팩토링 -> ⏳ 대기

## GREEN 단계 구현 목록

### 구현 우선순위

#### 중요도 높음 (필수 구현)

1. **모듈 구조 생성**
   - [ ] `src/arithmetic.py` 파일 생성
   - [ ] `Arithmetic` 클래스 정의

2. **덧셈 기능 (`add` 메서드)**
   - [ ] 양수 + 양수: `add(1, 10) = 11`
   - [ ] 0 포함: `add(0, 1) = 1`
   - [ ] 음수 + 음수: `add(-1, -10) = -11`

3. **뺄셈 기능 (`subtract` 메서드)**
   - [ ] 양수 - 양수: `subtract(5, 2) = 3`

4. **나눗셈 기능 (`divide` 메서드)**
   - [ ] 정수 나눗셈 (소수점 버림): `divide(5, 2) = 2`
   - [ ] 음수 나눗셈: `divide(-10, 2) = -5`
   - [ ] 0으로 나누기 예외 처리: `divide(0, 0)` → `ArithmeticError` 발생

#### 중요도 보통

5. **곱셈 기능 (`multiply` 메서드)**
   - [ ] 음수 × 음수: `multiply(-5, -3) = 15`
   - [ ] 0 포함: `multiply(0, 10) = 0`

6. **몫 계산 기능 (`divide_quotient` 메서드)**
   - [ ] 소수점 포함 몫: `divide_quotient(5, 2) = 2.5`

### 구현 체크리스트

- [ ] `src/arithmetic.py` 파일 생성
- [ ] `Arithmetic` 클래스 구현
- [ ] `add(a, b)` 메서드 구현
- [ ] `subtract(a, b)` 메서드 구현
- [ ] `multiply(a, b)` 메서드 구현
- [ ] `divide(a, b)` 메서드 구현 (정수 나눗셈, 소수점 버림)
- [ ] `divide_quotient(a, b)` 메서드 구현 (소수점 포함)
- [ ] 0으로 나누기 예외 처리 (`ArithmeticError` 발생)
- [ ] 모든 테스트 케이스 통과 확인
- [ ] 테스트 실행: `python -m pytest tests/test_arithmetic.py -v`

## 프로젝트 구조

```
Arithmetic/
├── README.md
├── requirements.txt
├── src/
│   └── arithmetic.py
└── tests/
    └── test_arithmetic.py
```

## 설치 및 실행

### 1. 가상환경 생성 (선택사항)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. 테스트 실행

```bash
pytest tests/
```

또는

```bash
python -m pytest tests/
```

## 성공/실패 기준

- **성공**: 모든 테스트 사례가 예상한 결과를 생성
- **실패**: 테스트 케이스가 예상한 결과를 생성하지 않음

## 전제 조건

- 프로그램은 오류 없이 성공적으로 컴파일되어야 합니다
- 모든 종속성을 올바르게 설치하고 구성해야 합니다

## 특별 절차

- 테스트 결과를 기록하고 이에 따라 테스트 사례 문서를 업데이트합니다
- 즉각적인 해결을 위해 모든 실패를 개발팀에 전달하세요

## 작성자

- 작성자: 홍길동
- 승인자: 박문수

---

## Refactory 시 해야할 일

### 리팩토링 단계별 방법

#### 1단계: 아키텍처 설계 (SOLID 준수)

##### 1.1 계층 구조 설계

```
┌─────────────────┐
│   GUI Layer     │  (PyQt UI)
│  (calculator_ui.py)
└────────┬────────┘
         │
┌────────▼────────┐
│  Controller     │  (계산기 상태 관리)
│ (calculator_controller.py)
└────────┬────────┘
         │
┌────────▼────────┐
│  Business Logic │  (기존 Arithmetic 유지)
│  (arithmetic.py)
└─────────────────┘
```

##### 1.2 디자인 패턴 적용

- **Strategy Pattern**: 연산자별 전략 객체로 분리
- **Command Pattern**: 버튼 클릭을 명령 객체로 처리
- **Observer Pattern**: UI 업데이트를 위한 상태 변경 알림

---

#### 2단계: 비즈니스 로직 리팩토링

##### 2.1 연산자 전략 패턴 구현

- **목적**: Open/Closed 원칙 준수, if-elif 체인 제거
- **방법**:
  - `OperationStrategy` 추상 클래스 생성
  - 각 연산자별 전략 클래스 구현 (`AddOperation`, `SubtractOperation`, `MultiplyOperation`, `DivideOperation`)
  - `OperationFactory`로 연산자 문자열 → 전략 객체 매핑

##### 2.2 Arithmetic 클래스 개선

- **현재**: 각 메서드가 독립적으로 존재
- **개선**: Strategy 패턴을 사용하도록 리팩토링 (선택사항, 기존 API 유지 가능)

---

#### 3단계: 컨트롤러 계층 구현

##### 3.1 CalculatorController 클래스 생성

- **책임**:
  - 계산기 상태 관리 (현재 값, 이전 값, 연산자, 입력 모드)
  - 연산 실행 및 결과 계산
  - 예외 처리 및 에러 상태 관리

- **상태 관리**:
  - `current_value`: 현재 입력/표시 값
  - `previous_value`: 이전 값
  - `operator`: 선택된 연산자
  - `waiting_for_operand`: 새 피연산자 입력 대기 여부

##### 3.2 계산기 로직 구현

- 숫자 입력 처리
- 연산자 선택 처리
- 등호(=) 처리
- 초기화(Clear) 처리
- 부호 변경(+/-) 처리
- 소수점 처리

---

#### 4단계: PyQt GUI 구현

##### 4.1 UI 컴포넌트 설계

- **CalculatorWindow** (QMainWindow 또는 QWidget)
  - 디스플레이: QLineEdit 또는 QLabel (읽기 전용)
  - 버튼 그리드: QGridLayout
  - 버튼 구성:
    - 숫자 버튼 (0-9)
    - 연산자 버튼 (+, -, ×, /)
    - 기능 버튼 (=, +/-, Clear, .)

##### 4.2 UI와 컨트롤러 연결

- **시그널-슬롯 연결**:
  - 숫자 버튼 클릭 → `controller.input_number()`
  - 연산자 버튼 클릭 → `controller.set_operator()`
  - 등호 버튼 클릭 → `controller.calculate()`
  - Clear 버튼 클릭 → `controller.clear()`

- **UI 업데이트**:
  - 컨트롤러 상태 변경 시 디스플레이 업데이트
  - Observer 패턴 또는 직접 호출 방식 선택

---

#### 5단계: 리소스 및 설정 분리

##### 5.1 문자열 외부화

- `resources/strings.py` 또는 `config/messages.py` 생성
- 한국어 메시지를 상수로 정의
- 국제화(i18n) 대비 구조

##### 5.2 스타일 분리

- `resources/styles.py` 또는 QSS 파일
- 버튼 색상, 크기, 폰트 등 스타일 정의
- 이미지에서 본 디자인 반영 (파란색 = 버튼 등)

---

#### 6단계: 예외 처리 및 에러 핸들링

##### 6.1 예외 처리 전략

- 비즈니스 로직 예외: `ArithmeticError` (0으로 나누기)
- UI 예외: 잘못된 입력, 오버플로우 등
- 사용자 친화적 메시지 표시

##### 6.2 에러 상태 관리

- 에러 발생 시 디스플레이에 메시지 표시
- 다음 입력 시 자동 초기화 또는 명시적 Clear 필요

---

#### 7단계: 테스트 가능성 개선

##### 7.1 의존성 주입

- Controller가 Arithmetic에 의존하되, 인터페이스로 추상화
- 테스트 시 Mock 객체 주입 가능

##### 7.2 단위 테스트 구조

- Controller 로직 테스트 (GUI 없이)
- Arithmetic 로직 테스트 (기존 유지)
- 통합 테스트 (선택사항)

