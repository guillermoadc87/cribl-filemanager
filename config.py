import os
from logging.config import dictConfig


class Config:
    """
    App configuration
    """

    APP_NAME = os.environ.get('APP_NAME', 'Cumulus API')

    # project directory (absolute path), path containing config.py file
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    S3_BUCKET = os.environ.get('S3_BUCKET', 'bucket-filemanager-sand')

    ALLOWED_EXTENSIONS = os.environ.get('ALLOWED_EXTENSIONS', {'tgz'})

    LOGGIN = {
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'filename': '/tmp/flask_app.log',
            }
        },
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi', 'file']
        }
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


try:
    from production_config import ProductionConfig as MainProductionConfig

    class ProductionConfig(Config, MainProductionConfig):
        pass
except ImportError:
    class ProductionConfig(DevelopmentConfig):
        DEBUG = False


config = {
    'development': DevelopmentConfig,
    'default': ProductionConfig,
    'production': ProductionConfig
}
