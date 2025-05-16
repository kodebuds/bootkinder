import tkinter as tk
from tkinter import ttk
from ui.theme import Theme

class Container(ttk.Frame):
    """
    A flexible container widget that supports any number of columns or rows, inspired by Bootstrap's grid system.
    Allows custom width/height ratios, background colors, and per-cell padding.
    """
    _styles_configured = set()  # Track which styles have been configured

    def __init__(self, parent, grid_size=2, weights=None, bgs=None, paddings=None, direction="column", **kwargs):
        """
        Initialize the Container.

        Args:
            parent: The parent tkinter widget.
            grid_size: Number of columns/rows to create (default 2).
            weights: List of grid weights for each column/row (default: equal weights).
            bgs: List of background colors for each column/row (default: theme colors).
            paddings: List of paddings (int/tuple per column/row) or single int/tuple for all.
            direction: "column" (default) for horizontal, "row" for vertical stacking.
            **kwargs: Additional keyword arguments for the Frame.
        """
        super().__init__(parent, **kwargs)

        # Set default weights and backgrounds if not provided
        if weights is None:
            weights = [1] * grid_size  # Equal weights if not specified
        if bgs is None:
            # Default backgrounds: alternate between BACKGROUND and SURFACE
            bgs = [Theme.BACKGROUND, Theme.SURFACE] * (grid_size // 2 + 1)

        # Handle paddings: allow single value or list
        if paddings is None:
            paddings = [0] * grid_size  # Default no padding
        elif isinstance(paddings, (int, tuple)):
            paddings = [paddings] * grid_size  # Apply same padding to all
        elif isinstance(paddings, list):
            if len(paddings) < grid_size:
                paddings = (paddings * grid_size)[:grid_size]

        self.columns = []  # Store references to frames (columns or rows)
        style = ttk.Style()
        style.theme_use('clam')

        for i in range(grid_size):
            style_name = f"Column{i}.TFrame"
            if style_name not in Container._styles_configured:
                style.configure(style_name, background=bgs[i % len(bgs)])
                Container._styles_configured.add(style_name)
            # Create the frame with individual padding
            col = ttk.Frame(self, style=style_name, padding=paddings[i])
            if direction == "column":
                col.grid(row=0, column=i, sticky="nsew")
                self.columnconfigure(i, weight=weights[i % len(weights)])
            else:  # direction == "row"
                col.grid(row=i, column=0, sticky="nsew")
                self.rowconfigure(i, weight=weights[i % len(weights)])
            self.columns.append(col)
        if direction == "column":
            self.rowconfigure(0, weight=1)
        else:
            self.columnconfigure(0, weight=1)

    def get_column(self, idx):
        """
        Returns the frame for the specified column/row index.
        Args:
            idx: The column/row index (0-based).
        Returns:
            ttk.Frame: The frame for the column/row.
        """
        return self.columns[idx]

    def get_columns(self):
        """
        Returns a list of all column/row frames.
        Returns:
            list: List of ttk.Frame objects for each column/row.
        """
        return self.columns

