from flask_admin.contrib.sqla import ModelView

from app import admin, db

from app.auth.models import User

admin.add_view(ModelView(User, db.session))