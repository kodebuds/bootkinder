import tkinter as tk
import tkinter.ttk as ttk  # Import the themed widgets

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
        self.root = tk.Tk()  # Create the main window.  This is the root window.
        self.root.title("My Tkinter App")  # Set the title of the window
        self.width = 1024  # Set the  width of the window
        self.height = 720 # Set the  height of the window

        self._center_window()  # Call the method to center the window
        self._create_widgets() # Call the method to create the widgets

    def _center_window(self):
        """
        Centers the application window on the screen.

        This method calculates the x and y coordinates to center the window
        based on the screen's width and height, and the application's
        width and height.  It then sets the geometry of the window.
        """
        screen_width = self.root.winfo_screenwidth()  # Get the screen width
        screen_height = self.root.winfo_screenheight() # Get the screen height

        x = (screen_width / 2) - (self.width / 2)  # Calculate the x coordinate
        y = (screen_height / 2) - (self.height / 2) # Calculate the y coordinate

        # Set the geometry of the window.  The format is "widthxheight+x+y"
        self.root.geometry(f"{self.width}x{self.height}+{int(x)}+{int(y)}")
        self.root.resizable(True, True) #  allow resizing

    def _create_widgets(self):
        """
        Creates the widgets for the application.  This method is called during
        initialization to set up the user interface.  For this basic example,
        it adds a label and a button.  You can add more widgets here.
        """
        # Use ttk.Label for a themed label
        label = ttk.Label(self.root, text="Welcome to My Tkinter App!", font=("Arial", 16))
        label.pack(pady=20)  # Use pack layout manager

        # Use ttk.Button for a themed button
        button = ttk.Button(self.root, text="Click Me", command=self._on_button_click)
        button.pack(pady=10)

    def _on_button_click(self):
        """
        This method is called when the button is clicked.  It's an example
        of an event handler.  For now, it just prints a message to the console.
        You can change this to do something more useful.
        """
        print("Button Clicked!")
        # Example of changing label text:
        # self.label.config(text="Button was clicked!") #Removed self.label

    def run(self):
        """
        Starts the main loop of the application.  This is required for the
        application to run and respond to user events.
        """
        self.root.mainloop()  # Start the main loop

if __name__ == "__main__":
    """
    This is the entry point of the script.  It's where the program starts
    executing.  It creates an instance of the App class and then calls the
    run method to start the application.
    """
    app = App()  # Create an instance of the App class
    app.run()  # Start the application
