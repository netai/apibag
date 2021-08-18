from flask import render_template


def index():
    site_config = {}
    return render_template('index.html', config=site_config)
