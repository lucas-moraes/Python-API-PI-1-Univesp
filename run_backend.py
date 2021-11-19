from backend.view import app
import uvicorn


uvicorn.run(
    app,
    host="127.0.0.1",
    port=8000
    # ssl_keyfile="./backend/cert/localhost+2-key.pem",
    # ssl_certfile="./backend/cert/localhost+2.pem"
)
