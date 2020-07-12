"""
Main file
"""
from send_sms import send_sms

current_weather = "20 C"


#testing sending sms through twilio api
send_sms('+917798487388',current_weather)
