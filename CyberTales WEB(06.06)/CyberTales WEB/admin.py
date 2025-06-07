from flask import Blueprint, render_template, request, redirect, url_for, session, abort
from models import db, QuizQuestion
from forms import QuestionForm

admin_bp = Blueprint('admin', __name__)

@admin_bp.before_request
def require_admin():
    if not session.get('is_admin'):
        abort(403)

@admin_bp.route('/admin', methods=['GET', 'POST'])
def dashboard():
    form = QuestionForm()
    if form.validate_on_submit():
        new_q = QuizQuestion(
            text=form.text.data,
            options=[form.opt1.data, form.opt2.data, form.opt3.data],
            correct=form.correct.data,
            explanation=form.explanation.data
        )
        db.session.add(new_q)
        db.session.commit()
        return redirect(url_for('admin.dashboard'))

    questions = QuizQuestion.query.all()
    return render_template('admin_dashboard.html', form=form, questions=questions)

@admin_bp.route('/admin/delete/<int:id>')
def delete_question(id):
    db.session.delete(QuizQuestion.query.get_or_404(id))
    db.session.commit()
    return redirect(url_for('admin.dashboard'))
