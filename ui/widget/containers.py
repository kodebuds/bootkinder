import tkinter as tk
from tkinter import ttk
from ui.theme import Theme

class Container(ttk.Frame):
    """
    A flexible container widget that supports any number of columns, inspired by Bootstrap's grid system.
    Allows custom width ratios and background colors for each column.
    """
    _styles_configured = set()  # Track which column styles have been configured

    def __init__(self, parent, columns=2, weights=None, bgs=None, **kwargs):
        """
        Initialize the Container.

        Args:
            parent: The parent tkinter widget.
            columns: Number of columns to create (default 2).
            weights: List of grid weights for each column (default: equal weights).
            bgs: List of background colors for each column (default: theme colors).
            **kwargs: Additional keyword arguments for the Frame.
        """
        super().__init__(parent, **kwargs)

        if weights is None:
            weights = [1] * columns  # Equal weights if not specified
        if bgs is None:
            # Default backgrounds: alternate between BACKGROUND and SURFACE
            bgs = [Theme.BACKGROUND if i % 2 == 0 else Theme.SURFACE for i in range(columns)]

        self.columns = []  # Store references to column frames
        style = ttk.Style()
        style.theme_use('clam')

        for i in range(columns):
            # Use a safe style name for each column (no color codes)
            style_name = f"Column{i}.TFrame"
            if style_name not in Container._styles_configured:
                style.configure(style_name, background=bgs[i % len(bgs)])
                Container._styles_configured.add(style_name)
            # Create the column frame
            col = ttk.Frame(self, style=style_name)
            col.grid(row=0, column=i, sticky="nsew")
            self.columns.append(col)
            self.columnconfigure(i, weight=weights[i % len(weights)])
        self.rowconfigure(0, weight=1)

    def get_column(self, idx):
        """
        Returns the frame for the specified column index.
        Args:
            idx: The column index (0-based).
        Returns:
            ttk.Frame: The frame for the column.
        """
        return self.columns[idx]

    def get_columns(self):
        """
        Returns a list of all column frames.
        Returns:
            list: List of ttk.Frame objects for each column.
        """
        return self.columns

