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

# Register routing
@bp.route('/u<id>')
def profile(id):
	db = get_db()
	error = None

	user = db.execute(
		'SELECT * from user WHERE id = ?', (id,)
	).fetchone()

	if user is None:
		default = {
			'username': 'Unknown',
			'id': 0
		}
		error = 'ID {} does not exist.'.format(id)
		flash(error)
		abort(404)

	return render_template('profile.html', user=user)