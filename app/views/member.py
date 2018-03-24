from flask import Blueprint, render_template
#from flask.ext.login import login_required, current_user

member = Blueprint('member', __name__, url_prefix='/member')

@member.route('/')
def index():
    return render_template("member.html")

#@member.route('/login')
#def login():
#    pass
#
#@member.route('/logout')
#def logout():
#    pass
#
#@member.route('/home')
#@login_required
#def home():
#    return render_template("home.html")
