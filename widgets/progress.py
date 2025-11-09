"""
Progress bar widget with dynamic text color
"""

from PyQt6.QtWidgets import QProgressBar


class ShadcnProgressBar(QProgressBar):
    """Progress bar with dynamic text color based on progress value"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRange(0, 100)
        self.setValue(0)
        self._update_text_color()

    def setValue(self, value):
        """Override setValue to update text color"""
        super().setValue(value)
        self._update_text_color()

    def _update_text_color(self):
        """Update text color based on current progress value"""
        value = self.value()
        if value >= 50:
            self.setStyleSheet("QProgressBar { color: #ffffff; }")
        else:
            self.setStyleSheet("QProgressBar { color: #0f172a; }")
