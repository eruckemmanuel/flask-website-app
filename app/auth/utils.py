from werkzeug.security import check_password_hash

from app.auth.models import User


def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return user