from flask import Flask
from config import Config

app = Flask(__name__, static_folder=Config.STATIC_FOLDER,
            template_folder=Config.TEMPLATES_FOLDER)
app.config.from_object(Config)

from app import routes
