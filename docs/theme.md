# Theme System for Tkinter Bootstrap-Inspired UI

This documentation describes the `Theme` class used in the Bootkinder project to provide a modern, consistent look and feel for Tkinter applications, including color schemes and widget styling.

## Overview

The `Theme` class centralizes color definitions and ttk style configurations, making it easy to apply a unified theme across your application. It also supports dark mode detection and Windows title bar theming.

## Features
- **Centralized Color Scheme:** All main, accent, and text colors are defined in one place.
- **Predefined Widget Styles:** Easily apply consistent styles to buttons, labels, frames, entries, and more.
- **Dark Mode Support:** Automatically adapts to system dark mode (on Windows).
- **Easy Application:** Apply the theme to your app with a single method call.

## Usage

### Import
```python
from ui.theme import Theme
```

### Applying the Theme
Call `Theme.apply_theme(app)` after creating your main app instance:
```python
app = App()
Theme.apply_theme(app)
```
This will set the background color and configure all ttk widget styles.

### Customizing Widgets
You can apply a specific style to a widget:
```python
Theme.style_widget(my_button, "Secondary.TButton")
```

### Example Styles
- `TButton` (primary button)
- `Secondary.TButton` (secondary button)
- `TFrame`, `TLabel`, `Header.TLabel`, `TEntry`, `TCombobox`, etc.

### Example: Themed Button
```python
import tkinter as tk
from tkinter import ttk
from ui.theme import Theme

root = tk.Tk()
Theme.apply_theme(type('App', (), {'root': root})())
btn = ttk.Button(root, text="Primary", style="TButton")
btn.pack(padx=10, pady=10)
root.mainloop()
```

## API Reference

### `Theme.apply_theme(app)`
- Applies the theme to the main application window and configures ttk styles.

### `Theme.style_widget(widget, style_name)`
- Applies a predefined ttk style to a widget.

### `Theme.get_color_scheme()`
- Returns the color scheme as a dictionary.

### `Theme.get_widget_styles()`
- Returns the widget style configuration dictionary.

## Notes
- The theme is designed to work seamlessly with the Bootstrap-inspired `Container` class.
- You can extend the theme by adding more styles in `get_widget_styles()`.

---
For more details, see the source code in `ui/theme.py`.
