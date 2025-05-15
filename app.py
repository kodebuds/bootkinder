from ui.layout import App
from ui.theme import Theme

if __name__ == "__main__":
    app = App()
    Theme.apply_theme(app)  # Apply the theme to the app
    app.run()