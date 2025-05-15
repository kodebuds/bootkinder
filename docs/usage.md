# Bootkinder UI Usage Guide

This guide provides practical examples and best practices for using the Bootkinder Bootstrap-inspired Tkinter UI system, including the flexible `Container` and the `Theme` class.

## Getting Started

1. **Install dependencies** (if not already):
   - Tkinter (usually included with Python)
   - `darkdetect` (for dark mode support):
     ```sh
     pip install darkdetect
     ```

2. **Project Structure**
   - Place your UI code in the `ui/` directory.
   - Use `ui/widget/containers.py` for layout and `ui/theme.py` for theming.

## Basic Example

```python
import tkinter as tk
from tkinter import ttk
from ui.layout import App
from ui.theme import Theme

if __name__ == "__main__":
    app = App()
    Theme.apply_theme(app)
    app.run()
```

## Creating Responsive Layouts

```python
from ui.widget.containers import Container

# In your App or window:
container = Container(parent, columns=3, weights=[2, 5, 5])
container.pack(fill=tk.BOTH, expand=True)

# Add widgets to columns
for idx, col in enumerate(container.get_columns()):
    ttk.Label(col, text=f"Column {idx+1}").pack(padx=10, pady=10)
```

## Theming Widgets

```python
from ui.theme import Theme

# Apply a custom style to a widget
Theme.style_widget(my_button, "Secondary.TButton")
```

## Tips
- Use the `weights` argument to control the width ratio of columns (like Bootstrap's grid system).
- Use the `bgs` argument to set custom background colors for columns.
- Always call `Theme.apply_theme(app)` before adding widgets for consistent styling.
- Use `get_column(idx)` or `get_columns()` to access and populate columns.

## Advanced: Customizing the Theme
- Edit `ui/theme.py` to add or modify color schemes and widget styles.
- Add new styles in `get_widget_styles()` and use them via `Theme.style_widget()`.

---
For more, see the full documentation in `docs/container.md` and `docs/theme.md`.
