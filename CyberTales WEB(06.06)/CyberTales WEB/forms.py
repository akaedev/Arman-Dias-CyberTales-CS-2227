
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, IntegerField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, Regexp, ValidationError
from zxcvbn import zxcvbn
from wtforms import HiddenField

#проверка на сложность + 3 языка
def strong_password_check(form, field):
    result = zxcvbn(field.data)
    if result['score'] < 3:
        messages = {
            'en': "Password is too weak. Use a stronger password.",
            'ru': "Пароль слишком слабый. Используйте более надёжный пароль.",
            'kk': "Құпиясөз әлсіз. Күштірек құпиясөзді қолданыңыз."
        }
        lang_code = getattr(form.lang, 'data', 'en')
        raise ValidationError(messages.get(lang_code, messages['en']))
    
class QuestionForm(FlaskForm):
    text = StringField('Question', validators=[InputRequired()])
    opt1 = StringField('Option 1', validators=[InputRequired()])
    opt2 = StringField('Option 2', validators=[InputRequired()])
    opt3 = StringField('Option 3', validators=[InputRequired()])
    correct = IntegerField('Correct Index (0-2)', validators=[InputRequired(), NumberRange(min=0, max=2)])
    explanation = TextAreaField('Explanation', validators=[InputRequired()])
    submit = SubmitField('Add Question')

class RegisterForm(FlaskForm):
    lang = HiddenField()
    username = StringField(validators=[
        InputRequired(),
        Length(min=3, max=30),
        Regexp(r'^[A-Za-z0-9_.-]+$', message="Only letters, numbers, dots, dashes, underscores")
    ])
    password = PasswordField(validators=[
        InputRequired(),
        strong_password_check
    ])
    submit = SubmitField()

    def __init__(self, lang='en', *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.lang.data = lang
        if lang == 'ru':
            self.username.label.text = 'Имя пользователя'
            self.password.label.text = 'Пароль'
            self.submit.label.text = 'Зарегистрироваться'
        elif lang == 'kk':
            self.username.label.text = 'Пайдаланушы аты'
            self.password.label.text = 'Құпиясөз'
            self.submit.label.text = 'Тіркелу'
        else:
            self.username.label.text = 'Username'
            self.password.label.text = 'Password'
            self.submit.label.text = 'Register'

class LoginForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(),
        Regexp(r'^[A-Za-z0-9_.-]+$', message="Invalid characters in username.")
    ])
    password = PasswordField(validators=[InputRequired()])
    remember = BooleanField()
    submit = SubmitField()

    def __init__(self, lang='en', *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        if lang == 'ru':
            self.username.label.text = 'Имя пользователя'
            self.password.label.text = 'Пароль'
            self.remember.label.text = 'Запомнить меня'
            self.submit.label.text = 'Войти'
        elif lang == 'kk':
            self.username.label.text = 'Пайдаланушы аты'
            self.password.label.text = 'Құпиясөз'
            self.remember.label.text = 'Есте сақтау'
            self.submit.label.text = 'Кіру'
        else:
            self.username.label.text = 'Username'
            self.password.label.text = 'Password'
            self.remember.label.text = 'Remember Me'
            self.submit.label.text = 'Login'
