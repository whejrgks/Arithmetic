"""
PyQt 계산기 GUI 애플리케이션
"""
import sys
from typing import Optional
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout,
    QPushButton, QLineEdit
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from src.calculator_controller import CalculatorController


class CalculatorWindow(QMainWindow):
    """계산기 메인 윈도우"""
    
    def __init__(self):
        """계산기 윈도우 초기화"""
        super().__init__()
        self._controller = CalculatorController()
        self._controller.set_display_callback(self._update_display)
        self._init_ui()
    
    def _init_ui(self) -> None:
        """UI 초기화"""
        self.setWindowTitle("계산기")
        self.setFixedSize(300, 400)
        
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
        self._display.setFont(QFont("Arial", 20))
        self._display.setText("0")
        main_layout.addWidget(self._display)
        
        # 버튼 그리드
        button_layout = QGridLayout()
        main_layout.addLayout(button_layout)
        
        # 버튼 정의
        buttons = [
            # 행, 열, 텍스트, 스타일
            (0, 0, "7", None),
            (0, 1, "8", None),
            (0, 2, "9", None),
            (0, 3, "×", "operator"),
            (1, 0, "4", None),
            (1, 1, "5", None),
            (1, 2, "6", None),
            (1, 3, "−", "operator"),
            (2, 0, "1", None),
            (2, 1, "2", None),
            (2, 2, "3", None),
            (2, 3, "+", "operator"),
            (3, 0, "+/−", "function"),
            (3, 1, "0", None),
            (3, 2, ".", "function"),
            (3, 3, "=", "equals"),
        ]
        
        # 버튼 생성 및 연결
        for row, col, text, style in buttons:
            button = QPushButton(text)
            button.setFont(QFont("Arial", 14))
            button.setMinimumHeight(50)
            
            # 스타일 적용
            if style == "operator":
                button.setStyleSheet("background-color: #4a4a4a; color: white;")
            elif style == "equals":
                button.setStyleSheet("background-color: #0078d4; color: white;")
            elif style == "function":
                button.setStyleSheet("background-color: #4a4a4a; color: white;")
            else:
                button.setStyleSheet("background-color: #2d2d2d; color: white;")
            
            # 시그널 연결
            if text.isdigit():
                button.clicked.connect(lambda checked, d=text: self._on_number_clicked(d))
            elif text in ("+", "−", "×", "/"):
                button.clicked.connect(lambda checked, op=text: self._on_operator_clicked(op))
            elif text == "=":
                button.clicked.connect(self._on_equals_clicked)
            elif text == "+/−":
                button.clicked.connect(self._on_toggle_sign_clicked)
            elif text == ".":
                button.clicked.connect(self._on_decimal_clicked)
            
            button_layout.addWidget(button, row, col)
        
        # Clear 버튼 (별도 추가)
        clear_button = QPushButton("Clear")
        clear_button.setFont(QFont("Arial", 14))
        clear_button.setMinimumHeight(50)
        clear_button.setStyleSheet("background-color: #d13438; color: white;")
        clear_button.clicked.connect(self._on_clear_clicked)
        button_layout.addWidget(clear_button, 4, 0, 1, 4)
    
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


def main():
    """메인 함수"""
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

