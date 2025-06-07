from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


db = SQLAlchemy()
#юзеры в бд
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    failed_attempts = db.Column(db.Integer, default=0)
    locked_until = db.Column(db.DateTime, nullable=True)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#вопросы в бд
class QuizQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_en = db.Column(db.String(255))
    text_ru = db.Column(db.String(255))
    text_kk = db.Column(db.String(255))
    options_en = db.Column(db.PickleType)
    options_ru = db.Column(db.PickleType)
    options_kk = db.Column(db.PickleType)
    correct = db.Column(db.Integer)
    explanation_en = db.Column(db.Text)
    explanation_ru = db.Column(db.Text)
    explanation_kk = db.Column(db.Text)


class QuizAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    score = db.Column(db.Integer)
    total = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
