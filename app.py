import logging
import logging.handlers
from pathlib import Path

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from waitress import serve

import appmain.command as cmd
from models.models import db

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)

    csrf.init_app(app)
    app.config['csrf'] = csrf

    # app.config['SESSION_COOKIE_SECURE'] = False

    # set context
    with app.app_context():
        app.config.from_object("settings")  # public information日立　真鶴荘
        if "development" in app.config.get("ENVIRONMENT"):
            app.config.from_pyfile(
                Path("instance", "config", "development.py"), silent=True)
        else:
            app.config.from_pyfile(
                Path("instance", "config", "production.py"), silent=True)

        app.secret_key = app.config.get("SECRET_KEY")
        db.init_app(app)
        db.create_all()

        # import and register Blueprint
        from appmain.appmain_bp import appmain_bp
        from appml.appml_bp import appml_bp
        from auth.auth_bp import auth_bp
        from manual.manual_bp import manual_bp
        from topview.topview_bp import topview_bp
        app.register_blueprint(auth_bp)
        app.register_blueprint(topview_bp)
        app.register_blueprint(appmain_bp)
        app.register_blueprint(appml_bp)
        app.register_blueprint(manual_bp)

        # set logger
        # DEBUG, INFO, WARNING, ERROR, CRITICAL
        app.logger.setLevel(logging.INFO)
        h = logging.handlers.RotatingFileHandler(app.config["LOG_FILE"],
                                                 mode="a",
                                                 maxBytes=app.config["LOG_FILE_MAXBYTES"],
                                                 backupCount=3,
                                                 encoding="utf-8")
        h.setFormatter(logging.Formatter(
            ' %(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        app.logger.addHandler(h)

        logging.getLogger('werkzeug').disabled = True

    return app


app = create_app()  # factory
app.logger.info("Logging Starts.")
cmd.checkup_resources()


if __name__ == "__main__":
    host = app.config["HOST"]
    port = app.config["PORT"]
    # app.run(host=host, port=port, threaded=True, debug=True)  # Flask, Apache24, Heroku
    # waitress, Windows service, Azure
    serve(app, host=host, port=port, threads=10)
