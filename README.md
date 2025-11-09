# Shadcn-inspired PyQt6 GUI

A modern, clean desktop application built with PyQt6 that mimics the design aesthetic of Shadcn UI components.

## Features

- **Modern Design**: Clean, minimal interface with rounded corners, subtle shadows, and consistent spacing
- **Component Library**: Custom widgets styled to match Shadcn components:
  - Buttons (Primary, Secondary, Outline, Ghost variants)
  - Input fields with focus states
  - Cards with hover effects
  - Form controls (checkboxes, radio buttons, combo boxes)
  - Progress bars and sliders
  - Typography hierarchy
- **Modular Architecture**: Organized into separate packages for maintainability
- **Theme System**: Support for multiple themes (Light/Dark) with easy switching

## Project Structure

```bash
pyqt6-shadcn/
├── main.py                 # Main application entry point
├── test_components.py      # Component tests
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── styles/                # Style management
│   └── __init__.py        # StyleManager for theme application
├── themes/                # Theme definitions
│   └── __init__.py        # Theme classes and ThemeManager
└── widgets/               # Custom widget components
    ├── __init__.py        # Widget package exports
    ├── buttons.py         # Button variants
    ├── cards.py           # Card and label components
    └── progress.py        # Progress bar with dynamic styling
```

## Requirements

- Python 3.8+
- PyQt6

## Installation

1. Clone or download this repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python main.py
```

## Testing

Run the component tests:

```bash
python test_components.py
```

## Architecture

### Theme System

The application uses a flexible theme system with:

- **Abstract Theme Base Class**: Defines the interface for all themes
- **Concrete Theme Implementations**: ShadcnTheme (light) and DarkTheme
- **Theme Manager**: Handles theme switching and application
- **Style Manager**: Applies themes globally to the PyQt6 application

### Widget Components

Custom widgets are organized into focused modules:

- **buttons.py**: Button variants (Primary, Secondary, Outline, Ghost)
- **cards.py**: Card containers and typography components
- **progress.py**: Progress bar with automatic text color switching

### Styling

Styles are defined using Qt Style Sheets (QSS) with:

- Color variables for easy theme customization
- Consistent spacing and typography
- Hover and focus states
- Responsive design elements

## Design Philosophy

This implementation captures the essence of Shadcn's design system:

- **Minimalism**: Clean layouts with ample white space
- **Consistency**: Uniform spacing, typography, and interaction patterns
- **Accessibility**: Clear focus states and hover effects
- **Modularity**: Easy to extend and maintain
