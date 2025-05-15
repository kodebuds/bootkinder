from typing import Dict
import sys
import ctypes
import darkdetect
from tkinter import ttk
import tkinter as tk  # Import the main tkinter module

# Color Constants
BEAVER = "#CB997E"
CHAMPAGNE_PINK = "#EDDCD2"
MISTY_ROSE = "#FFF1E6"
PLATINUM = "#F0EFEB"
PALE_TAUPE = "#DDBEA9"
ARTICHOKE = "#A5A58D"
SILVER_CHALICE = "#B7B7A4"

class Theme:
    """Theme class containing color schemes and styling configurations"""

    # Main color scheme 
    PRIMARY = BEAVER
    SECONDARY = ARTICHOKE
    BACKGROUND = MISTY_ROSE
    SURFACE = PLATINUM
    ACCENT = PALE_TAUPE

    # Text colors 
    TEXT_PRIMARY = "#2B2B2B"
    TEXT_SECONDARY = "#4A4A4A"
    TEXT_DISABLED = "#808080"

    # Functional colors
    SUCCESS = "#4CAF50"
    WARNING = "#FFA726"
    ERROR = "#F44336"
    INFO = "#2196F3"

    @classmethod
    def get_color_scheme(cls) -> Dict[str, str]:
        """Returns the complete color scheme as a dictionary"""
        return {
            "primary": cls.PRIMARY,
            "secondary": cls.SECONDARY,
            "background": cls.BACKGROUND,
            "surface": cls.SURFACE,
            "accent": cls.ACCENT,
            "text_primary": cls.TEXT_PRIMARY,
            "text_secondary": cls.TEXT_SECONDARY,
            "text_disabled": cls.TEXT_DISABLED
        }

    @classmethod
    def get_widget_styles(cls) -> Dict[str, Dict[str, dict]]:
        """Returns predefined base styles for ttk widgets using theme colors"""
        return {
            "TButton": {
                "configure": {
                    "background": cls.PRIMARY,
                    "foreground": cls.BACKGROUND,
                    "padding": 6,
                    "font": ("Arial", 10)
                },
                "map": {
                    "background": [("active", BEAVER), ("pressed", BEAVER)],
                    "foreground": [("active", cls.BACKGROUND), ("pressed", cls.BACKGROUND)]
                }
            },
            "Secondary.TButton": {  # Example of a custom style
                "configure": {
                    "background": cls.SECONDARY,
                    "foreground": cls.BACKGROUND,
                    "padding": 6,
                    "font": ("Arial", 10)
                },
                "map": {
                    "background": [("active", ARTICHOKE), ("pressed", ARTICHOKE)],
                    "foreground": [("active", cls.BACKGROUND), ("pressed", cls.BACKGROUND)]
                }
            },
            "TFrame": {
                "configure": {"background": cls.BACKGROUND}
            },
            "TLabel": {
                "configure": {"background": cls.BACKGROUND, "foreground": cls.TEXT_PRIMARY, "padding": 4}
            },
            "Header.TLabel": {  # Example of a custom label style
                "configure": {"font": ("Arial", 14, "bold"), "foreground": cls.PRIMARY}
            },
            "TEntry": {
                "configure": {"background": cls.SURFACE, "foreground": cls.TEXT_PRIMARY, "insertcolor": cls.TEXT_PRIMARY, "padding": 5}
            },
            "TCombobox": {
                "configure": {"background": cls.SURFACE, "foreground": cls.TEXT_PRIMARY, "padding": 5},
                "map": {"background": [("readonly", cls.SURFACE)]} # Ensure consistent background in readonly state
            },
            "TCheckbutton": {
                "configure": {"background": cls.BACKGROUND, "foreground": cls.TEXT_PRIMARY, "padding": 4}
            },
            "TRadiobutton": {
                "configure": {"background": cls.BACKGROUND, "foreground": cls.TEXT_PRIMARY, "padding": 4}
            },
            "TProgressbar": {
                "configure": {"background": cls.ACCENT, "troughcolor": cls.SURFACE}
            },
            "Treeview": {
                "configure": {"background": cls.SURFACE, "foreground": cls.TEXT_PRIMARY}
            },
            "Treeview.Heading": {
                "configure": {"background": cls.SECONDARY, "foreground": cls.BACKGROUND, "font": ("Arial", 10, "bold"), "padding": 4}
            }
            # Add styles for other ttk widgets as needed (e.g., TScale, etc.)
        }

    @classmethod
    def set_window_dark_title_bar(cls, window, dark_mode: bool = True) -> bool:
        """
        Attempts to set the Windows title bar to dark or light mode for the given Tkinter window.
        This enhances the application's appearance to match the system's dark/light theme.

        Args:
            window: The tkinter window/root instance to modify.
            dark_mode: Boolean indicating whether to use dark mode (True) or light mode (False).

        Returns:
            bool: True if the title bar theme was set successfully, False otherwise.
        """
        if not sys.platform.startswith('win'):
            return False

        try:
            # Ensure the window is updated before changing the title bar appearance
            window.update()

            # Windows constant for immersive dark mode attribute
            DWMWA_USE_IMMERSIVE_DARK_MODE = 20

            # Retrieve the window handle for the Tkinter window
            hwnd = ctypes.windll.user32.GetParent(window.winfo_id())

            # Set the value for dark or light mode (2 = dark, 0 = light)
            value = ctypes.c_int(2 if dark_mode else 0)

            # Apply the dark/light mode to the window's title bar
            result = ctypes.windll.dwmapi.DwmSetWindowAttribute(
                hwnd,
                DWMWA_USE_IMMERSIVE_DARK_MODE,
                ctypes.byref(value),
                ctypes.sizeof(value)
            )

            if result == 0:
                # Refresh the window to apply the new title bar appearance
                window.iconify()    # Minimize the window
                window.deiconify()  # Restore the window
                window.lift()       # Bring the window to the front
                window.focus()      # Set focus to the window

                return True

            return False

        except Exception as e:
            print(f"Failed to set title bar theme: {e}")
            return False

    @classmethod
    def style_widget(cls, widget, style_name: str) -> None:
        """
        Apply a predefined ttk style to a widget.

        Args:
            widget: The ttk widget to style.
            style_name: The name of the ttk style to apply (e.g., "TButton", "Secondary.TButton").
        """
        widget.configure(style=style_name)

    @classmethod
    def apply_theme(cls, app):
        """
        Applies the theme to the main application window and configures ttk styles.

        Args:
            app: The App instance (with .root as the main Tk window).
        """
        # Set the background color for the main window (standard tkinter)
        app.root.config(bg=cls.BACKGROUND)

        # Create a ttk Style object
        style = ttk.Style(app.root)

        # Set a default theme to build upon (optional, but recommended)
        style.theme_use('clam')  # Or 'alt', 'default', etc.

        # Get the predefined widget styles
        widget_styles = cls.get_widget_styles()

        # Configure ttk styles based on our theme
        for style_name, config in widget_styles.items():
            style.configure(style_name, **config.get("configure", {}))
            style.map(style_name, **config.get("map", {}))

        # Optionally, set dark title bar if on Windows and dark mode is detected
        try:
            if darkdetect.isDark():
                cls.set_window_dark_title_bar(app.root, dark_mode=True)
        except Exception:
            pass
