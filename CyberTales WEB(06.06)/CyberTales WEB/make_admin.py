from models import db, User

user = User.query.filter_by(username='arman').first()

user.is_admin = True
db.session.commit()
