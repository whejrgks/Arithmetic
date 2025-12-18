"""
PyQt 계산기 GUI 애플리케이션
"""
import sys
import os
from typing import Optional

# 프로젝트 루트를 sys.path에 추가
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


class CalculatorWindow(QMainWindow):
    """계산기 메인 윈도우"""
    
    def __init__(self):
        """계산기 윈도우 초기화"""
        super().__init__()
        self._controller = CalculatorController()
        self._controller.set_display_callback(self._update_display)
        self._init_ui()
        self._setup_shortcuts()  # 키보드 단축키 설정
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
        self.setWindowTitle("계산기")
        self.setFixedSize(320, 450)
        
        # 윈도우 스타일 설정
        self.setStyleSheet("background-color: #1e1e1e;")
        
        # 중앙 위젯
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 메인 레이아웃
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # 디스플레이
        self._display = QLineEdit()
        self._display.setReadOnly(True)
        self._display.setAlignment(Qt.AlignRight)
        self._display.setFont(QFont("Arial", 24, QFont.Bold))
        self._display.setText("0")
        self._display.setStyleSheet(
            "background-color: #1e1e1e; color: white; "
            "border: 2px solid #4a4a4a; border-radius: 4px; "
            "padding: 10px;"
        )
        main_layout.addWidget(self._display)
        
        # 버튼 그리드
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
        
        # 나눗셈 버튼 추가 (별도 행 또는 기존 레이아웃에 추가)
        # 이미지에는 없지만 기능상 필요하므로 추가
        divide_button = QPushButton("/")
        divide_button.setFont(QFont("Arial", 14))
        divide_button.setMinimumHeight(50)
        divide_button.setStyleSheet("background-color: #4a4a4a; color: white;")
        divide_button.clicked.connect(lambda: self._on_operator_clicked("/"))
        button_layout.addWidget(divide_button, 4, 3)  # Clear 버튼 옆에 배치
        
        # 버튼 생성 및 연결
        for row, col, text, style in buttons:
            button = QPushButton(text)
            button.setFont(QFont("Arial", 14))
            button.setMinimumHeight(50)
            
            # 스타일 적용 (이미지 디자인 반영)
            if style == "operator":
                # 연산자 버튼: 어두운 회색 배경
                button.setStyleSheet(
                    "background-color: #4a4a4a; color: white; "
                    "border: none; border-radius: 4px;"
                )
            elif style == "equals":
                # 등호 버튼: 파란색 배경 (이미지에서 강조)
                button.setStyleSheet(
                    "background-color: #0078d4; color: white; "
                    "border: none; border-radius: 4px; font-weight: bold;"
                )
            elif style == "function":
                # 기능 버튼: 어두운 회색 배경
                button.setStyleSheet(
                    "background-color: #4a4a4a; color: white; "
                    "border: none; border-radius: 4px;"
                )
            else:  # number
                # 숫자 버튼: 더 어두운 회색 배경
                button.setStyleSheet(
                    "background-color: #2d2d2d; color: white; "
                    "border: none; border-radius: 4px;"
                )
            
            # 호버 효과 추가
            button.setCursor(Qt.PointingHandCursor)
            
            # 시그널-슬롯 연결
            # 숫자 버튼 클릭 → controller.input_number()
            if text.isdigit():
                button.clicked.connect(lambda checked, d=text: self._on_number_clicked(d))
            # 연산자 버튼 클릭 → controller.set_operator()
            elif text in ("+", "−", "×"):
                button.clicked.connect(lambda checked, op=text: self._on_operator_clicked(op))
            # 등호 버튼 클릭 → controller.calculate()
            elif text == "=":
                button.clicked.connect(self._on_equals_clicked)
            # 부호 변경 버튼 클릭 → controller.toggle_sign()
            elif text == "+/−":
                button.clicked.connect(self._on_toggle_sign_clicked)
            # 소수점 버튼 클릭 → controller.input_decimal()
            elif text == ".":
                button.clicked.connect(self._on_decimal_clicked)
            
            button_layout.addWidget(button, row, col)
        
        # Clear 버튼 (별도 추가)
        clear_button = QPushButton("Clear")
        clear_button.setFont(QFont("Arial", 14))
        clear_button.setMinimumHeight(50)
        clear_button.setStyleSheet(
            "background-color: #d13438; color: white; "
            "border: none; border-radius: 4px; font-weight: bold;"
        )
        clear_button.setCursor(Qt.PointingHandCursor)
        clear_button.clicked.connect(self._on_clear_clicked)
        button_layout.addWidget(clear_button, 4, 0, 1, 3)  # 나눗셈 버튼 공간 확보
    
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
            operator: 클릭된 연산자
        """
        # − 기호를 -로 변환
        if operator == "−":
            operator = "-"
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


def main():
    """메인 함수"""
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

