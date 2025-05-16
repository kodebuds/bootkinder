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

# 2 columns, 3:9 ratio (default is horizontal/columns)
container = Container(parent, grid_size=2, weights=[3, 9])
container.pack(fill=tk.BOTH, expand=True)

# 3 columns, equal width
container = Container(parent, grid_size=3)

# 4 columns, custom ratios and backgrounds
container = Container(parent, grid_size=4, weights=[2, 3, 4, 3], bgs=["#fff", "#eee", "#ddd", "#ccc"])

# 3 rows, vertical stacking (direction="row")
container = Container(parent, grid_size=3, direction="row")

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
- Use the `weights` argument to control the width ratio of columns/rows (like Bootstrap's grid system).
- Use the `bgs` argument to set custom background colors for columns/rows.
- Use the `paddings` argument to set padding for columns/rows.
- Always call `Theme.apply_theme(app)` before adding widgets for consistent styling.
- Use `get_column(idx)` or `get_columns()` to access and populate columns/rows.

## Advanced: Customizing the Theme
- Edit `ui/theme.py` to add or modify color schemes and widget styles.
- Add new styles in `get_widget_styles()` and use them via `Theme.style_widget()`.

## API Reference

### `Container(parent, grid_size=2, weights=None, bgs=None, paddings=None, direction="column", **kwargs)`
- **parent:** Parent Tkinter widget.
- **grid_size:** Number of columns or rows (default: 2).
- **weights:** List of grid weights for each column/row (default: equal weights).
- **bgs:** List of background colors for each column/row (default: alternates theme colors).
- **paddings:** Padding for columns/rows. Can be a single int/tuple (applied to all) or a list for per-column/row padding.
- **direction:** `"column"` (default, horizontal) or `"row"` (vertical stacking).
- **kwargs:** Additional arguments for `ttk.Frame`.

---

For more, see the full documentation in `docs/container.md` and `docs/theme.md`.
