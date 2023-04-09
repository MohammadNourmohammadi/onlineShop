# onlineShop
use python 3.11 or above

use rabbitmq

start celery worker:

celery -A onlineShop worker --loglevel=INFO

start rabbitmq:

brew service start rabbitmq