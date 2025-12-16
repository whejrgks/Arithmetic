# Arithmetic Operations 프로젝트 작업 리포트

## 프로젝트 정보

- **프로젝트명**: Arithmetic Operations - 사칙연산 모듈
- **테스트 ID**: TC-CMM-001 (Common Module) / TC-AO-001 (Arithmetic Operations)
- **작성일**: 2020-09-01
- **버전**: v1.0
- **테스트 범위**: 공통 모듈
- **테스트 환경**: Python, PyCharm, Windows 10
- **개발 방법론**: TDD (Test-Driven Development) - RED-GREEN-REFACTOR

## 작업 일지

### 2024-12-16

#### 1. 프로젝트 초기 설정

**작업 내용:**
- README.md 파일 생성
  - 프로젝트 개요 및 테스트 정보 작성
  - 테스트 케이스 문서화
  - 프로젝트 구조 정의
  - 설치 및 실행 방법 안내

- .gitignore 파일 생성
  - Python 프로젝트용 표준 .gitignore 설정
  - 가상환경, 캐시, IDE 파일 제외

**결과:**
- 프로젝트 문서화 완료
- Git 저장소 초기화 완료

#### 2. GitHub 저장소 연동

**작업 내용:**
- Git 저장소 초기화 (`git init`)
- 원격 저장소 추가 (`https://github.com/whejrgks/Arithmetic.git`)
- 초기 커밋 및 푸시 완료

**커밋 내역:**
- `Initial commit: Add README.md and .gitignore`

#### 3. TDD 브랜치 생성

**작업 내용:**
- `main` 브랜치에서 `red` 브랜치 생성
- RED 단계 작업을 위한 브랜치 분리

**브랜치 구조:**
```
main (초기 브랜치)
  └── red (RED 단계 작업 브랜치)
```

#### 4. 프로젝트 구조 생성

**작업 내용:**
- `src/` 디렉토리 생성
  - `__init__.py` 파일 추가
- `tests/` 디렉토리 생성
  - `__init__.py` 파일 추가
- `requirements.txt` 파일 생성
  - pytest>=7.0.0 의존성 추가

**프로젝트 구조:**
```
Arithmetic/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── __init__.py
└── tests/
    └── __init__.py
```

#### 5. RED 단계: 실패하는 테스트 작성

**작업 내용:**
- `tests/test_arithmetic.py` 파일 작성
- 테스트 케이스 기반 테스트 함수 구현

**작성된 테스트 케이스:**

##### 덧셈 테스트 (3개)
1. `test_add_1_plus_10`: 1 + 10 = 11
2. `test_add_0_plus_1`: 0 + 1 = 1
3. `test_add_negative_numbers`: -1 + (-10) = -11

##### 뺄셈 테스트 (1개)
4. `test_subtract_5_minus_2`: 5 - 2 = 3

##### 곱셈 테스트 (2개)
5. `test_multiply_negative_numbers`: -5 * -3 = 15
6. `test_multiply_by_zero`: 0 * 10 = 0

##### 나눗셈 테스트 (3개)
7. `test_divide_integer_5_by_2`: 5 / 2 = 2 (정수 나눗셈)
8. `test_divide_quotient_5_by_2`: 5 ÷ 2 = 2.5 (몫 계산)
9. `test_divide_negative_10_by_2`: -10 / 2 = -5

##### 예외 처리 테스트 (1개)
10. `test_divide_by_zero_exception`: 0 / 0 → ArithmeticError 예외 발생

**테스트 코드 구조:**
```python
class TestArithmetic:
    def setup_method(self):
        self.arithmetic = Arithmetic()
    
    # 각 테스트 메서드 구현
```

**테스트 실행 결과:**
- 모든 테스트 실패 (예상대로)
- 원인: `ModuleNotFoundError: No module named 'src.arithmetic'`
- RED 단계 목적 달성: 구현 코드가 없어 테스트가 실패함

#### 6. Git 커밋 및 푸시

**커밋 내역:**
1. `RED: Add failing test for test_add_1_plus_10 and project structure`
   - 프로젝트 구조 생성
   - 테스트 파일 작성
   - requirements.txt 추가

2. `Merge: Resolve conflicts and update README.md`
   - 원격 저장소와 병합
   - README.md 업데이트

