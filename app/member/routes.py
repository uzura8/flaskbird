from flask import render_template, request, redirect, url_for, flash, g
from flask_login import current_user, login_user, logout_user, login_required
from flask_babel import _, get_locale
from datetime import datetime
from app import db
from app.member import bp
from app.email import send_password_reset_email
from app.member.models import Member
from app.member.forms import(
    LoginForm,
    RegistrationForm,
    ResetPasswordRequestForm,
    EditProfileForm,
    ResetPasswordForm,
)

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_access = datetime.now()
        db.session.commit()
    g.locale = str(get_locale())

@bp.route('/')
def index():
    return render_template("member/index.html")

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('member.index'))
    form = LoginForm()
    if form.validate_on_submit():
        member = Member.query.filter_by(name=form.name.data).first()
        if member is None or not member.check_password(form.password.data):
            flash(_('Invalid name or password'))
            return redirect(url_for('member.login'))
        login_user(member, remember=form.remember_me.data)
        member.last_login = datetime.now()
        db.session.add(member)
        db.session.commit()
        return redirect(url_for('member.index'))
    return render_template('member/login.html', title='Sign In', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('member.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('member.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        member = Member(name=form.name.data, email=form.email.data)
        member.set_password(form.password.data)
        db.session.add(member)
        db.session.commit()
        flash(_('Congratulations, you are now a registered user!'))
        login_user(member)
        return redirect(url_for('member.index'))
    return render_template('member/register.html', title='Register', form=form)

@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('member.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        member = Member.query.filter_by(email=form.email.data).first()
        if member:
            send_password_reset_email(member)
        flash(_('Check your email for the instructions to reset your password'))
        return redirect(url_for('member.login'))
    return render_template('member/reset_password_request.html',
                           title='Reset Password', form=form)

@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('member.index'))
    member = Member.verify_reset_password_token(token)
    if not member:
        return redirect(url_for('site.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        member.set_password(form.password.data)
        db.session.commit()
        flash(_('Your password has been reset.'))
        return redirect(url_for('member.login'))
    return render_template('member/reset_password.html', form=form)

@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.self_introduction = form.self_introduction.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('member.index'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.self_introduction.data = current_user.self_introduction
    return render_template('member/edit_profile.html', title='Edit Profile',
                           form=form)
