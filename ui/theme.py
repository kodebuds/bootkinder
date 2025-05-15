"""
Theme module containing color definitions and styling constants.
Based on the palette: https://coolors.co/palette/cb997e-eddcd2-fff1e6-f0efeb-ddbea9-a5a58d-b7b7a4
"""
from typing import Dict
import sys
import ctypes
import darkdetect
from tkinter import ttk

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
    def get_widget_styles(cls) -> Dict[str, Dict[str, str]]:
        """Returns predefined widget styles using the theme colors"""
        return {
            "primary_button": {
                "background": cls.PRIMARY,
                "foreground": cls.BACKGROUND,
                "activebackground": BEAVER,
                "activeforeground": cls.BACKGROUND,
            },
            "secondary_button": {
                "background": cls.SECONDARY,
                "foreground": cls.BACKGROUND,
                "activebackground": ARTICHOKE,
                "activeforeground": cls.BACKGROUND,
            },
            "frame": {
                "background": cls.BACKGROUND,
            },
            "label": {
                "background": cls.BACKGROUND,
                "foreground": cls.TEXT_PRIMARY,
            },
            "entry": {
                "background": cls.SURFACE,
                "foreground": cls.TEXT_PRIMARY,
                "insertbackground": cls.TEXT_PRIMARY,
            }
        }

    @classmethod
    def set_window_dark_title_bar(cls, window, dark_mode: bool = True) -> bool:
        """
        Set the Windows title bar to dark/light mode with proper window refresh
        
        Args:
            window: The tkinter window/root instance
            dark_mode: Boolean indicating dark (True) or light (False) mode
        
        Returns:
            bool: True if successful, False otherwise
        """
        if not sys.platform.startswith('win'):
            return False
            
        try:
            # Force window update before making changes
            window.update()
            
            # Windows dark mode constant
            DWMWA_USE_IMMERSIVE_DARK_MODE = 20
            
            # Get window handle
            hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
            
            # Prepare dark mode value (2 for dark, 0 for light)
            value = ctypes.c_int(2 if dark_mode else 0)
            
            # Set the window attribute
            result = ctypes.windll.dwmapi.DwmSetWindowAttribute(
                hwnd,
                DWMWA_USE_IMMERSIVE_DARK_MODE,
                ctypes.byref(value),
                ctypes.sizeof(value)
            )
            
            if result == 0:
                # Refresh the window appearance
                window.iconify()    # minimize
                window.deiconify() # restore
                window.lift()      # bring to front
                window.focus()     # set focus
                
                return True
                
            return False
            
        except Exception as e:
            print(f"Failed to set title bar theme: {e}")
            return False

    @classmethod
    def style_widget(cls, widget, style_name: str) -> None:
        """
        Apply theme styles to a widget
        
        Args:
            widget: The tkinter widget to style
            style_name: The name of the style to apply from get_widget_styles()
        """
        styles = cls.get_widget_styles().get(style_name, {})
        for option, value in styles.items():
            try:
                widget[option] = value
            except:
                # Some widgets might not support all style options
                pass

    @classmethod
    def apply_theme(cls, app):
        """
        Applies the theme to the main application window and its widgets.
        Args:
            app: The App instance (with .root as the main Tk window)
        """
        # Set the background color for the main window
        app.root.configure(bg=cls.BACKGROUND)

        # Optionally, set ttk styles for widgets
        style = ttk.Style(app.root)
        style.theme_use('default')
        style.configure('TFrame', background=cls.BACKGROUND)
        style.configure('TLabel', background=cls.BACKGROUND, foreground=cls.TEXT_PRIMARY)
        style.configure('TButton', background=cls.PRIMARY, foreground=cls.BACKGROUND)
        # Add more widget styles as needed

        # Optionally, set dark title bar if on Windows and dark mode is detected
        try:            
            if darkdetect.isDark():
                cls.set_window_dark_title_bar(app.root, dark_mode=True)
        except Exception:
            pass

