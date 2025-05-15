# Bootstrap-Inspired Flexible Container for Tkinter

This documentation describes a reusable, Bootstrap-inspired `Container` widget for Tkinter, designed to simplify responsive and flexible column layouts in your Python GUI applications.

## Overview

The `Container` class allows you to create layouts with any number of columns, each with customizable width ratios and background colors, similar to the Bootstrap grid system. This makes it easy to build modern, visually organized interfaces in Tkinter.

## Features
- **Flexible Columns:** Specify any number of columns (2, 3, 4, etc.).
- **Custom Width Ratios:** Use a list of weights to control the relative width of each column (e.g., `[3, 9]` for a 2-column 3:9 split).
- **Custom Backgrounds:** Optionally set background colors for each column.
- **Easy Widget Placement:** Access each column as a frame to add your own widgets.

## Usage

### Import
```python
from ui.widget.containers import Container
```

### Creating a Container
```python
# 2 columns, 3:9 ratio
container = Container(parent, columns=2, weights=[3, 9])
container.pack(fill=tk.BOTH, expand=True)

# 3 columns, equal width
container = Container(parent, columns=3)

# 4 columns, custom ratios and backgrounds
container = Container(parent, columns=4, weights=[2, 3, 4, 3], bgs=["#fff", "#eee", "#ddd", "#ccc"])
```

### Adding Widgets to Columns
```python
# Access columns by index (0-based)
left_col = container.get_column(0)
right_col = container.get_column(1)

# Add widgets to columns
label1 = ttk.Label(left_col, text="Left")
label1.pack()
label2 = ttk.Label(right_col, text="Right")
label2.pack()
```

### Access All Columns
```python
columns = container.get_columns()
for idx, col in enumerate(columns):
    ttk.Label(col, text=f"Column {idx+1}").pack()
```

## Example in a Tkinter App
```python
import tkinter as tk
from tkinter import ttk
from ui.widget.containers import Container

root = tk.Tk()
container = Container(root, columns=3, weights=[2, 5, 5])
container.pack(fill=tk.BOTH, expand=True)

# Add widgets to each column
for idx, col in enumerate(container.get_columns()):
    ttk.Label(col, text=f"Column {idx+1}").pack(padx=10, pady=10)

root.mainloop()
```

## API Reference

### `Container(parent, columns=2, weights=None, bgs=None, **kwargs)`
- **parent:** Parent Tkinter widget.
- **columns:** Number of columns (default: 2).
- **weights:** List of grid weights for each column (default: equal weights).
- **bgs:** List of background colors for each column (default: alternates theme colors).
- **kwargs:** Additional arguments for `ttk.Frame`.

#### Methods
- **get_column(idx):** Returns the frame for the specified column index.
- **get_columns():** Returns a list of all column frames.

## Notes
- The container uses `ttk.Frame` for each column, so you can use any Tkinter or ttk widgets inside.
- The style system is robust and avoids style name conflicts.
- Inspired by Bootstrap's grid system for easy, responsive layouts.

---
For more details, see the source code in `ui/widget/containers.py`.
