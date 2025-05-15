import tkinter as tk
from tkinter import ttk
from ui.theme import Theme

class Container(ttk.Frame):
    """
    A reusable container widget with two columns, each having a different background color.
    Useful for layouts where you want to visually separate two sections side by side.
    """
    # Class-level flag to ensure styles are only configured once
    _styles_configured = False

    def __init__(self, parent, left_bg=Theme.BACKGROUND, right_bg=Theme.SURFACE, **kwargs):
        """
        Initialize the Container.

        Args:
            parent: The parent tkinter widget.
            left_bg: Background color for the left column.
            right_bg: Background color for the right column.
            **kwargs: Additional keyword arguments for the Frame.
        """
        super().__init__(parent, **kwargs)

        # Use fixed style names for left and right columns
        left_style = "LeftColumn.TFrame"
        right_style = "RightColumn.TFrame"

        # Configure styles only once at the class level
        if not Container._styles_configured:
            style = ttk.Style()
            style.theme_use('clam')
            style.configure(left_style, background=left_bg)
            style.configure(right_style, background=right_bg)
            Container._styles_configured = True

        # Create left column using ttk.Frame and set its style
        self.left_column = ttk.Frame(self, style=left_style)
        self.left_column.grid(row=0, column=0, sticky="nsew")

        # Create right column using ttk.Frame and set its style
        self.right_column = ttk.Frame(self, style=right_style)
        self.right_column.grid(row=0, column=1, sticky="nsew")

        # Configure grid weights to make columns expand equally
        self.columnconfigure(0, weight=12)
        self.columnconfigure(1, weight=88)
        self.rowconfigure(0, weight=1)

    def get_left_column(self):
        """
        Returns the left column frame for adding widgets.
        """
        return self.left_column

    def get_right_column(self):
        """
        Returns the right column frame for adding widgets.
        """
        return self.right_column

