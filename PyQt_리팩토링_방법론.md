# PyQt GUI 리팩토링 방법론

## 코드 스멜 분석

### 발견된 문제점

1. **긴 if-elif 체인 (33-50줄)**: 연산자 처리 로직이 하드코딩되어 있음
2. **관심사 분리 부족**: UI 로직과 비즈니스 로직이 `main()` 함수에 혼재
3. **하드코딩된 문자열**: 한국어 메시지가 코드에 직접 포함되어 있음
4. **단일 책임 원칙 위반**: `calculator.py`가 입력/출력/라우팅을 모두 처리
5. **개방-폐쇄 원칙 위반**: 새로운 연산자 추가 시 기존 코드 수정 필요

---

## 리팩토링 단계별 방법

### 1단계: 아키텍처 설계 (SOLID 준수)

#### 1.1 계층 구조 설계

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

#### 1.2 디자인 패턴 적용

- **Strategy Pattern**: 연산자별 전략 객체로 분리
- **Command Pattern**: 버튼 클릭을 명령 객체로 처리
- **Observer Pattern**: UI 업데이트를 위한 상태 변경 알림

---

### 2단계: 비즈니스 로직 리팩토링

#### 2.1 연산자 전략 패턴 구현

- **목적**: Open/Closed 원칙 준수, if-elif 체인 제거
- **방법**:
  - `OperationStrategy` 추상 클래스 생성
  - 각 연산자별 전략 클래스 구현 (`AddOperation`, `SubtractOperation`, `MultiplyOperation`, `DivideOperation`)
  - `OperationFactory`로 연산자 문자열 → 전략 객체 매핑

#### 2.2 Arithmetic 클래스 개선

- **현재**: 각 메서드가 독립적으로 존재
- **개선**: Strategy 패턴을 사용하도록 리팩토링 (선택사항, 기존 API 유지 가능)

---

### 3단계: 컨트롤러 계층 구현

#### 3.1 CalculatorController 클래스 생성

- **책임**:
  - 계산기 상태 관리 (현재 값, 이전 값, 연산자, 입력 모드)
  - 연산 실행 및 결과 계산
  - 예외 처리 및 에러 상태 관리

- **상태 관리**:
  - `current_value`: 현재 입력/표시 값
  - `previous_value`: 이전 값
  - `operator`: 선택된 연산자
  - `waiting_for_operand`: 새 피연산자 입력 대기 여부

#### 3.2 계산기 로직 구현

- 숫자 입력 처리
- 연산자 선택 처리
- 등호(=) 처리
- 초기화(Clear) 처리
- 부호 변경(+/-) 처리
- 소수점 처리

---

### 4단계: PyQt GUI 구현

#### 4.1 UI 컴포넌트 설계

- **CalculatorWindow** (QMainWindow 또는 QWidget)
  - 디스플레이: QLineEdit 또는 QLabel (읽기 전용)
  - 버튼 그리드: QGridLayout
  - 버튼 구성:
    - 숫자 버튼 (0-9)
    - 연산자 버튼 (+, -, ×, /)
    - 기능 버튼 (=, +/-, Clear, .)

#### 4.2 UI와 컨트롤러 연결

- **시그널-슬롯 연결**:
  - 숫자 버튼 클릭 → `controller.input_number()`
  - 연산자 버튼 클릭 → `controller.set_operator()`
  - 등호 버튼 클릭 → `controller.calculate()`
  - Clear 버튼 클릭 → `controller.clear()`

- **UI 업데이트**:
  - 컨트롤러 상태 변경 시 디스플레이 업데이트
  - Observer 패턴 또는 직접 호출 방식 선택

---

### 5단계: 리소스 및 설정 분리

#### 5.1 문자열 외부화

- `resources/strings.py` 또는 `config/messages.py` 생성
- 한국어 메시지를 상수로 정의
- 국제화(i18n) 대비 구조

#### 5.2 스타일 분리

