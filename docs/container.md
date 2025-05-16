# Bootstrap-Inspired Flexible Container for Tkinter

This documentation describes a reusable, Bootstrap-inspired `Container` widget for Tkinter, designed to simplify responsive and flexible column and row layouts in your Python GUI applications.

## Overview

The `Container` class allows you to create layouts with any number of columns **or rows**, each with customizable width/height ratios, background colors, and per-cell padding, similar to the Bootstrap grid system. This makes it easy to build modern, visually organized interfaces in Tkinter.

## Features
- **Flexible Columns or Rows:** Specify any number of columns (horizontal) or rows (vertical) using the `direction` parameter.
- **Custom Width/Height Ratios:** Use a list of weights to control the relative width of each column or height of each row (e.g., `[3, 9]` for a 2-column 3:9 split).
- **Custom Backgrounds:** Optionally set background colors for each column or row.
- **Per-Cell Padding:** Set padding for all columns/rows or individually per cell.
- **Easy Widget Placement:** Access each column or row as a frame to add your own widgets.

## Usage

### Import
```python
from ui.widget.containers import Container
```

### Creating a Container (Columns or Rows)
```python
# 2 columns, 3:9 ratio (default is horizontal/columns)
container = Container(parent, grid_size=2, weights=[3, 9])
container.pack(fill=tk.BOTH, expand=True)

# 3 columns, equal width
container = Container(parent, grid_size=3)

# 4 columns, custom ratios and backgrounds
container = Container(parent, grid_size=4, weights=[2, 3, 4, 3], bgs=["#fff", "#eee", "#ddd", "#ccc"])

# 3 rows, vertical stacking (direction="row")
container = Container(parent, grid_size=3, direction="row")
```

### Adding Widgets to Columns or Rows
```python
# Access columns or rows by index (0-based)
first = container.get_column(0)
second = container.get_column(1)

# Add widgets to columns/rows
label1 = ttk.Label(first, text="First")
label1.pack()
label2 = ttk.Label(second, text="Second")
label2.pack()
```

### Access All Columns or Rows
```python
columns = container.get_columns()
for idx, col in enumerate(columns):
    ttk.Label(col, text=f"Column/Row {idx+1}").pack()
```

### Using Padding

You can specify padding for all columns/rows or for each individually:

```python
# Same padding for all columns/rows (e.g., 10 pixels)
container = Container(parent, grid_size=3, paddings=10)

# Different paddings for each column/row
container = Container(parent, grid_size=3, paddings=[5, (10, 20), 0])
```
- Padding can be an integer (applied to all sides), a tuple (e.g., `(left, top, right, bottom)`), or a list of such values for per-column/row control.

## Example: Columns and Rows in a Tkinter App
```python
import tkinter as tk
from tkinter import ttk
from ui.widget.containers import Container

root = tk.Tk()
root.title("Container Example")

# Horizontal layout (columns)
container1 = Container(root, grid_size=3, paddings=[10, (20, 10), 5])
container1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
for idx, col in enumerate(container1.get_columns()):
    ttk.Label(col, text=f"Column {idx+1}").pack(padx=10, pady=10)

# Vertical layout (rows)
container2 = Container(root, grid_size=3, paddings=[8, (5, 15), 0], direction="row")
container2.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
for idx, row in enumerate(container2.get_columns()):
    ttk.Label(row, text=f"Row {idx+1}").pack(padx=10, pady=10)

root.mainloop()
```

## Example: Nested Layout with Different Widgets
```python
import tkinter as tk
from tkinter import ttk
from ui.widget.containers import Container

root = tk.Tk()
root.title("Nested Container Layout Example")

# Main container with 2 columns
main_container = Container(root, grid_size=2, paddings=10)
main_container.pack(fill="both", expand=True, padx=20, pady=20)

# Left column: 3 rows, each with a different widget
left_col = main_container.get_column(0)
left_rows = Container(left_col, grid_size=3, paddings=5, direction="row")
left_rows.pack(fill="both", expand=True)
ttk.Label(left_rows.get_column(0), text="Left Col - Row 1: Label").pack(padx=5, pady=5)
ttk.Entry(left_rows.get_column(1)).pack(padx=5, pady=5)
ttk.Button(left_rows.get_column(2), text="Left Col - Row 3: Button").pack(padx=5, pady=5)

# Right column: 5 rows, each with a different widget
right_col = main_container.get_column(1)
right_rows = Container(right_col, grid_size=5, paddings=5, direction="row")
right_rows.pack(fill="both", expand=True)
ttk.Label(right_rows.get_column(0), text="Right Col - Row 1: Label").pack(padx=5, pady=5)
ttk.Entry(right_rows.get_column(1)).pack(padx=5, pady=5)
ttk.Button(right_rows.get_column(2), text="Right Col - Row 3: Button").pack(padx=5, pady=5)
ttk.Combobox(right_rows.get_column(3), values=["Option 1", "Option 2"]).pack(padx=5, pady=5)
ttk.Checkbutton(right_rows.get_column(4), text="Right Col - Row 5: Check").pack(padx=5, pady=5)

root.mainloop()
```

## API Reference

### `Container(parent, grid_size=2, weights=None, bgs=None, paddings=None, direction="column", **kwargs)`
- **parent:** Parent Tkinter widget.
- **grid_size:** Number of columns or rows (default: 2).
- **weights:** List of grid weights for each column/row (default: equal weights).
- **bgs:** List of background colors for each column/row (default: alternates theme colors).
- **paddings:** Padding for columns/rows. Can be a single int/tuple (applied to all) or a list for per-column/row padding.
- **direction:** `"column"` (default, horizontal) or `"row"` (vertical stacking).
- **kwargs:** Additional arguments for `ttk.Frame`.

#### Methods
- **get_column(idx):** Returns the frame for the specified column/row index.
- **get_columns():** Returns a list of all column/row frames.

## Notes
- The container uses `ttk.Frame` for each column or row, so you can use any Tkinter or ttk widgets inside.
- The style system is robust and avoids style name conflicts.
- Inspired by Bootstrap's grid system for easy, responsive layouts.
- Padding is handled via the `padding` option of `ttk.Frame` for each column/row.
- Always add meaningful comments in your code for maintainability.

---
For more details, see the source code in `ui/widget/containers.py`.
