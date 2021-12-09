from celery import current_app as current_celery_app
from flask import Flask


def create_flask_app():
    """
    create Flask app.
    :return: Flask
    """
    app = Flask(__name__)
    app.config['CELERY_BROKER_URL'] = 'redis://broker:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://broker:6379/0'
    return app


def create_celery_app(app):
    """
    Create celery app
    :param app: Flask
    :return: Proxy
    """
    celery = current_celery_app
    celery.config_from_object(app.config, namespace='CELERY')
    return celery
