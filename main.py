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
)
from PyQt6.QtCore import Qt
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


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shadcn-inspired PyQt6 GUI")
        self.setMinimumSize(800, 700)  # Increased minimum height
        self.resize(900, 800)  # Set a reasonable default size
        self.setObjectName("MainWindow")  # Add object name for specific styling
        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(20, 20, 20, 20)

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
    app = QApplication(sys.argv)

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
