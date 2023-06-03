from melipayamak import Api, passwords
from celery import shared_task


@shared_task()
def send_sms_get_postman(phone, name):
    username = passwords.SMS_USER
    password = passwords.SMS_PASS
    api = Api(username, password)
    sms = api.sms()
    to = phone
    _from = passwords.SMS_FROM_NUMBER
    text = f'{name} عزیز سفارش شما تحویل پیک داده شد و تا ساعتی دیگر به دستتان خواهد رسید.' \
           f'تلوند یه سایت خوشمزه'
    response = sms.send(to, _from, text)
    print(response)
