from melipayamak import Api, passwords


def send_sms_success_payment(order):
    username = passwords.SMS_USER
    password = passwords.SMS_PASS
    api = Api(username, password)
    sms = api.sms()
    to = order.address.phone_of_transferee
    _from = passwords.SMS_FROM_NUMBER
    text = f'{order.address.name_of_transferee} عزیز سفارش شما با موفقیت ثبت شد و در حال آماده سازی است.' \
           f'تلوند یه سایت خوشمزه'
    response = sms.send(to, _from, text)
    print(response)
