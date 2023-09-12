# Online Shop
It's online shop website source.
I used Django,Postgresql, Rabbitmq, Celery, API for payment.

## Getting Started

### Dependencies

* python 3.11 or above, rabbitmq, and python libraries in requirements.txt file.

### Installing

* install<a href="https://www.rabbitmq.com//"> rabbitmq</a>
* install<a href="https://www.postgresql.org/"> postgresql</a>

### Executing program

* first use this cmd to install requirements
* pip3 install -r requirements.txt
* Read Makefile for all nessessory cmd.

## Authors

Mohammad Nourmohammadi [Linkdin](https://www.linkedin.com/in/mohammad-nourmohammadi/)




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

nginx willnload all files in /opt/homebrew/etc/nginx/servers/.
