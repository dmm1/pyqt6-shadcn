"""
Orange theme with OKLCH colors from Shadcn UI
"""

from themes.base import ShadcnTheme


class OrangeTheme(ShadcnTheme):
    """Orange theme with light and dark variants"""

    @property
    def name(self) -> str:
        return "orange"

    def __init__(self):
        super().__init__()
        self._setup_colors()

    def _setup_colors(self):
        """Setup OKLCH colors for orange theme"""
        # Light mode colors
        self._light_colors = {
            "background": "oklch(0.984 0.003 247.858)",
            "foreground": "oklch(0.208 0.042 265.755)",
            "card": "oklch(0.984 0.003 247.858)",
            "card-foreground": "oklch(0.208 0.042 265.755)",
            "popover": "oklch(0.984 0.003 247.858)",
            "popover-foreground": "oklch(0.208 0.042 265.755)",
            "primary": "oklch(0.705 0.213 47)",
            "primary-foreground": "oklch(0.984 0.003 247.858)",
            "secondary": "oklch(0.968 0.007 247.896)",
            "secondary-foreground": "oklch(0.208 0.042 265.755)",
            "muted": "oklch(0.968 0.007 247.896)",
            "muted-foreground": "oklch(0.551 0.027 264.364)",
            "accent": "oklch(0.968 0.007 247.896)",
            "accent-foreground": "oklch(0.208 0.042 265.755)",
            "destructive": "oklch(0.704 0.191 22.216)",
            "destructive-foreground": "oklch(0.984 0.003 247.858)",
            "border": "oklch(0.928 0.006 264.531)",
            "input": "oklch(0.928 0.006 264.531)",
            "ring": "oklch(0.705 0.213 47)",
            "chart-1": "oklch(0.488 0.243 264.376)",
            "chart-2": "oklch(0.696 0.17 162.48)",
            "chart-3": "oklch(0.769 0.188 70.08)",
            "chart-4": "oklch(0.627 0.265 303.9)",
            "chart-5": "oklch(0.645 0.246 16.439)",
            "sidebar": "oklch(0.208 0.042 265.755)",
            "sidebar-foreground": "oklch(0.984 0.003 247.858)",
            "sidebar-primary": "oklch(0.705 0.213 47)",
            "sidebar-primary-foreground": "oklch(0.984 0.003 247.858)",
            "sidebar-accent": "oklch(0.279 0.041 260.031)",
            "sidebar-accent-foreground": "oklch(0.984 0.003 247.858)",
            "sidebar-border": "oklch(0.928 0.006 264.531)",
            "sidebar-ring": "oklch(0.705 0.213 47)",
        }

        # Dark mode colors
        self._dark_colors = {
            "background": "oklch(0.208 0.042 265.755)",
            "foreground": "oklch(0.984 0.003 247.858)",
            "card": "oklch(0.223 0.042 265.755)",
            "card-foreground": "oklch(0.984 0.003 247.858)",
            "popover": "oklch(0.223 0.042 265.755)",
            "popover-foreground": "oklch(0.984 0.003 247.858)",
            "primary": "oklch(0.705 0.213 47)",
            "primary-foreground": "oklch(0.984 0.003 247.858)",
            "secondary": "oklch(0.279 0.041 260.031)",
            "secondary-foreground": "oklch(0.984 0.003 247.858)",
            "muted": "oklch(0.279 0.041 260.031)",
            "muted-foreground": "oklch(0.707 0.022 261.325)",
            "accent": "oklch(0.279 0.041 260.031)",
            "accent-foreground": "oklch(0.984 0.003 247.858)",
            "destructive": "oklch(0.704 0.191 22.216)",
            "destructive-foreground": "oklch(0.984 0.003 247.858)",
            "border": "oklch(1 0 0 / 10%)",
            "input": "oklch(1 0 0 / 15%)",
            "ring": "oklch(0.705 0.213 47)",
            "chart-1": "oklch(0.488 0.243 264.376)",
            "chart-2": "oklch(0.696 0.17 162.48)",
            "chart-3": "oklch(0.769 0.188 70.08)",
            "chart-4": "oklch(0.627 0.265 303.9)",
            "chart-5": "oklch(0.645 0.246 16.439)",
            "sidebar": "oklch(0.21 0.034 264.665)",
            "sidebar-foreground": "oklch(0.985 0.002 247.839)",
            "sidebar-primary": "oklch(0.705 0.213 47)",
            "sidebar-primary-foreground": "oklch(0.985 0.002 247.839)",
            "sidebar-accent": "oklch(0.278 0.033 256.848)",
            "sidebar-accent-foreground": "oklch(0.985 0.002 247.839)",
            "sidebar-border": "oklch(1 0 0 / 10%)",
            "sidebar-ring": "oklch(0.705 0.213 47)",
        }
