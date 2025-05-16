import tkinter as tk
from tkinter import ttk
from ui.widget.containers import Container

def test_container_layout():
    """
    Test the Container widget with nested layout:
    - Main container with 2 columns (grid_size=2)
    - Left column: 3 rows, each with a different widget
    - Right column: 5 rows, each with a different widget
    """
    root = tk.Tk()
    root.title("Container Test Layout")

    # Main container with 2 columns
    main_container = Container(root, grid_size=2, paddings=10, weights=[1, 11])
    main_container.pack(fill="both", expand=True, padx=5, pady=5)

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

if __name__ == "__main__":
    test_container_layout()
