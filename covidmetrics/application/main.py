"""Logged-in page routes."""
from flask import Blueprint, render_template, session
from flask_login import login_required, current_user, AnonymousUserMixin
from . import cache
from covidmetrics.application.DataCaches.IndexDataCache import IndexDataCache
from datetime import datetime


# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@main_bp.route('/')
def index():
    dc = cache.get('index')
    if dc is None:
        dc = IndexDataCache()
        cache.set('index',dc)
    if current_user.is_anonymous:
        session['username']=''
    else:
        session['username']=current_user.name
    if 'district_id' not in session:
        session['district_id'] = ''
        session['district_name'] = ''
    if 'perms' not in session:
        session['perms'] = {}
        session['permset'] = 0
    return render_template('index.html', data=dc.districts, session=session)

@main_bp.route('/status')
def status():
    return 'Online'

@main_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=session.get('username'), session=session)

