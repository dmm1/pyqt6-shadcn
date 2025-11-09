"""
Gray theme with OKLCH colors from Shadcn UI
"""

from themes.base import ShadcnTheme


class GrayTheme(ShadcnTheme):
    """Gray theme with light and dark variants"""

    @property
    def name(self) -> str:
        return "gray"

    def __init__(self):
        super().__init__()
        self._setup_colors()

    def _setup_colors(self):
        """Setup OKLCH colors for gray theme"""
        # Light mode colors
        self._light_colors = {
            "background": "oklch(0.98 0.00 248)",
            "foreground": "oklch(0.145 0.00 248)",
            "card": "oklch(0.98 0.00 248)",
            "card-foreground": "oklch(0.145 0.00 248)",
            "popover": "oklch(0.98 0.00 248)",
            "popover-foreground": "oklch(0.145 0.00 248)",
            "primary": "oklch(0.145 0.00 248)",
            "primary-foreground": "oklch(0.98 0.00 248)",
            "secondary": "oklch(0.967 0.00 248)",
            "secondary-foreground": "oklch(0.145 0.00 248)",
            "muted": "oklch(0.967 0.00 248)",
            "muted-foreground": "oklch(0.553 0.00 248)",
            "accent": "oklch(0.967 0.00 248)",
            "accent-foreground": "oklch(0.145 0.00 248)",
            "destructive": "oklch(0.704 0.191 22.216)",
            "destructive-foreground": "oklch(0.98 0.00 248)",
            "border": "oklch(0.929 0.00 248)",
            "input": "oklch(0.929 0.00 248)",
            "ring": "oklch(0.553 0.00 248)",
            "chart-1": "oklch(0.488 0.243 264.376)",
            "chart-2": "oklch(0.696 0.17 162.48)",
            "chart-3": "oklch(0.769 0.188 70.08)",
            "chart-4": "oklch(0.627 0.265 303.9)",
            "chart-5": "oklch(0.645 0.246 16.439)",
            "sidebar": "oklch(0.145 0.00 248)",
            "sidebar-foreground": "oklch(0.98 0.00 248)",
            "sidebar-primary": "oklch(0.488 0.243 264.376)",
            "sidebar-primary-foreground": "oklch(0.98 0.00 248)",
            "sidebar-accent": "oklch(0.278 0.033 256.848)",
            "sidebar-accent-foreground": "oklch(0.98 0.00 248)",
            "sidebar-border": "oklch(0.929 0.00 248)",
            "sidebar-ring": "oklch(0.553 0.00 248)",
        }

        # Dark mode colors
        self._dark_colors = {
            "background": "oklch(0.145 0.00 248)",
            "foreground": "oklch(0.98 0.00 248)",
            "card": "oklch(0.16 0.00 248)",
            "card-foreground": "oklch(0.98 0.00 248)",
            "popover": "oklch(0.16 0.00 248)",
            "popover-foreground": "oklch(0.98 0.00 248)",
            "primary": "oklch(0.696 0.17 162.48)",
            "primary-foreground": "oklch(0.98 0.00 248)",
            "secondary": "oklch(0.278 0.033 256.848)",
            "secondary-foreground": "oklch(0.98 0.00 248)",
            "muted": "oklch(0.278 0.033 256.848)",
            "muted-foreground": "oklch(0.707 0.022 261.325)",
            "accent": "oklch(0.278 0.033 256.848)",
            "accent-foreground": "oklch(0.98 0.00 248)",
            "destructive": "oklch(0.704 0.191 22.216)",
            "destructive-foreground": "oklch(0.98 0.00 248)",
            "border": "oklch(1 0 0 / 10%)",
            "input": "oklch(1 0 0 / 15%)",
            "ring": "oklch(0.553 0.00 248)",
            "chart-1": "oklch(0.488 0.243 264.376)",
            "chart-2": "oklch(0.696 0.17 162.48)",
            "chart-3": "oklch(0.769 0.188 70.08)",
            "chart-4": "oklch(0.627 0.265 303.9)",
            "chart-5": "oklch(0.645 0.246 16.439)",
            "sidebar": "oklch(0.147 0.00 248)",
            "sidebar-foreground": "oklch(0.98 0.00 248)",
            "sidebar-primary": "oklch(0.488 0.243 264.376)",
            "sidebar-primary-foreground": "oklch(0.98 0.00 248)",
            "sidebar-accent": "oklch(0.278 0.033 256.848)",
            "sidebar-accent-foreground": "oklch(0.98 0.00 248)",
            "sidebar-border": "oklch(1 0 0 / 10%)",
            "sidebar-ring": "oklch(0.553 0.00 248)",
        }
