import os
import base64
from datetime import datetime
#from werkzeug import secure_filename
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from flask_babel import _
from app import db, NotAcceptableException
from app.common.site.media import upload_image
from app.common.image import Image
from app.site import site_before_request
from . import site_auth_check
from app.member import bp
from app.email import send_password_reset_email
from app.media.models import File, FileBin
from app.member.models import Member
from app.member.forms import(
    LoginForm,
    RegistrationForm,
    ResetPasswordRequestForm,
    EditProfileForm,
    ResetPasswordForm,
)

@bp.before_request
@site_before_request
@site_auth_check
def before_request():
    pass

@bp.route('/')
@login_required
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
    return render_template('member/edit_profile.html', title=_('Edit Profile'),
                           form=form)

@bp.route('/profile/photos', methods=['GET'])
def profile_photos():
    return render_template('member/profile/photos.html',
                            title=_('Profile Photos'))

@bp.route('/profile/photos/upload', methods=['POST'])
@login_required
def profile_photos_upload():
    if 'profile_photo' not in request.files:
        flash(_('File not selected.'))
        return redirect(url_for('member.profile_photos'))
    uploaded = request.files['profile_photo']
    try:
        path, filename = upload_image(uploaded, 'photo', 'm', current_user.id)
        with open(path, 'rb') as imageFile:
            bin_data = base64.b64encode(imageFile.read())
            file_bin = FileBin(
                name=filename,
                bin=bin_data)
            db.session.add(file_bin)
        image = Image(path)
        exifs = image.get_exifs('json')

        if current_user.file_name:
            file_current = File.query.get(current_user.file_name)
            if file_current and not file_current.check_deleted():
                file_current.soft_delete()

        file = File(
            user_type='member',
            name=filename,
            original_name=uploaded.filename,
            type=uploaded.mimetype,
            exif=exifs,
            size=os.stat(path).st_size)
        db.session.add(file)
        current_user.file_name = filename
    except NotAcceptableException:
        flash(_('Uploaded file is not allowed.'))
        return redirect(url_for('member.profile_photos'))
    except Exception:
        db.session.rollback()
        raise
    db.session.commit()
    return redirect(url_for('member.profile_photos'))

@bp.route('/profile/photos/delete', methods=['POST'])
@login_required
def profile_photos_delete():
    file = File.query.get(current_user.file_name)
    if not file or file.check_deleted():
        flash(_('Profile Photo not set.'))
        return redirect(url_for('member.profile_photos'))
    try:
        file.soft_delete()
    except Exception:
        db.session.rollback()
        raise
    current_user.file_name = ''
    db.session.commit()
    flash(_('Profile Photo has been deleted.'))
    return redirect(url_for('member.profile_photos'))

