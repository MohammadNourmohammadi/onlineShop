run:
	sudo mkdir /var/run/gunicorn ; sudo touch /var/run/gunicorn/dev.pid && sudo gunicorn -c config/gunicorn/dev.py
run-srv:
	sudo mkdir /var/run/gunicorn ; sudo touch /var/run/gunicorn/dev.pid && gunicorn -c config/gunicorn/dev.py
stop:
	sudo kill -9 `cat /var/run/gunicorn/dev.pid`
error-nginx-srv:
	vim /var/log/nginx/telond.error.log
access-nginx-srv:
	vim /var/log/nginx/telond.access.log
error-nginx:
	vim /opt/homebrew/var/log/nginx/telond.error.log
access-nginx:
	vim /opt/homebrew/var/log/nginx/telond.access.log
restart-nginx:
	brew services restart nginx
restart-nginx-srv:
	sudo systemctl restart nginx
log-gunicorn:
	sudo vim /var/log/gunicorn/dev.log
collect-static:
	python manage.py collectstatic
