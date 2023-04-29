# onlineShop
use python 3.11 or above

use rabbitmq

start celery worker:

celery -A onlineShop worker --loglevel=INFO

start rabbitmq:

brew service start rabbitmq



conf nginx:

server_tokens               off;
access_log                  /opt/homebrew/var/log/nginx/telond.access.log;
error_log                   /opt/homebrew/var/log/nginx/telond.error.log;
server {
  server_name               localhost;
  listen                    80;
  location / {
    proxy_pass              http://localhost:8000;
    proxy_set_header        Host $host;
  }
  location /static/ {
        alias /Users/mohammad/Desktop/onlineShop/static/;
  }
}