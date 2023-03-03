from flask import Flask
from application.config import Config

app = Flask(__name__, template_folder = "templates")
app.config.from_object(Config)
app.app_context().push()

if __name__ == "__main__":
    from application.controllers import *
    app.run(host = "0.0.0.0", port = 8080)
