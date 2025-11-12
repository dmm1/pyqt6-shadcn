"""
Custom input widgets for Shadcn-inspired PyQt6 applications
"""

from PyQt6.QtWidgets import (
    QLineEdit,
    QTextEdit,
    QComboBox,
    QCheckBox,
    QRadioButton,
    QSlider,
    QVBoxLayout,
    QWidget,
    QLabel,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class ShadcnInput(QLineEdit):
    """Shadcn-inspired input field"""

    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setObjectName("shadcn_input")
        self.setMinimumHeight(40)
        self.setFont(QFont("Segoe UI", 10))


class ShadcnTextArea(QTextEdit):
    """Shadcn-inspired text area"""

    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setObjectName("shadcn_textarea")
        self.setMinimumHeight(80)
        self.setMaximumHeight(120)
        self.setFont(QFont("Segoe UI", 10))


class ShadcnSelect(QComboBox):
    """Shadcn-inspired select dropdown"""

    def __init__(self, items=None, parent=None):
        super().__init__(parent)
        self.setObjectName("shadcn_select")
        self.setMinimumHeight(40)
        self.setFont(QFont("Segoe UI", 10))
        if items:
            self.addItems(items)


class ShadcnCheckbox(QCheckBox):
    """Shadcn-inspired checkbox"""

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setObjectName("shadcn_checkbox")
        self.setFont(QFont("Segoe UI", 10))


class ShadcnRadioButton(QRadioButton):
    """Shadcn-inspired radio button"""

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setObjectName("shadcn_radio")
        self.setFont(QFont("Segoe UI", 10))


class ShadcnSlider(QSlider):
    """Shadcn-inspired slider"""

    def __init__(self, orientation=Qt.Orientation.Horizontal, parent=None):
        super().__init__(orientation, parent)
        self.setObjectName("shadcn_slider")
        (
            self.setMinimumHeight(20)
            if orientation == Qt.Orientation.Horizontal
            else self.setMinimumWidth(20)
        )


class ShadcnFormField(QWidget):
    """Form field wrapper with label and input"""

    def __init__(self, label_text="", input_widget=None, parent=None):
        super().__init__(parent)
        self.setObjectName("shadcn_form_field")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        if label_text:
            self.label = QLabel(label_text)
            self.label.setObjectName("shadcn_label")
            self.label.setFont(QFont("Segoe UI", 10, QFont.Weight.Medium))
            layout.addWidget(self.label)

        if input_widget:
            self.input_widget = input_widget
            layout.addWidget(input_widget)

    def get_input(self):
        """Get the input widget"""
        return getattr(self, "input_widget", None)

    def set_label(self, text):
        """Set the label text"""
        if hasattr(self, "label"):
            self.label.setText(text)

    def get_value(self):
        """Get the value from the input widget"""
        if hasattr(self, "input_widget"):
            if isinstance(self.input_widget, (ShadcnInput, QLineEdit)):
                return self.input_widget.text()
            elif isinstance(self.input_widget, (ShadcnTextArea, QTextEdit)):
                return self.input_widget.toPlainText()
            elif isinstance(self.input_widget, (ShadcnSelect, QComboBox)):
                return self.input_widget.currentText()
            elif isinstance(self.input_widget, (ShadcnCheckbox, QCheckBox)):
                return self.input_widget.isChecked()
            elif isinstance(self.input_widget, (ShadcnRadioButton, QRadioButton)):
                return self.input_widget.isChecked()
            elif isinstance(self.input_widget, (ShadcnSlider, QSlider)):
                return self.input_widget.value()
        return None

    def set_value(self, value):
        """Set the value for the input widget"""
        if hasattr(self, "input_widget"):
            if isinstance(self.input_widget, (ShadcnInput, QLineEdit)):
                self.input_widget.setText(str(value))
            elif isinstance(self.input_widget, (ShadcnTextArea, QTextEdit)):
                self.input_widget.setPlainText(str(value))
            elif isinstance(self.input_widget, (ShadcnSelect, QComboBox)):
                index = self.input_widget.findText(str(value))
                if index >= 0:
                    self.input_widget.setCurrentIndex(index)
            elif isinstance(self.input_widget, (ShadcnCheckbox, QCheckBox)):
                self.input_widget.setChecked(bool(value))
            elif isinstance(self.input_widget, (ShadcnRadioButton, QRadioButton)):
                self.input_widget.setChecked(bool(value))
            elif isinstance(self.input_widget, (ShadcnSlider, QSlider)):
                self.input_widget.setValue(int(value))
