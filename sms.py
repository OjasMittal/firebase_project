import requests
import pandas



def bulk_sms(number):
    url = "https://www.fast2sms.com/dev/bulkV2"
    message = "Your hair treatment appointment with Juventus is scheduled at 6pm today."
    payload = f'sender_id=Cghpet&message={message}&route=v3&language=english&numbers={number}'
    headers = {
        'authorization': "HberTzKB8YW3uRmZ6XahvVdkML7w40NSnODqP1JoQxtypc9UFAIM5TOHdlAf0hgpL1erci4G9YX8oS6J",
        'Content-Type': 'application/x-www-form-urlencoded'

    }
    response = requests.request("POST", url=url, data=payload, headers=headers)
    print(response.text)

