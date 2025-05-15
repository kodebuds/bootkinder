# Copyright (c) 2025 Kodebuds - All rights reserved under the Apache License 2.0.
#             app: The main application instance.

import tkinter as tk
from tkinter import ttk
from ui.widget.containers import Container
from ui.theme import Theme

class App:
    """
    This class creates a basic Tkinter application.  It sets up the main window,
    adds a title, and centers the window on the screen.

    Attributes:
        root (tk.Tk): The main window of the application.
        width (int): The width of the application window.
        height (int): The height of the application window.
    """
    def __init__(self):
        """
        Initializes the App class.  This is the constructor for the class.
        It creates the main window, sets the title, and centers the window.
        """
        self.root = tk.Tk()  # Create the main window.
        self.root.title("Bootkinder")  # Set the title 
        self.width = 1024  # Set the  width of the window
        self.height = 720 # Set the  height of the window

        self._center_window()  # Call the method to center the window
        self._create_layout() # Call the method to create the layout

    def _center_window(self):
        """
        Centers the application window on the screen and sets the minimum window size.

        This method calculates the x and y coordinates to center the window
        based on the screen's width and height, and the application's
        width and height. It then sets the geometry of the window and
        enforces a minimum window size of 1024x720.
        """
        screen_width = self.root.winfo_screenwidth()  # Get the screen width
        screen_height = self.root.winfo_screenheight() # Get the screen height

        x = (screen_width / 2) - (self.width / 2)  # Calculate the x coordinate
        y = (screen_height / 2) - (self.height / 2) # Calculate the y coordinate

        # Set the geometry of the window. The format is "widthxheight+x+y"
        self.root.geometry(f"{self.width}x{self.height}+{int(x)}+{int(y)}")
        self.root.resizable(True, True) # Allow resizing
        self.root.minsize(1024, 720)    # Set minimum window size

    def _create_layout(self):
        """
        Creates the layout for the application. Adds widgets to the main window.
        Demonstrates usage of the flexible Container with 2 columns (3:9 ratio).
        """
        # Create a container with 2 columns, using a 3:9 width ratio
        container = Container(self.root, columns=2, weights=[3, 9])
        container.pack(fill=tk.BOTH, expand=True)

        # Example: Add widgets to each column
        left_col = container.get_column(0)
        right_col = container.get_column(1)

        # Add a label to the left column
        left_label = ttk.Label(left_col, text="Left Column (3/12)")
        left_label.pack(padx=10, pady=10)

        # Add a label to the right column
        right_label = ttk.Label(right_col, text="Right Column (9/12)")
        right_label.pack(padx=10, pady=10)

    def run(self):
        """
        Starts the main loop of the application.  This is required for the
        application to run and respond to user events.
        """
        self.root.mainloop()  # Start the main loop