**브랜치 상태:**
- `red` 브랜치에서 작업 진행
- 모든 변경사항 원격 저장소에 푸시 완료

## 테스트 케이스 상세

### 기본 사칙연산 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|--------------|--------|--------|--------|------|
| 덧셈 | 1 + 10 | 11 | 중요 | RED (실패) |
| 덧셈 | 0 + 1 | 1 | 중요 | RED (실패) |
| 덧셈 | -1 + (-10) | -11 | 보통 | RED (실패) |
| 뺄셈 | 5 - 2 | 3 | 중요 | RED (실패) |
| 곱셈 | -5 * -3 | 15 | 보통 | RED (실패) |
| 곱셈 | 0 * 10 | 0 | 낮음 | RED (실패) |
| 나눗셈 (정수) | 5 / 2 | 2 | 중요 | RED (실패) |
| 나눗셈 (몫) | 5 ÷ 2 | 2.5 | 보통 | RED (실패) |
| 나눗셈 | -10 / 2 | -5 | 중요 | RED (실패) |

### 예외 처리 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|--------------|--------|--------|--------|------|
| 0으로 나누기 | 0 / 0 | ArithmeticError | 중요 | RED (실패) |

## 현재 프로젝트 상태

### 완료된 작업
- ✅ 프로젝트 초기 설정
- ✅ GitHub 저장소 연동
- ✅ TDD 브랜치 구조 생성
- ✅ 프로젝트 구조 생성
- ✅ RED 단계: 실패하는 테스트 작성
- ✅ Git 커밋 및 푸시

### 다음 단계 (GREEN 단계)
- ⏳ `src/arithmetic.py` 파일 생성
- ⏳ `Arithmetic` 클래스 구현
- ⏳ 각 메서드 구현 (add, subtract, multiply, divide, divide_quotient)
- ⏳ 예외 처리 구현 (0으로 나누기)
- ⏳ 모든 테스트 통과 확인

## 파일 구조

```
Arithmetic/
├── README.md                    # 프로젝트 문서
├── requirements.txt             # Python 의존성
├── .gitignore                   # Git 제외 파일
├── Report/
│   └── Project_Report.md        # 작업 리포트 (본 문서)
├── src/
│   └── __init__.py             # 소스 패키지 초기화
└── tests/
    ├── __init__.py             # 테스트 패키지 초기화
    └── test_arithmetic.py      # 테스트 코드
```

## Git 브랜치 및 커밋 히스토리

```
*   e41311a (HEAD -> red, origin/red) Merge: Resolve conflicts and update README.md
|\
| * 34d1c3e Update README.md
* | 2d31f59 RED: Add failing test for test_add_1_plus_10 and project structure  
|/
* 1d71201 (origin/main, main) Initial commit: Add README.md and .gitignore
```

## 테스트 실행 방법

### 환경 설정
```bash
# 가상환경 생성 (선택사항)
python -m venv venv
venv\Scripts\activate  # Windows

# 의존성 설치
pip install -r requirements.txt
```

### 테스트 실행
```bash
# 전체 테스트 실행
python -m pytest tests/ -v

# 특정 테스트 실행
python -m pytest tests/test_arithmetic.py::TestArithmetic::test_add_1_plus_10 -v
```

### 현재 테스트 결과
- **상태**: 모든 테스트 실패 (예상됨)
- **원인**: `src.arithmetic` 모듈이 존재하지 않음
- **목적**: RED 단계 완료 - 구현 코드 작성 준비 완료

## 참고사항

### TDD 사이클
1. **RED**: 실패하는 테스트 작성 ✅ (완료)
2. **GREEN**: 테스트를 통과하는 최소한의 코드 작성 ⏳ (다음 단계)
3. **REFACTOR**: 코드 개선 및 리팩토링 ⏳ (예정)

### 개발 원칙
- 테스트 우선 작성
- 최소한의 코드로 테스트 통과
- 지속적인 리팩토링
- 작은 단위로 점진적 개발

## 작성자 정보

- **작성자**: 홍길동
- **승인자**: 박문수
- **작성일**: 2024-12-16
- **버전**: v1.0

---

**다음 업데이트**: GREEN 단계 완료 후 업데이트 예정

