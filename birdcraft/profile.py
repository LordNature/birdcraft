"""
Profile.py
------
Handles user profiles and dashboard
List of functions:
* init
"""

# Flask blueprinting services
from flask import (
	Blueprint, flash, g, redirect, render_template, url_for, abort
)

# Fetches database from our app
from birdcraft.auth import login_required
from birdcraft.db import get_db

bp = Blueprint('profile', __name__)

# Index
@bp.route('/')
def index():
	if g.user is None:
		return render_template('index.html')
	return redirect(url_for('profile.dashboard'))

# Dashboard
@bp.route('/dashboard')
@login_required
def dashboard():
	error = None
	
	if g.user['rank'] == 1:
		rank='Admin'
	else:
		rank='User'

	if error is not None:
		flash(error)
	return render_template('dashboard.html', rank=rank)

# Profile routing
@bp.route('/user/<id>')
def user(id):
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

	users = db.execute(
		'SELECT * from user'
	).fetchall()

	if user is None:
		error = 'The galaxy has been eradicated.'.format(id)
		flash(error)
		abort(404)

	return render_template('users.html', users=users)