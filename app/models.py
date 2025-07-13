from . import db

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    mechanic_name = db.Column(db.String(100), nullable=False)
    vehicle_id = db.Column(db.String(50), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Pending')
