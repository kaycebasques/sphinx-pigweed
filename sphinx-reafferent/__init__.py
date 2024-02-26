import os

def setup(app):  # TODO: Type hints
    """TODO: Description"""
    app.add_html_theme('sphinx-reafferent', os.path.abspath(os.path.dirname(__file__)))
