# Your main Flask script
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# --- Database Setup ---
def init_db():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            vehicle_make TEXT,
            vehicle_model TEXT,
            vehicle_year TEXT,
            vin TEXT,
            repair_summary TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# --- Dashboard View ---
@app.route('/')
def dashboard():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM jobs ORDER BY date DESC')
    jobs = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', jobs=jobs)

# --- New Job Entry ---
@app.route('/new', methods=['GET', 'POST'])
def new_job():
    if request.method == 'POST':
        data = (
            request.form['customer_name'],
            request.form['vehicle_make'],
            request.form['vehicle_model'],
            request.form['vehicle_year'],
            request.form['vin'],
            request.form['repair_summary'],
            request.form['date']
        )
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO jobs (
                customer_name, vehicle_make, vehicle_model,
                vehicle_year, vin, repair_summary, date
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    return render_template('job_form.html')

# --- Individual Job Report View ---
@app.route('/report/<int:job_id>')
def report(job_id):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM jobs WHERE id = ?', (job_id,))
    job = cursor.fetchone()
    conn.close()
    if job:
        return render_template('report_template.html', job=job)
    else:
        return render_template('404.html'), 404

# --- Custom 404 Page ---
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# --- Entry Point for Render Deployment ---
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
