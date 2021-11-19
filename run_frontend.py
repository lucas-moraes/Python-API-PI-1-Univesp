import os
from waitress import serve
from frontend.app import app

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    context = (
        './frontend/cert/localhost+2.pem',
        './frontend/cert/localhost+2-key.pem'
    )
    os.environ['FLASK_ENV'] = 'development'
    serve(app.run(
        host="127.0.0.2",
        port=5000,
        # ssl_context=context
    ))
