from flask_restful import Resource 

from app.auth.models import User

class UsersAPI(Resource):
    def get(self):
        users = []
        for user in User.query.all():
            users.append(
                {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email
                }
            )
        return users