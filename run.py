# The new entry point to start your app
import os
from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()  # Creates tables if they don't exist

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
