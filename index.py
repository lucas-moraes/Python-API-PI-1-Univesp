from waitress import serve
from frontend import app

serve(app.app.run(), host='0.0.0.0', port=8080)
