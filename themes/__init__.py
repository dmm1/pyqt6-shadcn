"""
Theme system for PyQt6 applications
"""

from typing import Optional
from themes.base import Theme
from themes.neutral import NeutralTheme
from themes.stone import StoneTheme
from themes.zinc import ZincTheme
from themes.slate import SlateTheme
from themes.gray import GrayTheme
from themes.red import RedTheme
from themes.orange import OrangeTheme
from themes.amber import AmberTheme
from themes.yellow import YellowTheme
from themes.lime import LimeTheme
from themes.green import GreenTheme
from themes.emerald import EmeraldTheme
from themes.teal import TealTheme
from themes.cyan import CyanTheme
from themes.sky import SkyTheme
from themes.blue import BlueTheme
from themes.indigo import IndigoTheme
from themes.violet import VioletTheme
from themes.purple import PurpleTheme
from themes.fuchsia import FuchsiaTheme
from themes.pink import PinkTheme
from themes.rose import RoseTheme


class ThemeManager:
    """Manages theme switching and application"""

    def __init__(self):
        self.themes = {
            "neutral": NeutralTheme(),
            "stone": StoneTheme(),
            "zinc": ZincTheme(),
            "slate": SlateTheme(),
            "gray": GrayTheme(),
            "red": RedTheme(),
            "orange": OrangeTheme(),
            "amber": AmberTheme(),
            "yellow": YellowTheme(),
            "lime": LimeTheme(),
            "green": GreenTheme(),
            "emerald": EmeraldTheme(),
            "teal": TealTheme(),
            "cyan": CyanTheme(),
            "sky": SkyTheme(),
            "blue": BlueTheme(),
            "indigo": IndigoTheme(),
            "violet": VioletTheme(),
            "purple": PurpleTheme(),
            "fuchsia": FuchsiaTheme(),
            "pink": PinkTheme(),
            "rose": RoseTheme(),
        }
        self.current_theme = self.themes["neutral"]
        self.current_dark_mode = False

    def set_theme(self, theme_name: str, dark_mode: bool = False) -> bool:
        """Set the current theme and mode"""
        if theme_name in self.themes:
            self.current_theme = self.themes[theme_name]
            self.current_dark_mode = dark_mode
            return True
        return False

    def toggle_dark_mode(self) -> bool:
        """Toggle between light and dark mode"""
        self.current_dark_mode = not self.current_dark_mode
        return self.current_dark_mode

    def set_dark_mode(self, dark: bool):
        """Set dark mode state"""
        self.current_dark_mode = dark

    def get_theme(self, theme_name: str) -> Optional[Theme]:
        """Get a theme by name"""
        return self.themes.get(theme_name)

    def get_available_themes(self) -> list[str]:
        """Get list of available theme names"""
        return list(self.themes.keys())

    @property
    def current_theme_name(self) -> str:
        """Get current theme name"""
        return self.current_theme.name

    def get_current_theme_name(self) -> str:
        """Get current theme name"""
        return self.current_theme_name

    @property
    def is_dark_mode(self) -> bool:
        """Check if dark mode is active"""
        return self.current_dark_mode
