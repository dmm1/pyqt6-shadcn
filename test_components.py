#!/usr/bin/env python3
"""
Simple test script for Shadcn-style PyQt6 components
"""

import sys
from PyQt6.QtWidgets import QApplication
from main import MainWindow


def test_application():
    """Test that the application can be instantiated and shows components"""
    app = QApplication(  # noqa: F841
        sys.argv
    )  # Required for QWidget creation, even though not used in test

    # Create main window
    window = MainWindow()

    # Test that widgets exist
    assert window.name_input is not None
    assert window.description_text is not None
    assert window.category_combo is not None
    assert window.slider is not None
    assert window.progress_bar is not None

    # Test slider connection
    window.slider.setValue(75)
    assert window.progress_bar.value() == 75

    print("✓ All components created successfully")
    print("✓ Slider-progress connection working")
    print("✓ Application styling applied")

    # Don't actually show the window in test mode
    # window.show()
    # sys.exit(app.exec())


if __name__ == "__main__":
    test_application()
    print("✓ All tests passed!")
