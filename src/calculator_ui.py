"""
PyQt 계산기 GUI 애플리케이션
"""
import sys
import os
from typing import Optional

# 직접 실행 시 프로젝트 루트를 sys.path에 추가
# (패키지로 설치된 경우에는 불필요하지만, 직접 실행 시 필요)
# 파일이 직접 실행될 때만 sys.path 조정
if not __package__ or __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout,
    QPushButton, QLineEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QKeySequence

from src.calculator_controller import CalculatorController
from src.resources.styles import CalculatorStyles


class CalculatorWindow(QMainWindow):
    """계산기 메인 윈도우"""
    
    def __init__(self):
        """계산기 윈도우 초기화"""
        super().__init__()
        self._controller = CalculatorController()
        self._controller.set_display_callback(self._update_display)
        self._init_ui()
        self._setup_shortcuts()  # 키보드 단축키 설정
    
    def _init_ui(self) -> None:
        """
        UI 초기화
        
        UI 컴포넌트:
        - 디스플레이: QLineEdit (읽기 전용, 오른쪽 정렬)
        - 버튼 그리드: QGridLayout
          - 숫자 버튼 (0-9)
          - 연산자 버튼 (+, -, ×, /)
          - 기능 버튼 (=, +/-, Clear, .)
        """
        self._setup_window()
        main_layout = self._setup_main_layout()
        self._create_display(main_layout)
        self._create_button_grid(main_layout)
    
    def _setup_window(self) -> None:
        """윈도우 기본 설정"""
        self.setWindowTitle(CalculatorStyles.WINDOW_TITLE)
        self.setFixedSize(CalculatorStyles.WINDOW_WIDTH, CalculatorStyles.WINDOW_HEIGHT)
        self.setStyleSheet(CalculatorStyles.get_window_style())
    
    def _setup_main_layout(self) -> QVBoxLayout:
        """
        메인 레이아웃을 설정합니다.
        
        Returns:
            메인 레이아웃 (QVBoxLayout)
        """
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        return main_layout
    
    def _create_display(self, main_layout: QVBoxLayout) -> None:
        """
        디스플레이를 생성하고 레이아웃에 추가합니다.
        
        Args:
            main_layout: 메인 레이아웃
        """
        self._display = QLineEdit()
        self._display.setReadOnly(True)
        self._display.setAlignment(Qt.AlignRight)
        self._display.setFont(QFont(CalculatorStyles.FONT_FAMILY, CalculatorStyles.FONT_SIZE_DISPLAY, QFont.Bold))
        self._display.setText(CalculatorStyles.DISPLAY_INITIAL_VALUE)
        self._display.setStyleSheet(CalculatorStyles.get_display_style())
        main_layout.addWidget(self._display)
    
    def _create_button_grid(self, main_layout: QVBoxLayout) -> None:
        """
        버튼 그리드를 생성하고 레이아웃에 추가합니다.
        
        Args:
            main_layout: 메인 레이아웃
        """
        button_layout = QGridLayout()
        main_layout.addLayout(button_layout)
        
        # 버튼 정의 (이미지 레이아웃 반영)
        # Row 1: 7, 8, 9, ×
        # Row 2: 4, 5, 6, −
        # Row 3: 1, 2, 3, +
        # Row 4: +/−, 0, ., =
        buttons = [
            # 행, 열, 텍스트, 스타일
            (0, 0, "7", "number"),
            (0, 1, "8", "number"),
            (0, 2, "9", "number"),
            (0, 3, "×", "operator"),
            (1, 0, "4", "number"),
            (1, 1, "5", "number"),
            (1, 2, "6", "number"),
            (1, 3, "−", "operator"),
            (2, 0, "1", "number"),
            (2, 1, "2", "number"),
            (2, 2, "3", "number"),
            (2, 3, "+", "operator"),
            (3, 0, "+/−", "function"),
            (3, 1, "0", "number"),
            (3, 2, ".", "function"),
            (3, 3, "=", "equals"),
        ]
        
        # 버튼 생성 및 연결
        for row, col, text, style in buttons:
            button = self._create_button(text, style)
            self._connect_button_signal(button, text)
            button_layout.addWidget(button, row, col)
        
        # 나눗셈 버튼 추가 (별도 행 또는 기존 레이아웃에 추가)
        # 이미지에는 없지만 기능상 필요하므로 추가
        divide_button = self._create_button("/", "operator")
        self._connect_button_signal(divide_button, "/")
        button_layout.addWidget(
            divide_button, 
            CalculatorStyles.BUTTON_GRID_ROW_DIVIDE, 
            CalculatorStyles.BUTTON_GRID_COL_DIVIDE
        )
        
        # Clear 버튼 (별도 추가)
        clear_button = self._create_button("Clear", "clear")
        self._connect_button_signal(clear_button, "Clear")
        button_layout.addWidget(
            clear_button, 
            CalculatorStyles.BUTTON_GRID_ROW_CLEAR, 
            CalculatorStyles.BUTTON_GRID_COL_CLEAR_START, 
            1, 
            CalculatorStyles.BUTTON_GRID_CLEAR_SPAN
        )
    
    def _update_display(self, value: str) -> None:
        """
        디스플레이를 업데이트합니다.
        
        Args:
            value: 표시할 값
        """
        self._display.setText(value)
    
    def _on_number_clicked(self, digit: str) -> None:
        """
        숫자 버튼 클릭 핸들러
        
        Args:
            digit: 클릭된 숫자
        """
        self._controller.input_number(digit)
    
    def _on_operator_clicked(self, operator: str) -> None:
        """
        연산자 버튼 클릭 핸들러
        
        Args:
            operator: 클릭된 연산자 (UI 표시용 기호 포함 가능)
        """
        # 기호 변환은 컨트롤러에서 처리
        self._controller.set_operator(operator)
    
    def _on_equals_clicked(self) -> None:
        """등호 버튼 클릭 핸들러"""
        self._controller.calculate()
    
    def _on_clear_clicked(self) -> None:
        """Clear 버튼 클릭 핸들러"""
        self._controller.clear()
    
    def _on_toggle_sign_clicked(self) -> None:
        """부호 변경 버튼 클릭 핸들러"""
        self._controller.toggle_sign()
    
    def _on_decimal_clicked(self) -> None:
        """소수점 버튼 클릭 핸들러"""
        self._controller.input_decimal()
    
    def _create_button(self, text: str, style_type: str) -> QPushButton:
        """
        버튼을 생성하고 스타일을 적용합니다.
        
        Args:
            text: 버튼 텍스트
            style_type: 버튼 스타일 타입 ("number", "operator", "function", "equals", "clear")
            
        Returns:
            생성된 QPushButton 인스턴스
        """
        button = QPushButton(text)
        button.setFont(QFont(CalculatorStyles.FONT_FAMILY, CalculatorStyles.FONT_SIZE_BUTTON))
        button.setMinimumHeight(CalculatorStyles.BUTTON_MIN_HEIGHT)
        button.setStyleSheet(CalculatorStyles.get_button_style(style_type))
        button.setCursor(Qt.PointingHandCursor)
        return button
    
    def _connect_button_signal(self, button: QPushButton, text: str) -> None:
        """
        버튼의 시그널을 적절한 슬롯에 연결합니다.
        
        Args:
            button: 연결할 버튼
            text: 버튼 텍스트 (기능 판별용)
        """
        # 버튼 타입별 핸들러 매핑 (딕셔너리 기반)
        # 숫자 버튼은 isdigit()으로 체크하므로 별도 처리
        if text.isdigit():
            button.clicked.connect(lambda checked, d=text: self._on_number_clicked(d))
            return
        
        # 특정 텍스트에 대한 핸들러 매핑
        button_handlers = {
            # 연산자 버튼
            "+": lambda: self._on_operator_clicked("+"),
            "−": lambda: self._on_operator_clicked("−"),
            "×": lambda: self._on_operator_clicked("×"),
            "/": lambda: self._on_operator_clicked("/"),
            # 기능 버튼
            "=": self._on_equals_clicked,
            "+/−": self._on_toggle_sign_clicked,
            ".": self._on_decimal_clicked,
            "Clear": self._on_clear_clicked,
        }
        
        # 딕셔너리에서 핸들러 찾아서 연결
        handler = button_handlers.get(text)
        if handler:
            button.clicked.connect(handler)
    
    def _setup_shortcuts(self) -> None:
        """키보드 단축키 설정"""
        from PyQt5.QtWidgets import QShortcut
        
        # 숫자 키 (0-9)
        for i in range(10):
            shortcut = QShortcut(QKeySequence(str(i)), self)
            shortcut.activated.connect(lambda digit=str(i): self._on_number_clicked(digit))
        
        # 연산자 키
        QShortcut(QKeySequence("+"), self).activated.connect(lambda: self._on_operator_clicked("+"))
        QShortcut(QKeySequence("-"), self).activated.connect(lambda: self._on_operator_clicked("-"))
        QShortcut(QKeySequence("*"), self).activated.connect(lambda: self._on_operator_clicked("×"))
        QShortcut(QKeySequence("/"), self).activated.connect(lambda: self._on_operator_clicked("/"))
        
        # 기능 키
        QShortcut(QKeySequence("Return"), self).activated.connect(self._on_equals_clicked)
        QShortcut(QKeySequence("Enter"), self).activated.connect(self._on_equals_clicked)
        QShortcut(QKeySequence("="), self).activated.connect(self._on_equals_clicked)
        QShortcut(QKeySequence("Escape"), self).activated.connect(self._on_clear_clicked)
        QShortcut(QKeySequence("Delete"), self).activated.connect(self._on_clear_clicked)
        QShortcut(QKeySequence("."), self).activated.connect(self._on_decimal_clicked)
        QShortcut(QKeySequence(","), self).activated.connect(self._on_decimal_clicked)  # 콤마도 소수점으로


def main() -> None:
    """
    메인 함수
    
    PyQt 애플리케이션을 초기화하고 계산기 윈도우를 표시합니다.
    """
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

