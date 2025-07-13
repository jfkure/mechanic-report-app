# The new entry point to start your app
import os
from app import create_app, db

app = create_app()

if __name__ == '__main__':
    # Bind to the port Render provides (default to 5000 if not found)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
