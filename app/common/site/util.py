from flask import url_for

def config_js():
    return {
        'BASE_URL': url_for('site.index'),
        'FBD_SITE_NAME': 'FlaskBird',
    }
