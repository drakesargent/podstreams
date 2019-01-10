from flask import Flask

app = Flask(__name__)
app.config.from_object(app.config)

from app.core.views import rue as core
app.register_blueprint(core)