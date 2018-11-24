"""
Profile.py
------
Handles user profiles and dashboard
List of functions:
* init
"""

# Flask blueprinting services
from flask import (
	Blueprint, flash, g, render_template, url_for
)

# Fetches database from our app
from birdcraft.db import get_db

bp = Blueprint('profile', __name__)

# Register routing
@bp.route('/u<id>')
def profile(id):
	return render_template('profile.html', id=id)