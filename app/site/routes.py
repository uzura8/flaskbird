from flask import render_template
from app.site import bp

@bp.route('/')
def index():
    return render_template('index.html')
