import logging

from flask import (request, render_template,
                   flash, g, session, redirect, url_for)
from flask_login import (login_required, current_user, 
                         login_user, logout_user)

# Password encryption helper
from werkzeug.security import check_password_hash, generate_password_hash

# Import database object from main app
from app import db
from app import http_auth
from app import login_manager

# Models of app module
from app.auth.models import User
from app.auth import auth

from app.auth.utils import authenticate


logger = logging.getLogger(__name__)


@auth.route('/login/', methods=['GET', 'POST'])
def sign_in():
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect('/auth/users/')
        
        next = request.args.get('next')
        return render_template('auth/login.html', data={"next": next})
    else:
        data = request.form
        user = authenticate(data.get('email'), data.get('password'))
        if not user:
            flash('Username or password is incorrect')
            return redirect('/auth/login/?next={}'.format(data.get('next')))
        
        login_user(user)
        next = data.get('next')
        if not next:
            next = "/auth/users/"
        return redirect(next) 
 

@auth.route('/logout/', methods=['GET'])
def sign_out():
    logout_user()
    return redirect('/')   

@auth.route('/signup/', methods=['POST', "GET"])
def sign_up():
    if request.method == "GET":
        return render_template('auth/signup.html')
    else:
        data = request.form
        user = User(email=data.get('email'), 
                        password=generate_password_hash(data.get('password')),
                        first_name=data.get('first_name'),
                        last_name=data.get('last_name'),
                        role=1,
                        status=1)
            
        db.session.add(user)
        db.session.commit()
        
        return redirect('/auth/users/')

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


@auth.route('/users/', methods=['GET'])
@login_required
def users():
    users = User.query.all()
    return render_template('auth/users.html', users=users)
