"""
Auth.py
------
Handles authentication of the user
List of functions:
* register: registers the user
* login: logins the user
* logout: logouts the user
* load_logged_in_user: gets session cookies
* login_required: wrapper for view that checks if user logged in
	* todo: add rank system
"""

import functools

# Flask blueprinting services
from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
# Flask provided hashing service; uses sha
from werkzeug.security import check_password_hash, generate_password_hash

# Fetches database from our app
from birdcraft.db import get_db

bp = Blueprint('auth', __name__)

# Register routing
@bp.route('/register', methods=('GET', 'POST'))
def register():
	if request.method == 'POST':
		username = request.form['usr']
		password = request.form['pwd']

		db = get_db()
		error = None

		if not username:
			error = 'Username required.'
		elif not password:
			error = 'Password required.'
		elif db.execute(
				'SELECT id from user WHERE username = ?', (username,)
			).fetchone() is not None:
			error = 'Username {} is already registered'.format(username)

		if error is None:
			db.execute(
					'INSERT INTO user (username, password) values (?, ?)',
					(username, generate_password_hash(password))
				)
			db.commit()
			return redirect(url_for('auth.login'))

		flash(error)
	return render_template('auth/register.html');

# Login routing
@bp.route('/login', methods=('GET', 'POST'))
def login():
	if request.method == 'POST':
		username = request.form['usr']
		password = request.form['pwd']

		db = get_db()
		error = None

		user = db.execute(
				'SELECT * FROM user WHERE username = ?', (username,)
			).fetchone()

		if user is None:
			error = 'Incorrect username.'
		elif not check_password_hash(user['password'], password):
			error = 'Incorrect password.'

		# see http://flask.pocoo.org/docs/1.0/api/#flask.session
		if error is None:
			session.clear()
			session['user_id'] = user['id']
			return redirect(url_for('home'))

		flash(error)

	return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
	user_id = session.get('user_id')

	if user_id is None:
		g.user = None
	else:
		g.user = get_db().execute(
				'SELECT * FROM user WHERE id = ?', (user_id,)
			).fetchone()

@bp.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('home'))

# Login wrapper
def login_required(view):
	@functools.wraps(view)
	def wrapped_view(**kwargs):
		if g.user is None:
			# Add error response
			return redirect(url_for('auth.login'))
		return view(**kwargs)
	return wrapped_view