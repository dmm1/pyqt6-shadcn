"""
Progress bar widget with Shadcn styling
"""

from PyQt6.QtWidgets import QProgressBar


class ShadcnProgressBar(QProgressBar):
    """Progress bar with Shadcn styling"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRange(0, 100)
        self.setValue(0)
        self.setObjectName("progress")
        # Ensure text is visible
        self.setTextVisible(True)
        self.setFormat("%p%")  # Show percentage
