#!/usr/bin/env python3
"""
PyQt6 GUI with Shadcn-inspired styling - Modular version
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QTextEdit,
    QGroupBox,
    QCheckBox,
    QRadioButton,
    QComboBox,
    QSlider,
    QPushButton,
    QSizePolicy,
)
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QFont

# Import our modular components
from widgets import (
    PrimaryButton,
    SecondaryButton,
    OutlineButton,
    GhostButton,
    ShadcnCard,
    ShadcnLabel,
    ShadcnProgressBar,
)


class CustomTitleBar(QWidget):
    """Custom title bar widget that matches the theme"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.drag_start_position = None
        self.setFixedHeight(40)
        self.setObjectName("title_bar")
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 0, 12, 0)
        layout.setSpacing(8)

        # Window title
        self.title_label = ShadcnLabel("Shadcn-inspired PyQt6 GUI", "heading")
        size_policy = self.title_label.sizePolicy()
        size_policy.setHorizontalPolicy(QSizePolicy.Policy.Expanding)
        size_policy.setVerticalPolicy(QSizePolicy.Policy.Preferred)
        self.title_label.setSizePolicy(size_policy)

        # Window controls
        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(0)

        # Minimize button
        self.minimize_btn = QPushButton("—")
        self.minimize_btn.setFixedSize(40, 30)
        self.minimize_btn.setObjectName("title_bar_button")
        self.minimize_btn.clicked.connect(self.minimize_window)

        # Maximize button
        self.maximize_btn = QPushButton("⬜")
        self.maximize_btn.setFixedSize(40, 30)
        self.maximize_btn.setObjectName("title_bar_button")
        self.maximize_btn.clicked.connect(self.toggle_maximize)

        # Close button
        self.close_btn = QPushButton("✕")
        self.close_btn.setFixedSize(40, 30)
        self.close_btn.setObjectName("close_button")
        self.close_btn.clicked.connect(self.close_window)

        controls_layout.addWidget(self.minimize_btn)
        controls_layout.addWidget(self.maximize_btn)
        controls_layout.addWidget(self.close_btn)

        layout.addWidget(self.title_label)
        layout.addLayout(controls_layout)

    def minimize_window(self):
        if self.parent_window:
            self.parent_window.showMinimized()

    def toggle_maximize(self):
        if self.parent_window:
            if self.parent_window.isMaximized():
                self.parent_window.showNormal()
                self.maximize_btn.setText("⬜")
            else:
                self.parent_window.showMaximized()
                self.maximize_btn.setText("❐")

    def close_window(self):
        if self.parent_window:
            self.parent_window.close()

    def mousePressEvent(self, a0):
        if a0 and a0.button() == Qt.MouseButton.LeftButton and self.parent_window:
            self.drag_start_position = (
                a0.globalPosition().toPoint()
                - self.parent_window.frameGeometry().topLeft()
            )
            a0.accept()

    def mouseMoveEvent(self, a0):
        if (
            a0
            and a0.buttons() & Qt.MouseButton.LeftButton
            and self.drag_start_position is not None
            and self.parent_window
            and not self.parent_window.isMaximized()
        ):
            new_pos = a0.globalPosition().toPoint() - self.drag_start_position
            self.parent_window.move(new_pos)
            a0.accept()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Make window frameless and add custom title bar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window)
        self.setWindowTitle("Shadcn-inspired PyQt6 GUI")
        self.setMinimumSize(800, 700)
        self.resize(900, 800)
        self.setObjectName("MainWindow")

        # Create main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Add custom title bar
        self.title_bar = CustomTitleBar(self)
        self.main_layout.addWidget(self.title_bar)

        # Create content widget
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setSpacing(16)
        self.content_layout.setContentsMargins(20, 20, 20, 20)

        self.main_layout.addWidget(self.content_widget)

        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        layout = self.content_layout  # Use content layout instead of main layout

        # Header
        header_card = ShadcnCard()

        title = ShadcnLabel("Shadcn-inspired PyQt6 GUI", "heading")
        subtitle = ShadcnLabel(
            "Modern desktop application with clean, minimal design", "subheading"
        )

        # Theme selector
        theme_layout = QHBoxLayout()
        theme_label = ShadcnLabel("Theme:")
        self.theme_combo = QComboBox()
        from styles import style_manager

        self.theme_combo.addItems(style_manager.get_available_themes())
        self.theme_combo.currentTextChanged.connect(self.on_theme_changed)

        # Dark mode toggle button
        self.dark_mode_btn = PrimaryButton("Dark Mode")
        self.dark_mode_btn.clicked.connect(self.on_dark_mode_toggle)

        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(self.theme_combo)
        theme_layout.addWidget(self.dark_mode_btn)
        theme_layout.addStretch()

        # Add widgets directly to card layout
        header_card.add_widget(title)
        header_card.add_widget(subtitle)
        header_card._layout.addLayout(theme_layout)

        layout.addWidget(header_card)

        # Buttons section
        buttons_group = QGroupBox("Buttons")
        buttons_layout = QHBoxLayout(buttons_group)
        buttons_layout.setSpacing(8)

        primary_btn = PrimaryButton("Primary")
        secondary_btn = SecondaryButton("Secondary")
        outline_btn = OutlineButton("Outline")
        ghost_btn = GhostButton("Ghost")

        buttons_layout.addWidget(primary_btn)
        buttons_layout.addWidget(secondary_btn)
        buttons_layout.addWidget(outline_btn)
        buttons_layout.addWidget(ghost_btn)
        buttons_layout.addStretch()

        layout.addWidget(buttons_group)

        # Form section
        form_group = QGroupBox("Form Elements")
        form_layout = QVBoxLayout(form_group)
        form_layout.setSpacing(12)

        # Input field
        input_layout = QVBoxLayout()
        input_label = ShadcnLabel("Name:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name...")
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.name_input)
        form_layout.addLayout(input_layout)

        # Text area
        text_layout = QVBoxLayout()
        text_label = ShadcnLabel("Description:")
        self.description_text = QTextEdit()
        self.description_text.setPlaceholderText("Enter a description...")
        self.description_text.setMaximumHeight(80)
        text_layout.addWidget(text_label)
        text_layout.addWidget(self.description_text)
        form_layout.addLayout(text_layout)

        # Combo box
        combo_layout = QVBoxLayout()
        combo_label = ShadcnLabel("Category:")
        self.category_combo = QComboBox()
        self.category_combo.addItems(["Option 1", "Option 2", "Option 3", "Option 4"])
        combo_layout.addWidget(combo_label)
        combo_layout.addWidget(self.category_combo)
        form_layout.addLayout(combo_layout)

        # Checkboxes and radio buttons
        controls_layout = QHBoxLayout()

        # Checkboxes
        checkbox_group = QVBoxLayout()
        checkbox_group.addWidget(ShadcnLabel("Preferences:"))
        self.checkbox1 = QCheckBox("Option A")
        self.checkbox2 = QCheckBox("Option B")
        self.checkbox3 = QCheckBox("Option C")
        checkbox_group.addWidget(self.checkbox1)
        checkbox_group.addWidget(self.checkbox2)
        checkbox_group.addWidget(self.checkbox3)
        controls_layout.addLayout(checkbox_group)

        # Radio buttons
        radio_group = QVBoxLayout()
        radio_group.addWidget(ShadcnLabel("Choice:"))
        self.radio1 = QRadioButton("Choice 1")
        self.radio2 = QRadioButton("Choice 2")
        self.radio3 = QRadioButton("Choice 3")
        radio_group.addWidget(self.radio1)
        radio_group.addWidget(self.radio2)
        radio_group.addWidget(self.radio3)
        controls_layout.addLayout(radio_group)

        controls_layout.addStretch()
        form_layout.addLayout(controls_layout)

        layout.addWidget(form_group)

        # Progress and slider section
        progress_group = QGroupBox("Progress & Controls")
        progress_layout = QVBoxLayout(progress_group)

        # Slider
        slider_layout = QHBoxLayout()
        slider_label = ShadcnLabel("Value:")
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.update_progress)
        slider_layout.addWidget(slider_label)
        slider_layout.addWidget(self.slider)
        progress_layout.addLayout(slider_layout)

        # Progress bar
        progress_layout.addWidget(ShadcnLabel("Progress:"))
        self.progress_bar = ShadcnProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(50)
        progress_layout.addWidget(self.progress_bar)

        layout.addWidget(progress_group)

        # Connect signals
        primary_btn.clicked.connect(self.on_primary_clicked)
        secondary_btn.clicked.connect(self.on_secondary_clicked)

    def apply_styles(self):
        # Styles are applied globally via the style manager
        pass

    def refresh_styling(self):
        """Refresh the styling of this window and all its children"""
        # Update and repaint
        self.update()
        self.repaint()
        for child in self.findChildren(QWidget):
            child.update()
            child.repaint()

        # Also refresh title bar
        if hasattr(self, "title_bar"):
            self.title_bar.update()
            self.title_bar.repaint()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def on_primary_clicked(self):
        print("Primary button clicked!")

    def on_secondary_clicked(self):
        print("Secondary button clicked!")

    def on_theme_changed(self, theme_name):
        """Handle theme selection change"""
        from styles import style_manager

        style_manager.switch_theme(theme_name)
        # Refresh styling
        self.refresh_styling()

    def on_dark_mode_toggle(self):
        """Toggle dark mode on and off"""
        from styles import style_manager

        # Toggle dark mode
        style_manager.toggle_dark_mode()

        # Update button text based on current mode
        if style_manager.is_dark_mode():
            self.dark_mode_btn.setText("Light Mode")
        else:
            self.dark_mode_btn.setText("Dark Mode")

        # Refresh styling
        self.refresh_styling()


def main():
    import os  # noqa: F401

    app = QApplication(sys.argv)

    # Try to set a style that supports theming
    app.setStyle("Fusion")

    # Set application-wide font
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    # Apply theme
    from styles import style_manager

    style_manager.set_application(app)
    style_manager.apply_theme("neutral")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
