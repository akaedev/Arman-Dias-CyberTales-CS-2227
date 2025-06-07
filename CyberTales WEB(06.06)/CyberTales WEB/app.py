from flask import Flask, render_template, jsonify, redirect, url_for, request, session
from flask_login import LoginManager, login_required, current_user
from flask_wtf import CSRFProtect
from models import db, QuizQuestion, User
from auth import auth_bp
from admin import admin_bp
import os

app = Flask(__name__)
app.secret_key = 'ubfenUIUinwdUIwdiua46728939bHFUFIEddubaiwneuifninoBIEF29942'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
csrf = CSRFProtect(app)

#авторизация
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.unauthorized_handler
def handle_needs_login():
    lang = session.get('lang', 'en')  # по умолчанию английский
    return redirect(url_for('auth.login_lang', lang_code=lang))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('index_lang', lang_code='en'))

@app.route('/<lang_code>/')
def index_lang(lang_code):
    if lang_code not in ['en', 'ru', 'kk']:
        lang_code = 'en'
    session['lang'] = lang_code
    return render_template(f"{lang_code}/index.html", lang_code=lang_code)


#модуль новеллы
@app.route('/<lang_code>/game')
@login_required
def game_lang(lang_code):
    if lang_code not in ['en', 'ru', 'kk']:
        lang_code = 'ru'
    session['lang'] = lang_code
    return render_template(f"{lang_code}/CyberTales.html", lang_code=lang_code)


#модуль теории
@app.route('/<lang_code>/cyber-hygiene')
@login_required
def cyber_hygiene_lang(lang_code):
    if lang_code not in ['en', 'ru', 'kk']:
        lang_code = 'en'
    session['lang'] = lang_code
    return render_template(f"{lang_code}/cyber_hygiene.html", lang_code=lang_code)


#модуль куиз
@app.route('/<lang_code>/cyber-hygiene-quiz')
@login_required
def cyber_hygiene_quiz_lang(lang_code):
    if lang_code not in ['en', 'ru', 'kk']:
        lang_code = 'en'
    session['lang'] = lang_code
    return render_template(f"{lang_code}/cyber_hygiene_quiz.html", lang_code=lang_code)

@app.route('/<lang_code>/api/quiz-questions')
@login_required
def api_quiz_questions(lang_code):
    if lang_code not in ['en', 'ru', 'kk']:
        lang_code = 'en'

    questions = QuizQuestion.query.all()

    def format_question(q):
        return {
            "id": q.id,
            "text": getattr(q, f"text_{lang_code}"),
            "options": getattr(q, f"options_{lang_code}"),
            "correct": q.correct,
            "explanation": getattr(q, f"explanation_{lang_code}")
        }

    return jsonify([format_question(q) for q in questions])


#модуль о пароле
@app.route('/<lang_code>/password-tools')
@login_required
def password_tools_lang(lang_code):
    if lang_code not in ['en', 'ru', 'kk']:
        lang_code = 'en'
    session['lang'] = lang_code
    return render_template(f"{lang_code}/password_tools.html", lang_code=lang_code)

#путь к сертификатам
cert_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cert.pem'))
key_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'key.pem'))

if __name__ == "__main__":
    app.run(ssl_context=(cert_path, key_path), host='127.0.0.1', port=5000, debug=False)
