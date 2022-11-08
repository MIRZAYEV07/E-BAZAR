import json
import random
import string

import requests
from django.conf import settings as s





def generate_random_password():
    _int = "".join(random.choice(string.digits) for _ in range(5))
    return _int


def send_password_as_sms(phone_number, password):
    url = s.SMS_DOMAIN + "?token=" + s.SMS_TOKEN
    data = {
        "message": {"recipients": [str(phone_number)]},
        "priority": "default",
        "sms": {"content": f"your password for zukko system is: {password}"},
    }

    requests.post(url, data=json.dumps(data), timeout=5)
