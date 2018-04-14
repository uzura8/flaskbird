from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime
from flaskbird.database import db
from flaskbird.models import Member
from flaskbird.forms.member import LoginForm, RegistrationForm, EditProfileForm

member = Blueprint('member', __name__, url_prefix='/member')

@member.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_access = datetime.now()
        db.session.commit()

@member.route('/')
def index():
    return render_template("member/index.html")

@member.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('member.index'))
    form = LoginForm()
    if form.validate_on_submit():
        member = Member.query.filter_by(name=form.name.data).first()
        if member is None or not member.check_password(form.password.data):
            flash('Invalid name or password')
            return redirect(url_for('member.login'))
        login_user(member, remember=form.remember_me.data)
        member.last_login = datetime.now()
        db.session.add(member)
        db.session.commit()
        return redirect(url_for('member.index'))
    return render_template('member/login.html', title='Sign In', form=form)

@member.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('member.login'))

@member.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('member.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        member = Member(name=form.name.data, email=form.email.data)
        member.set_password(form.password.data)
        db.session.add(member)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        login_user(member)
        return redirect(url_for('member.index'))
    return render_template('member/register.html', title='Register', form=form)

@member.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.self_introduction = form.self_introduction.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('member.index'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.self_introduction.data = current_user.self_introduction
    return render_template('member/edit_profile.html', title='Edit Profile',
                           form=form)
