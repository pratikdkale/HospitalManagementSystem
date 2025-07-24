from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SECRET_KEY"] = "Get_Your_Own_Key"

bootstrap = Bootstrap(app)

from application import routes
