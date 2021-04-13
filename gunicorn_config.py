import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = '0.0.0.0:5055'
umask = 0o007
reload = True

#logging
accesslog = '-'
errorlog = '-'
