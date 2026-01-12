# 4단계: PyQt GUI 구현 진행 내용

## 개요

4단계에서는 PyQt를 사용하여 계산기 GUI를 구현하고, 컨트롤러와 UI를 연결하여 완전한 계산기 애플리케이션을 완성했습니다.

---

## 4.1 UI 컴포넌트 설계

### CalculatorWindow 클래스

**기본 구조**:
- `QMainWindow`를 상속받아 메인 윈도우 구현
- 중앙 위젯(`QWidget`)에 모든 컴포넌트 배치
- 수직 레이아웃(`QVBoxLayout`)으로 디스플레이와 버튼 그리드 구성

### 디스플레이 컴포넌트

**구현**: `QLineEdit` (읽기 전용)

**특징**:
- 오른쪽 정렬 (`Qt.AlignRight`)
- 큰 폰트 (Arial, 24pt, Bold)
- 어두운 배경 (#1e1e1e)
- 테두리 및 패딩 적용

```python
self._display = QLineEdit()
self._display.setReadOnly(True)
self._display.setAlignment(Qt.AlignRight)
self._display.setFont(QFont("Arial", 24, QFont.Bold))
self._display.setStyleSheet(
    "background-color: #1e1e1e; color: white; "
    "border: 2px solid #4a4a4a; border-radius: 4px; "
    "padding: 10px;"
)
```

### 버튼 그리드

**구현**: `QGridLayout`

**버튼 구성** (이미지 레이아웃 반영):

```
Row 1: [7] [8] [9] [×]
Row 2: [4] [5] [6] [−]
Row 3: [1] [2] [3] [+]
Row 4: [+/−] [0] [.] [=]
Row 5: [Clear] [Clear] [Clear] [/]
```

**버튼 종류**:
1. **숫자 버튼 (0-9)**: 어두운 회색 배경 (#2d2d2d)
2. **연산자 버튼 (+, -, ×, /)**: 중간 회색 배경 (#4a4a4a)
3. **기능 버튼 (+/-, .)**: 중간 회색 배경 (#4a4a4a)
4. **등호 버튼 (=)**: 파란색 배경 (#0078d4) - 이미지에서 강조
5. **Clear 버튼**: 빨간색 배경 (#d13438)

**스타일 특징**:
- 모든 버튼에 둥근 모서리 (`border-radius: 4px`)
- 호버 효과 (커서 변경)
- 등호 버튼은 굵은 글씨로 강조

---

## 4.2 UI와 컨트롤러 연결

### 시그널-슬롯 연결

모든 버튼 클릭 이벤트를 컨트롤러 메서드에 연결했습니다:

#### 1. 숫자 버튼 클릭 → `controller.input_number()`

```python
if text.isdigit():
    button.clicked.connect(lambda checked, d=text: self._on_number_clicked(d))

def _on_number_clicked(self, digit: str) -> None:
    """숫자 버튼 클릭 핸들러"""
    self._controller.input_number(digit)
```

**동작**:
- 0-9 버튼 클릭 시 해당 숫자가 컨트롤러로 전달
- 컨트롤러가 상태를 업데이트하고 콜백을 통해 디스플레이 갱신

#### 2. 연산자 버튼 클릭 → `controller.set_operator()`

```python
elif text in ("+", "−", "×"):
    button.clicked.connect(lambda checked, op=text: self._on_operator_clicked(op))

def _on_operator_clicked(self, operator: str) -> None:
    """연산자 버튼 클릭 핸들러"""
    # − 기호를 -로 변환
    if operator == "−":
        operator = "-"
    self._controller.set_operator(operator)
```

**동작**:
- +, −, ×, / 버튼 클릭 시 연산자 설정
- UI의 "−" 기호를 내부적으로 "-"로 변환

#### 3. 등호 버튼 클릭 → `controller.calculate()`

```python
elif text == "=":
    button.clicked.connect(self._on_equals_clicked)

def _on_equals_clicked(self) -> None:
    """등호 버튼 클릭 핸들러"""
    self._controller.calculate()
```

**동작**:
- = 버튼 클릭 시 현재 연산 실행
- 결과가 디스플레이에 표시됨

#### 4. Clear 버튼 클릭 → `controller.clear()`

```python
clear_button.clicked.connect(self._on_clear_clicked)

def _on_clear_clicked(self) -> None:
    """Clear 버튼 클릭 핸들러"""
    self._controller.clear()
```

**동작**:
- Clear 버튼 클릭 시 모든 상태 초기화
- 디스플레이가 "0"으로 리셋

#### 5. 부호 변경 버튼 클릭 → `controller.toggle_sign()`

```python
elif text == "+/−":
    button.clicked.connect(self._on_toggle_sign_clicked)

def _on_toggle_sign_clicked(self) -> None:
    """부호 변경 버튼 클릭 핸들러"""
    self._controller.toggle_sign()
```

**동작**:
- +/- 버튼 클릭 시 현재 값의 부호 변경

#### 6. 소수점 버튼 클릭 → `controller.input_decimal()`

```python
elif text == ".":
    button.clicked.connect(self._on_decimal_clicked)

def _on_decimal_clicked(self) -> None:
    """소수점 버튼 클릭 핸들러"""
    self._controller.input_decimal()
```

**동작**:
- . 버튼 클릭 시 소수점 입력

### UI 업데이트 메커니즘

**Observer 패턴 방식**: 콜백 함수를 통한 디스플레이 업데이트

```python
def __init__(self):
    self._controller = CalculatorController()
    self._controller.set_display_callback(self._update_display)
    self._init_ui()

def _update_display(self, value: str) -> None:
    """디스플레이를 업데이트합니다."""
    self._display.setText(value)
```

**동작 흐름**:
1. 사용자가 버튼 클릭
2. UI 핸들러가 컨트롤러 메서드 호출
3. 컨트롤러가 상태 업데이트
4. 컨트롤러가 콜백 함수 호출
5. UI가 디스플레이 업데이트

---

## 추가 개선 사항

### 1. 키보드 단축키 지원

**구현**: `_setup_shortcuts()` 메서드

**지원하는 단축키**:
- **숫자 키 (0-9)**: 해당 숫자 입력
- **연산자 키**: +, -, *, / (키보드 입력)
- **등호 키**: Enter, Return, = (계산 실행)
- **Clear 키**: Escape, Delete (초기화)
- **소수점 키**: . (점), , (콤마도 소수점으로 처리)

```python
def _setup_shortcuts(self) -> None:
    """키보드 단축키 설정"""
    from PyQt5.QtWidgets import QShortcut
    
    # 숫자 키 (0-9)
    for i in range(10):
        shortcut = QShortcut(QKeySequence(str(i)), self)
        shortcut.activated.connect(lambda digit=str(i): self._on_number_clicked(digit))
    
    # 연산자 및 기능 키...
```

**사용성 향상**:
- 마우스 없이도 키보드로 모든 기능 사용 가능
- 일반 계산기 사용 패턴과 일치

### 2. 디자인 개선

**색상 스키마** (이미지 디자인 반영):
- **배경**: 어두운 회색 (#1e1e1e)
- **숫자 버튼**: 더 어두운 회색 (#2d2d2d)
- **연산자/기능 버튼**: 중간 회색 (#4a4a4a)
- **등호 버튼**: 파란색 (#0078d4) - 강조
- **Clear 버튼**: 빨간색 (#d13438) - 경고

**스타일 특징**:
- 모든 버튼에 둥근 모서리
- 호버 시 커서 변경 (PointingHandCursor)
- 등호 버튼은 굵은 글씨로 강조
- 디스플레이에 테두리 및 패딩 적용

### 3. 윈도우 크기 및 레이아웃

**윈도우 크기**: 320 × 450 픽셀 (고정)
- 버튼 크기와 레이아웃에 최적화
- 모바일 계산기와 유사한 비율

**레이아웃 구조**:
```
┌─────────────────────┐
│     디스플레이      │
├─────────────────────┤
│ [7] [8] [9] [×]    │
│ [4] [5] [6] [−]    │
│ [1] [2] [3] [+]    │
│ [+/−] [0] [.] [=]  │
│ [Clear] [Clear] [/]│
└─────────────────────┘
```

---

## 파일 구조

### 생성/수정된 파일

1. **src/calculator_ui.py** - PyQt GUI 메인 파일
   - CalculatorWindow 클래스
   - UI 초기화 및 이벤트 핸들러
   - 키보드 단축키 지원

### 의존성

- **PyQt5**: GUI 프레임워크
  - `QApplication`: 애플리케이션 메인 루프
  - `QMainWindow`: 메인 윈도우
  - `QWidget`: 중앙 위젯
  - `QVBoxLayout`, `QGridLayout`: 레이아웃
  - `QPushButton`: 버튼
  - `QLineEdit`: 디스플레이
  - `QShortcut`: 키보드 단축키

---

## 실행 방법

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

`requirements.txt`에 `PyQt5>=5.15.0` 포함됨

### 2. GUI 실행

```bash
python src/calculator_ui.py
```

또는

```bash
python -m src.calculator_ui
```

### 3. 사용 방법

**마우스 사용**:
- 버튼 클릭으로 모든 기능 사용

**키보드 사용**:
- 숫자 키 (0-9): 숫자 입력
- +, -, *, /: 연산자 선택
- Enter, Return, =: 계산 실행
- Escape, Delete: Clear
- . 또는 ,: 소수점 입력

---

## 테스트 시나리오

### 기본 연산 테스트

1. **덧셈**: 5 + 3 = 8
   - 5 클릭 → + 클릭 → 3 클릭 → = 클릭
   - 또는: 5 → + → 3 → Enter

2. **뺄셈**: 10 - 3 = 7
   - 1 → 0 → − → 3 → =

3. **곱셈**: 5 × 3 = 15
   - 5 → × → 3 → =

4. **나눗셈**: 10 / 2 = 5
   - 1 → 0 → / → 2 → =

### 소수점 연산 테스트

1. **소수점 입력**: 5.2
   - 5 → . → 2

2. **소수점 결과**: 5 / 2 = 2.5
   - 5 → / → 2 → =

### 에러 처리 테스트

1. **0으로 나누기**: 5 / 0 = Error
   - 5 → / → 0 → =
   - 디스플레이에 "Error" 표시
   - Clear 버튼으로 복구

### 복합 시나리오 테스트

1. **연속 계산**: 10 + 5 - 3 × 2 / 4 = 6
   - 각 연산 후 결과 확인

2. **부호 변경**: 5 → +/- → -5
   - +/- 버튼으로 부호 변경

---

## SOLID 원칙 준수 확인

### ✅ Single Responsibility 원칙
- `CalculatorWindow`: UI 렌더링 및 이벤트 처리만 담당
- `CalculatorController`: 상태 관리 및 연산 실행만 담당
- 관심사 분리 완료

### ✅ Dependency Inversion 원칙
- UI가 컨트롤러 인터페이스에 의존
- 콜백 함수를 통한 느슨한 결합
- 테스트 시 Mock 컨트롤러 주입 가능

---

## 개선 효과

### 사용성
- ✅ 직관적인 버튼 레이아웃
- ✅ 키보드 단축키 지원
- ✅ 명확한 시각적 피드백
- ✅ 에러 상태 명확한 표시

### 코드 품질
- ✅ 관심사 분리 (UI / Controller / Business Logic)
- ✅ 재사용 가능한 구조
- ✅ 확장 가능한 디자인
- ✅ 타입 힌팅 및 문서화

### 유지보수성
- ✅ 명확한 메서드 분리
- ✅ 이벤트 핸들러 독립적 관리
- ✅ 스타일 중앙 관리
- ✅ 쉬운 테스트 가능

---

## 다음 단계

4단계가 완료되었으므로 다음 단계로 진행할 수 있습니다:

- **5단계**: 리소스 및 설정 분리
  - 문자열 외부화
  - 스타일 QSS 파일 분리
  - 국제화(i18n) 대비

- **6단계**: 예외 처리 및 에러 핸들링 (일부 완료)
  - 추가 에러 메시지 개선
  - 사용자 친화적 메시지

- **7단계**: 테스트 가능성 개선 (완료)
  - Controller 테스트 완료
  - UI 테스트 (선택사항)

---

## 요약

✅ **4.1 UI 컴포넌트 설계**: 완료
- CalculatorWindow 클래스 구현
- 디스플레이 (QLineEdit) 구현
- 버튼 그리드 (QGridLayout) 구현
- 모든 버튼 구성 완료

✅ **4.2 UI와 컨트롤러 연결**: 완료
- 시그널-슬롯 연결 완료
  - 숫자 버튼 → `input_number()` ✅
  - 연산자 버튼 → `set_operator()` ✅
  - 등호 버튼 → `calculate()` ✅
  - Clear 버튼 → `clear()` ✅
  - 부호 변경 버튼 → `toggle_sign()` ✅
  - 소수점 버튼 → `input_decimal()` ✅
- Observer 패턴을 통한 UI 업데이트 ✅

✅ **추가 개선**: 완료
- 키보드 단축키 지원 ✅
- 디자인 개선 (이미지 스타일 반영) ✅
- 사용성 향상 ✅

✅ **완전한 계산기 애플리케이션**: 완성
- 모든 기능 정상 작동
- 사용자 친화적 인터페이스
- 확장 가능한 구조

