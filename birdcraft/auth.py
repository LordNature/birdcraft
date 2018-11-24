"""
Auth.py
------
Handles authentication of the user
List of functions:
* init
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

bp = Blueprint('auth', __name__, url_prefix='/auth')

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
				'SELECT id from user WHERE username = ?', (username)
			).fetchone() is not None:
			error = 'Username {} is already registered'.format(username)

		if error is None:
			db.execute(
					'INSERT INTO user (username, password) valeus (?, ?)',
					(username, generate_password_hash(password))
				)
			db.commit()
			return redirect(url_for('auth.login'))

		flash(error)
	return render_template('auth/register.html');

# Login routing
def login():
	if request.method == 'POST':
		username = request.form['usr']
		password = request.form['pwd']

		db = get_db()
		error = None

		user = db.execute(
				'SELECT * FROM user WHERE username = ?', (username)
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