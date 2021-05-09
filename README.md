# Vaccinate.py

Get notified whenever vaccines get available
Run this python script somewhere (locally, on some remote server) and get notified by email whenever slots are available in your district

## Dependencies

- Python3
- ssmtp
  - Follow [this](https://netcorecloud.com/tutorials/linux-send-mail-from-command-line-using-smtp-server/) for setting it up if you dont have it.


## Usage

1. You will need your district id:
    1. First use [this](https://cdn-api.co-vin.in/api/v2/admin/location/states) to find out your state id.
    2. Then use [this](https://cdn-api.co-vin.in/api/v2/admin/location/districts/16), replacing the id with your state id to find out your district id.
2. Replace the `DISTRICT_ID` and `DATES` in `vaccine.py` variables with the values that apply to you. I recommend only setting a couple of dates (tomorrow and day after)
3. Replace the email id list in `send_email.sh` with email ids you want to send notifs to.
4. Run the script in a shell using `./vaccine.py`


By default this script runs at 5 second intervals and finds slots for the 18+ age group. You can change these defaults by changing values in `vaccine.py`


