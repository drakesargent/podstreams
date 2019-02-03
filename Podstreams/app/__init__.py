from flask import Flask
from app.core.views import rue as core

app = Flask(__name__)
app.config.from_object(app.config)
app.register_blueprint(core)
