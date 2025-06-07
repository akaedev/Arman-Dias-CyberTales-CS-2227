
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User
from forms import RegisterForm, LoginForm
from datetime import datetime, timedelta
from collections import defaultdict

auth_bp = Blueprint('auth', __name__)


failed_attempts = defaultdict(list)
LOCKOUT_THRESHOLD = 5 #попытки входа
LOCKOUT_DURATION = timedelta(minutes=15)

def get_client_ip():
    return request.headers.get('X-Forwarded-For', request.remote_addr)

def is_locked_out(ip, username):
    key = (ip, username)
    now = datetime.now()
    failed_attempts[key] = [ts for ts in failed_attempts[key] if now - ts < LOCKOUT_DURATION]
    return len(failed_attempts[key]) >= LOCKOUT_THRESHOLD

def record_failed_attempt(ip, username):
    failed_attempts[(ip, username)].append(datetime.now())

#словарь
translations = {
    'login_success': {
        'en': "Login successful",
        'ru': "Вход выполнен успешно",
        'kk': "Сәтті кірдіңіз"
    },
    'invalid_credentials': {
        'en': "Invalid username or password",
        'ru': "Неверное имя пользователя или пароль",
        'kk': "Қате пайдаланушы аты немесе құпиясөз"
    },
    'locked_out': {
        'en': "Too many failed attempts. Try again later.",
        'ru': "Слишком много неудачных попыток. Попробуйте позже.",
        'kk': "Тым көп қате әрекет. Кейінірек қайталап көріңіз."
    },
    'registered': {
        'en': "Registered successfully",
        'ru': "Регистрация прошла успешно",
        'kk': "Тіркеу сәтті өтті"
    },
    'user_exists': {
        'en': "Username already taken",
        'ru': "Имя пользователя уже занято",
        'kk': "Бұл пайдаланушы аты бос емес"
    },
    'logged_out': {
        'en': "Logged out",
        'ru': "Вы вышли из системы",
        'kk': "Сіз жүйеден шықтыңыз"
    }
}

@auth_bp.route('/<lang_code>/register', methods=['GET', 'POST'])
def register_lang(lang_code):
    if lang_code not in ['en', 'ru', 'kk']:
        lang_code = 'en'

    if current_user.is_authenticated:
        return redirect(url_for('index_lang', lang_code=lang_code))

    form = RegisterForm(lang=lang_code)
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash(translations['user_exists'][lang_code])
            return redirect(url_for('auth.register_lang', lang_code=lang_code))

        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(translations['registered'][lang_code])
        return redirect(url_for('auth.login_lang', lang_code=lang_code))

    return render_template(f"{lang_code}/register.html", form=form, lang_code=lang_code)

@auth_bp.route('/<lang_code>/login', methods=['GET', 'POST'])
def login_lang(lang_code):
    if lang_code not in ['en', 'ru', 'kk']:
        lang_code = 'en'

    if current_user.is_authenticated:
        return redirect(url_for('index_lang', lang_code=lang_code))

    form = LoginForm(lang=lang_code)
    client_ip = get_client_ip()
    username_input = form.username.data.strip() if form.username.data else ''

    if form.validate_on_submit():
        if is_locked_out(client_ip, username_input):
            flash(translations['locked_out'][lang_code])
            return redirect(url_for('auth.login_lang', lang_code=lang_code))

        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash(translations['login_success'][lang_code])
            return redirect(url_for('index_lang', lang_code=lang_code))
        else:
            flash(translations['invalid_credentials'][lang_code])
            record_failed_attempt(client_ip, username_input)
            return redirect(url_for('auth.login_lang', lang_code=lang_code))

    return render_template(f"{lang_code}/login.html", form=form, lang_code=lang_code)

@auth_bp.route('/logout')
@login_required
def logout():
    lang_code = session.get("lang", "en")
    logout_user()
    flash(translations['logged_out'][lang_code])
    return redirect(url_for('auth.login_lang', lang_code=lang_code))


@auth_bp.route('/<lang_code>/logout')
@login_required
def logout_lang(lang_code):
    if lang_code not in ['en', 'ru', 'kk']:
        lang_code = 'en'

    logout_user()
    flash(translations['logged_out'][lang_code])
    return redirect(url_for('auth.login_lang', lang_code=lang_code))
