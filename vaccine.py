import requests
import json
from threading import Timer
import subprocess

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'

DISTRICT_ID = '365'
DATES = ['09-05-2021', '10-05-2021']

with open('headers.json', 'r') as f:
    headers = f.read()
    headers = json.loads(headers)

def send_email():
    try:
        subprocess.run(["./send_mail.sh"])
    except:
        print('Error sending email')

def find_slots():
    def check18(slot):
        sessions = slot['sessions']
        return any(map(lambda x: x['min_age_limit'] == 18 and x['available_capacity'] > 0, sessions))
    try:
        params = { "district_id": DISTRICT_ID }
        slots = []
        for date in DATES:
           params["date"] = date
           r = requests.get(url, params, headers=headers)
           data = r.json()
           data = data["centers"]
           slots += list(filter(check18, data))

        if len(slots) > 0:
            print('Found slot')
            send_email()
        else:
            print('No slot')
    except Exception as e:
        print(r.status_code)
        print(e)

def loop():
    Timer(5.0, loop).start()
    find_slots()

loop()






