import os


# database settings
MONGODB_URL = os.environ.get('MONGODB_URL', 'mongodb://mongo:27017')
MONGODB_DATABASE = os.environ.get('MONGODB_DATABASE', 'iris')
MONGODB_COLLECTION = os.environ.get('MONGODB_COLLECTION', 'predict')

HOST = os.environ.get('HOST', "0.0.0.0")
PORT = os.environ.get('PORT', "5000")

# gunicorn settings
bind = os.environ.get('GUNICORN_BIND', f'{HOST}:{PORT}')
workers = os.environ.get('GUNICORN_WORKERS', 1)
threads = os.environ.get('GUNICORN_THREADS', 1)
reload = os.environ.get('GUNICORN_RELOAD', True)
timeout = os.environ.get('GUNICORN_TIMEOUT', 600)
graceful_timeout = os.environ.get('GUNICORN_GRACEFUL_TIMEOUT', 600)
loglevel = os.environ.get('GUNICORN_LOGLEVEL', 'debug')

WEIGHTS_PATH = '/code/projeto/model/weights/best_model_weights.sav'

PATH_LOG = os.environ.get("PATH_LOG", "./log_api_iris")
