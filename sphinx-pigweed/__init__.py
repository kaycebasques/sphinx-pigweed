import os

def add_context(app, pagename, templatename, context, doctree):
    context['pw_pagenav_label'] = app.config.pw_pagenav_label
    context['pw_banner_text'] = app.config.pw_banner_text

def setup(app):
    app.add_html_theme('sphinx-pigweed', os.path.abspath(os.path.dirname(__file__)))
    app.add_config_value('pw_pagenav_label', 'Page Contents', 'html', [str])
    app.add_config_value('pw_banner_text', None, 'html', [str])
    app.connect('html-page-context', add_context) 