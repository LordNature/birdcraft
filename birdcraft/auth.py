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
