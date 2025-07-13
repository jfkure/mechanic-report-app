# Your routes and views now live here
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Report
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    reports = Report.query.order_by(Report.date.desc()).all()
    return render_template('dashboard.html', reports=reports)

@main.route('/report', methods=['GET', 'POST'])
def job_form():
    if request.method == 'POST':
        data = Report(
            mechanic_name=request.form['mechanic_name'],
            vehicle_id=request.form['vehicle_id'],
            issue_description=request.form['issue_description']
        )
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('main.dashboard'))

    return render_template('job_form.html')

@main.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
