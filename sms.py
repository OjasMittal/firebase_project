import requests
import pandas



def bulk_sms(number,message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    #message = "Your hair treatment appointment with Juventus is scheduled at 6pm today."
    payload = f'sender_id=FTWSMS&message={message}&route=v3&language=english&numbers={number}'
    headers = {
        'authorization': "EYAlFQpae3j6mdJncuXPwZoHhTtv9SMN8D4zIy7rUq12OgBkiK0InWbCEsvNDqV5lwuA7Y9zKRfk3rPm",
        'Content-Type': 'application/x-www-form-urlencoded'

    }
    response = requests.request("POST", url=url, data=payload, headers=headers)
    print(response.text)

