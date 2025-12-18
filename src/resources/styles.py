"""
계산기 UI 스타일 상수 정의
매직 스트링을 제거하고 상수로 관리합니다.
"""


class CalculatorStyles:
    """계산기 UI 스타일 상수 클래스"""
    
    # 색상 상수
    COLOR_BACKGROUND = "#1e1e1e"
    COLOR_NUMBER_BUTTON = "#2d2d2d"
    COLOR_OPERATOR_BUTTON = "#4a4a4a"
    COLOR_EQUALS_BUTTON = "#0078d4"
    COLOR_CLEAR_BUTTON = "#d13438"
    COLOR_TEXT = "white"
    
    # 폰트 상수
    FONT_FAMILY = "Arial"
    FONT_SIZE_DISPLAY = 24
    FONT_SIZE_BUTTON = 14
    
    # 크기 상수
    WINDOW_WIDTH = 320
    WINDOW_HEIGHT = 450
    BUTTON_MIN_HEIGHT = 50
    
    # 스타일 템플릿
    STYLE_BUTTON_BASE = "color: {color}; border: none; border-radius: 4px;"
    STYLE_BUTTON_BOLD = "color: {color}; border: none; border-radius: 4px; font-weight: bold;"
    
    # 디스플레이 스타일
    DISPLAY_BORDER_COLOR = COLOR_OPERATOR_BUTTON
    DISPLAY_PADDING = "10px"
    DISPLAY_BORDER_WIDTH = "2px"
    DISPLAY_BORDER_RADIUS = "4px"
    
    @classmethod
    def get_display_style(cls) -> str:
        """
        디스플레이 스타일 문자열을 반환합니다.
        
        Returns:
            CSS 스타일 문자열
        """
        return (
            f"background-color: {cls.COLOR_BACKGROUND}; "
            f"color: {cls.COLOR_TEXT}; "
            f"border: {cls.DISPLAY_BORDER_WIDTH} solid {cls.DISPLAY_BORDER_COLOR}; "
            f"border-radius: {cls.DISPLAY_BORDER_RADIUS}; "
            f"padding: {cls.DISPLAY_PADDING};"
        )
    
    @classmethod
    def get_window_style(cls) -> str:
        """
        윈도우 스타일 문자열을 반환합니다.
        
        Returns:
            CSS 스타일 문자열
        """
        return f"background-color: {cls.COLOR_BACKGROUND};"
    
    @classmethod
    def get_button_style(cls, style_type: str) -> str:
        """
        버튼 스타일 문자열을 반환합니다.
        
        Args:
            style_type: 버튼 스타일 타입 ("number", "operator", "function", "equals", "clear")
            
        Returns:
            CSS 스타일 문자열
        """
        style_map = {
            "number": {
                "background": cls.COLOR_NUMBER_BUTTON,
                "template": cls.STYLE_BUTTON_BASE
            },
            "operator": {
                "background": cls.COLOR_OPERATOR_BUTTON,
                "template": cls.STYLE_BUTTON_BASE
            },
            "function": {
                "background": cls.COLOR_OPERATOR_BUTTON,
                "template": cls.STYLE_BUTTON_BASE
            },
            "equals": {
                "background": cls.COLOR_EQUALS_BUTTON,
                "template": cls.STYLE_BUTTON_BOLD
            },
            "clear": {
                "background": cls.COLOR_CLEAR_BUTTON,
                "template": cls.STYLE_BUTTON_BOLD
            }
        }
        
        style_config = style_map.get(style_type, style_map["number"])
        return (
            f"background-color: {style_config['background']}; "
            f"{style_config['template'].format(color=cls.COLOR_TEXT)}"
        )

