import multiprocessing
from app import app

workers = multiprocessing.cpu_count() * 2 + 1
bind = f"{app.config['HOST']}:{app.config['PORT']}"
umask = 0o007
reload = True

# logging
accesslog = '-'
errorlog = '-'
