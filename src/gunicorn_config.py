workers = 1
worker_class = 'socketio.sgunicorn.GeventSocketIOWorker'
bind = '0.0.0.0:5400'
pidfile = '/tmp/gunicorn-rivers.pid'
debug = True
loglevel = 'debug'
errorlog = '/tmp/gunicorn_rivers_error.log'
accesslog = '/tmp/gunicorn_rivers_access.log'
daemon = True 
