"""
Card widget with Shadcn styling
"""

from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel


class ShadcnCard(QFrame):
    """Card widget with Shadcn styling"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("card")
        self.setFrameStyle(QFrame.Shape.NoFrame)
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(16, 16, 16, 16)
        self._layout.setSpacing(8)

    def add_widget(self, widget):
        """Add a widget to the card"""
        self._layout.addWidget(widget)

    def set_spacing(self, spacing):
        """Set spacing between card elements"""
        self._layout.setSpacing(spacing)


class ShadcnLabel(QLabel):
    """Label with Shadcn styling variants"""

    def __init__(self, text, variant="default", parent=None):
        super().__init__(text, parent)
        if variant != "default":
            self.setObjectName(variant)


class HeadingLabel(ShadcnLabel):
    """Heading label"""

    def __init__(self, text, parent=None):
        super().__init__(text, "heading", parent)


class SubheadingLabel(ShadcnLabel):
    """Subheading label"""

    def __init__(self, text, parent=None):
        super().__init__(text, "subheading", parent)
