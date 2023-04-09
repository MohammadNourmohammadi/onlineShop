from melipayamak import Api, passwords
from celery import shared_task


@shared_task()
def send_sms_success_payment(phone, name):
    username = passwords.SMS_USER
    password = passwords.SMS_PASS
    api = Api(username, password)
    sms = api.sms()
    to = phone
    _from = passwords.SMS_FROM_NUMBER
    text = f'{name} عزیز سفارش شما با موفقیت ثبت شد و در حال آماده سازی است.' \
           f'تلوند یه سایت خوشمزه'
    response = sms.send(to, _from, text)
    print(response)
