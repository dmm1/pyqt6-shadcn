"""
Base theme classes for PyQt6 applications
"""

from abc import ABC, abstractmethod
from typing import Dict
import coloraide  # type: ignore


class Theme(ABC):
    """Abstract base class for themes"""

    @property
    @abstractmethod
    def name(self) -> str:
        """Theme name"""
        pass

    @abstractmethod
    def get_stylesheet(self, dark_mode: bool = False) -> str:
        """Generate the complete stylesheet for this theme"""
        pass


class ShadcnTheme(Theme):
    """Base class for Shadcn-inspired themes"""

    def __init__(self):
        self._current_dark_mode = False

    @property
    def name(self) -> str:
        """Theme name - override in subclasses"""
        return "base"

    def get_stylesheet(self, dark_mode: bool = False) -> str:
        """Generate stylesheet using OKLCH colors"""
        colors = self.get_colors_for_mode(dark_mode)
        return self._generate_stylesheet(colors)

    def get_colors_for_mode(self, dark_mode: bool = False) -> Dict[str, str]:
        """Get colors for the specified mode, converting OKLCH to hex"""
        if dark_mode:
            raw_colors = getattr(self, "_dark_colors", {})
        else:
            raw_colors = getattr(self, "_light_colors", {})

        # Convert OKLCH colors to hex
        converted_colors = {}
        for key, value in raw_colors.items():
            if value.startswith("oklch("):
                converted_colors[key] = self._oklch_to_hex(value)
            else:
                converted_colors[key] = value

        return converted_colors

    def _oklch_to_hex(self, oklch_str: str) -> str:
        """Convert OKLCH color string to hex format"""
        try:
            # Parse OKLCH values: oklch(L C H)
            values = oklch_str.replace("oklch(", "").replace(")", "").split()
            if len(values) != 3:
                return "#000000"  # fallback

            lightness = float(values[0])
            c = float(values[1])
            h = float(values[2])

            # Convert OKLCH to sRGB using coloraide
            color = coloraide.Color("oklch", [lightness, c, h])
            rgb = color.convert("srgb")
            r, g, b = rgb.coords()

            # Convert to 0-255 range and create hex
            r_int = max(0, min(255, int(r * 255)))
            g_int = max(0, min(255, int(g * 255)))
            b_int = max(0, min(255, int(b * 255)))

            return f"#{r_int:02x}{g_int:02x}{b_int:02x}"

        except Exception as e:
            print(f"Error converting OKLCH color {oklch_str}: {e}")
            return "#000000"  # fallback to black

    def _generate_stylesheet(self, colors: Dict[str, str]) -> str:
        """Generate the QSS stylesheet from colors"""
        return f"""
        /* Global styles */
        QWidget {{
            color: {colors.get('foreground', '#0f172a')};
            background-color: {colors.get('background', '#ffffff')};
        }}

        /* Main window background */
        QMainWindow, QWidget#MainWindow {{
            background-color: {colors.get('background', '#ffffff')};
            color: {colors.get('foreground', '#0f172a')};
        }}

        /* Try to affect window frame */
        QMainWindow {{
            background-color: {colors.get('background', '#ffffff')};
        }}

        /* Buttons */
        QPushButton {{
            background-color: {colors.get('background', '#f8fafc')};
            border: 1px solid {colors.get('border', '#e2e8f0')};
            border-radius: 6px;
            padding: 8px 16px;
            font-weight: 500;
            color: {colors.get('foreground', '#475569')};
            min-height: 36px;
        }}

        QPushButton:hover {{
            background-color: {colors.get('muted', '#f1f5f9')};
            border-color: {colors.get('border', '#cbd5e1')};
        }}

        QPushButton:pressed {{
            background-color: {colors.get('border', '#e2e8f0')};
        }}

        QPushButton#primary {{
            background-color: {colors.get('primary', '#0f172a')};
            border-color: {colors.get('primary', '#0f172a')};
            color: {colors.get('primary-foreground', '#ffffff')};
        }}

        QPushButton#primary:hover {{
            background-color: {colors.get('primary', '#1e293b')};
            border-color: {colors.get('primary', '#1e293b')};
        }}

        QPushButton#secondary {{
            background-color: {colors.get('secondary', '#f1f5f9')};
            border-color: {colors.get('border', '#e2e8f0')};
            color: {colors.get('secondary-foreground', '#475569')};
        }}

        QPushButton#secondary:hover {{
            background-color: {colors.get('muted', '#e2e8f0')};
            border-color: {colors.get('border', '#cbd5e1')};
        }}

        QPushButton#outline {{
            background-color: transparent;
            border: 1px solid {colors.get('border', '#e2e8f0')};
            color: {colors.get('foreground', '#475569')};
        }}

        QPushButton#outline:hover {{
            background-color: {colors.get('background', '#f8fafc')};
            border-color: {colors.get('border', '#cbd5e1')};
        }}

        QPushButton#ghost {{
            background-color: transparent;
            border: none;
            color: {colors.get('foreground', '#475569')};
        }}

        QPushButton#ghost:hover {{
            background-color: {colors.get('muted', '#f1f5f9')};
        }}

        /* Input fields */
        QLineEdit, QTextEdit {{
            background-color: {colors.get('background', '#ffffff')};
            border: 1px solid {colors.get('border', '#e2e8f0')};
            border
            padding: 8px 12px;
            font-size: 14px;
            color: {colors.get('foreground', '#0f172a')};
        }}

        QLineEdit:focus, QTextEdit:focus {{
            border-color: {colors.get('ring', '#3b82f6')};
            outline: none;
        }}

        QLineEdit:hover, QTextEdit:hover {{
            border-color: {colors.get('border', '#cbd5e1')};
        }}

        /* Labels */
        QLabel {{
            color: {colors.get('foreground', '#374151')};
            font-size: 14px;
        }}

        QLabel#heading {{
            font-size: 24px;
            font-weight: 600;
            color: {colors.get('foreground', '#0f172a')};
            margin-bottom: 8px;
        }}

        QLabel#subheading {{
            font-size: 18px;
            font-weight: 500;
            color: {colors.get('foreground', '#374151')};
            margin-bottom: 4px;
        }}

        /* Cards */
        QFrame#card {{
            background-color: {colors.get('card', '#ffffff')};
            border: 1px solid {colors.get('border', '#e2e8f0')};
            border-radius: 8px;
            padding: 16px;
        }}

        QFrame#card:hover {{
            border-color: {colors.get('border', '#cbd5e1')};
        }}

        /* Group boxes */
        QGroupBox {{
            font-weight: 600;
            border: 1px solid {colors.get('border', '#e2e8f0')};
            border-radius: 8px;
            margin-top: 8px;
            padding-top: 16px;
        }}

        QGroupBox::title {{
            subcontrol-origin: margin;
            left: 12px;
            padding: 0 8px 0 8px;
            color: {colors.get('foreground', '#374151')};
            font-weight: 600;
        }}

        /* Checkboxes and Radio buttons */
        QCheckBox, QRadioButton {{
            spacing: 8px;
            color: {colors.get('foreground', '#0f172a')};
        }}

        QCheckBox::indicator, QRadioButton::indicator {{
            width: 16px;
            height: 16px;
            border: 1px solid {colors.get('border', '#d1d5db')};
            border-radius: 3px;
            background-color: {colors.get('background', '#ffffff')};
        }}

        QCheckBox::indicator:hover, QRadioButton::indicator:hover {{
            border-color: {colors.get('muted-foreground', '#9ca3af')};
        }}

        QCheckBox::indicator:checked {{
            background-color: {colors.get('primary', '#0f172a')};
            border-color: {colors.get('primary', '#0f172a')};
        }}

        QRadioButton::indicator:checked {{
            background-color: {colors.get('primary', '#0f172a')};
            border-color: {colors.get('primary', '#0f172a')};
            border-radius: 8px;
        }}

        /* Combo boxes */
        QComboBox {{
            background-color: {colors.get('background', '#ffffff')};
            border: 1px solid {colors.get('border', '#e2e8f0')};
            border-radius: 6px;
            padding: 8px 12px;
            min-height: 36px;
            color: {colors.get('foreground', '#0f172a')};
        }}

        QComboBox:hover {{
            border-color: {colors.get('border', '#cbd5e1')};
        }}

        QComboBox:focus {{
            border-color: {colors.get('ring', '#3b82f6')};
            outline: none;
        }}

        QComboBox::drop-down {{
            border: none;
            width: 20px;
        }}

        QComboBox::down-arrow {{
            border: none;
            background: none;
            color: {colors.get('foreground', '#0f172a')};
        }}

        QComboBox QAbstractItemView {{
            background-color: {colors.get('background', '#ffffff')};
            border: 1px solid {colors.get('border', '#e2e8f0')};
            border-radius: 6px;
            selection-background-color: {colors.get('muted', '#f1f5f9')};
            selection-color: {colors.get('foreground', '#0f172a')};
        }}

        /* Sliders */
        QSlider::groove:horizontal {{
            height: 4px;
            background-color: {colors.get('border', '#e2e8f0')};
            border-radius: 2px;
        }}

        QSlider::handle:horizontal {{
            background-color: {colors.get('primary', '#0f172a')};
            border: none;
            width: 16px;
            height: 16px;
            border-radius: 8px;
            margin: -6px 0;
        }}

        QSlider::handle:horizontal:hover {{
            background-color: {colors.get('primary', '#1e293b')};
        }}

        /* Progress bars */
        QProgressBar {{
            border: 1px solid {colors.get('border', '#e2e8f0')};
            border-radius: 4px;
            text-align: center;
            background-color: {colors.get('background', '#f8fafc')};
            color: {colors.get('primary-foreground', '#ffffff')};
            font-weight: 500;
        }}

        QProgressBar::chunk {{
            background-color: {colors.get('primary', '#0f172a')};
            border-radius: 3px;
        }}

        /* Scroll bars */
        QScrollBar:vertical {{
            background-color: {colors.get('background', '#f8fafc')};
            width: 12px;
            border-radius: 6px;
        }}

        QScrollBar::handle:vertical {{
            background-color: {colors.get('border', '#cbd5e1')};
            border-radius: 6px;
            min-height: 30px;
        }}

        QScrollBar::handle:vertical:hover {{
            background-color: {colors.get('muted-foreground', '#94a3b8')};
        }}

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            border: none;
            background: none;
        }}

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
            background: none;
        }}

        /* Custom title bar */
        QWidget#title_bar {{
            background-color: {colors.get('background', '#ffffff')};
            border-bottom: 1px solid {colors.get('border', '#e2e8f0')};
        }}

        QPushButton#title_bar_button {{
            background-color: transparent;
            border: none;
            color: {colors.get('foreground', '#0f172a')};
            font-size: 14px;
            font-weight: bold;
        }}

        QPushButton#title_bar_button:hover {{
            background-color: {colors.get('muted', '#f1f5f9')};
        }}

        QPushButton#close_button {{
            background-color: transparent;
            border: none;
            color: {colors.get('foreground', '#0f172a')};
            font-size: 14px;
            font-weight: bold;
        }}

        QPushButton#close_button:hover {{
            background-color: {colors.get('destructive', '#ef4444')};
            color: {colors.get('destructive-foreground', '#ffffff')};
        }}
        """
