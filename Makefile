run:
	sudo gunicorn -c config/gunicorn/dev.py
stop:
	sudo kill -9 `cat /var/run/gunicorn/dev.pid`
error-nginx:
	vim /opt/homebrew/var/log/nginx/telond.error.log
access-nginx:
	vim /opt/homebrew/var/log/nginx/telond.access.log
restart-nginx:
	brew services restart nginx e