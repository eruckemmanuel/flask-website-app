import logging

from flask import (request, render_template,
                   flash, g, session, redirect, url_for)

# Password encryption helper
#from werkzeug import check_password_hash, generate_password_hash

# Import database object from main app
from app import db

# Models of app module
from app.auth.models import User
from app.auth import auth


logger = logging.getLogger(__name__)

@auth.route('/signin/', methods=['GET', 'POST'])
def sign_in():
    if request.method == "GET":
        logger.debug(request.args)
        return render_template('auth/login.html', data={"name":"Eruck Emmanuel"})
    else:
        data = request.data
        logger.debug(data)
        return redirect('/auth/users/') 
    
    
@auth.route('/users/', methods=['GET', 'POST'])
def users():
    if request.method == "GET":
        users = User.query.all()
        return render_template('auth/users.html', users=users)
    else:
        data = request.form
        user = User(email=data.get('email'), 
                    password=data.get('password'),
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    role=1,
                    status=1)
        
        db.session.add(user)
        db.session.commit()
        
        return redirect('/auth/users/')