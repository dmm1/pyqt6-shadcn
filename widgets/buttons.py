"""
Custom button widgets with Shadcn styling
"""

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt


class ShadcnButton(QPushButton):
    """Custom button with Shadcn styling variants"""

    def __init__(self, text, variant="default", parent=None):
        super().__init__(text, parent)
        self.setProperty("class", variant)
        self.setCursor(Qt.CursorShape.PointingHandCursor)


class PrimaryButton(ShadcnButton):
    """Primary action button"""

    def __init__(self, text, parent=None):
        super().__init__(text, "primary", parent)


class SecondaryButton(ShadcnButton):
    """Secondary action button"""

    def __init__(self, text, parent=None):
        super().__init__(text, "secondary", parent)


class OutlineButton(ShadcnButton):
    """Outlined button"""

    def __init__(self, text, parent=None):
        super().__init__(text, "outline", parent)


class GhostButton(ShadcnButton):
    """Ghost button with no background"""

    def __init__(self, text, parent=None):
        super().__init__(text, "ghost", parent)