- `resources/styles.py` 또는 QSS 파일
- 버튼 색상, 크기, 폰트 등 스타일 정의
- 이미지에서 본 디자인 반영 (파란색 = 버튼 등)

---

### 6단계: 예외 처리 및 에러 핸들링

#### 6.1 예외 처리 전략

- 비즈니스 로직 예외: `ArithmeticError` (0으로 나누기)
- UI 예외: 잘못된 입력, 오버플로우 등
- 사용자 친화적 메시지 표시

#### 6.2 에러 상태 관리

- 에러 발생 시 디스플레이에 메시지 표시
- 다음 입력 시 자동 초기화 또는 명시적 Clear 필요

---

### 7단계: 테스트 가능성 개선

#### 7.1 의존성 주입

- Controller가 Arithmetic에 의존하되, 인터페이스로 추상화
- 테스트 시 Mock 객체 주입 가능

#### 7.2 단위 테스트 구조

- Controller 로직 테스트 (GUI 없이)
- Arithmetic 로직 테스트 (기존 유지)
- 통합 테스트 (선택사항)

---

## 파일 구조 제안

```
src/
├── arithmetic.py              # 기존 (비즈니스 로직)
├── calculator.py              # 기존 (콘솔 버전 유지 또는 제거)
├── calculator_controller.py   # 신규 (계산기 상태 관리)
├── calculator_ui.py           # 신규 (PyQt GUI)
├── operations/                # 신규 (Strategy 패턴)
│   ├── __init__.py
│   ├── base.py               # OperationStrategy 추상 클래스
│   ├── add.py
│   ├── subtract.py
│   ├── multiply.py
│   └── divide.py
└── resources/                 # 신규 (리소스)
    ├── strings.py            # 문자열 상수
    └── styles.py             # 스타일 정의
```

---

## SOLID 원칙 적용 체크리스트

### ✅ Single Responsibility (단일 책임 원칙)
- `CalculatorController`: 상태 관리만 담당
- `CalculatorUI`: UI 렌더링만 담당
- `Arithmetic`: 연산 로직만 담당

### ✅ Open/Closed (개방-폐쇄 원칙)
- Strategy 패턴으로 새로운 연산자 추가 시 기존 코드 수정 없음

### ✅ Liskov Substitution (리스코프 치환 원칙)
- 모든 Operation 전략이 동일한 인터페이스 구현

### ✅ Interface Segregation (인터페이스 분리 원칙)
- 필요한 메서드만 포함하는 인터페이스 설계

### ✅ Dependency Inversion (의존성 역전 원칙)
- Controller가 Arithmetic 인터페이스에 의존 (구현체가 아닌)

---

## 정적 분석 고려사항

1. **타입 힌팅**: 모든 함수에 타입 힌트 추가
2. **Docstring**: 모든 클래스/메서드에 문서화
3. **상수 정의**: 매직 넘버/문자열 제거
4. **순환 참조 방지**: 모듈 간 의존성 최소화
5. **에러 처리**: 모든 예외 상황 명시적 처리

---

## 구현 우선순위

### Phase 1: 핵심 구조 (필수)
1. CalculatorController 클래스 구현
2. 기본 PyQt UI 구조 생성
3. 숫자 입력 및 기본 연산 연결

### Phase 2: 기능 완성 (중요)
1. 모든 연산자 버튼 구현
2. Strategy 패턴 적용
3. 예외 처리 구현

### Phase 3: 개선 (선택)
1. 리소스 분리
2. 스타일 적용
3. 테스트 코드 작성

---

## 참고사항

- 기존 `Arithmetic` 클래스는 비즈니스 로직이므로 최대한 유지
- 콘솔 버전(`calculator.py`)은 유지하거나 별도 모듈로 분리 가능
- PyQt 의존성은 `requirements.txt`에 추가 필요: `PyQt5>=5.15.0` 또는 `PyQt6>=6.0.0`

