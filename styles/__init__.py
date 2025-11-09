"""
Style manager for applying themes to PyQt6 applications
"""

from typing import Optional
from PyQt6.QtWidgets import QApplication
from themes import ThemeManager
from themes import Theme


class StyleManager:
    """Manages application styling and theme application"""

    def __init__(self):
        self.theme_manager = ThemeManager()
        self._app = None

    def set_application(self, app: QApplication):
        """Set the QApplication instance"""
        self._app = app

    def apply_theme(self, theme_name: Optional[str] = None):
        """Apply a theme to the application"""
        if theme_name:
            self.theme_manager.set_theme(theme_name)

        if self._app:
            stylesheet = self.theme_manager.current_theme.get_stylesheet(
                self.theme_manager.is_dark_mode
            )
            self._app.setStyleSheet(stylesheet)

    def get_current_theme(self) -> Theme:
        """Get the current theme"""
        return self.theme_manager.current_theme

    def get_available_themes(self) -> list[str]:
        """Get available theme names"""
        return self.theme_manager.get_available_themes()

    def switch_theme(self, theme_name: str) -> bool:
        """Switch to a different theme"""
        if self.theme_manager.set_theme(theme_name):
            self.apply_theme()
            # Force repaint of all widgets
            if self._app:
                for widget in self._app.allWidgets():
                    widget.repaint()
            return True
        return False

    def toggle_dark_mode(self):
        """Toggle between light and dark mode"""
        self.theme_manager.toggle_dark_mode()
        self.apply_theme()
        # Force repaint of all widgets
        if self._app:
            for widget in self._app.allWidgets():
                widget.repaint()

    def set_dark_mode(self, dark: bool):
        """Set dark mode state"""
        self.theme_manager.set_dark_mode(dark)
        self.apply_theme()
        # Force repaint of all widgets
        if self._app:
            for widget in self._app.allWidgets():
                widget.repaint()

    def get_current_theme_name(self) -> str:
        """Get current theme name"""
        return self.theme_manager.current_theme_name

    def is_dark_mode(self) -> bool:
        """Check if dark mode is active"""
        return self.theme_manager.is_dark_mode


# Global style manager instance
style_manager = StyleManager()
