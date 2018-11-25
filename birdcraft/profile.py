"""
Profile.py
------
Handles user profiles and dashboard
List of functions:
* init
"""

# Flask blueprinting services
from flask import (
	Blueprint, flash, g, render_template, url_for, abort
)

# Fetches database from our app
from birdcraft.db import get_db

bp = Blueprint('profile', __name__)

# Index
@bp.route('/')
def index():
	return render_template('index.html')

# Dashboard
@bp.route('/dasboard')
def dashboard():
	return render_template('index.html')

# Profile routing
@bp.route('/user/<id>')
def profile(id):
	db = get_db()
	error = None

	user = db.execute(
		'SELECT * from user WHERE id = ?', (id,)
	).fetchone()

	if user is None:
		error = 'ID {} does not exist.'.format(id)
		flash(error)
		abort(404)

	return render_template('profile.html', user=user)

# Profile routing
@bp.route('/users')
def list_users():
	db = get_db()
	error = None

	user = db.execute(
		'SELECT * from user'
	).fetchall()

	if user is None:
		error = 'The galaxy has been eradicated.'.format(id)
		flash(error)
		abort(404)

	return render_template('users.html', user=user)