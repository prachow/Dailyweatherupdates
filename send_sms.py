"""
file to handle sending sms using twilio api
"""

from APIKEYS import TWILIO_SID, TWILIO_TOKEN
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = TWILIO_SID
auth_token = TWILIO_TOKEN

def send_sms(phone_number, message):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
             body=message,
             from_='+12015818325',
             to=phone_number
         )
    print(message)
