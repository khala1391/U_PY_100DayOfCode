import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL ="khala1391@gmail.com"
MY_PASSWORD = "xnmp nkpp fcte rjty"
MY_LAT = 13.938543   # vary +-5
MY_LNG = 100.422962

def is_iss_overhead():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url=url)
    # print(response.status_code)
    # print(response.raise_for_status)

    data =response.json()
    # print(data)


    iss_lat = float(data['iss_position']['latitude'])
    iss_lng = float(data['iss_position']['longitude'])

    # location = (lat,lng)
    # print(location)

    # check  -5 deg to + 5 deg of iss_location compared to my_location
    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LNG-5 <= iss_lat <= MY_LNG+5:
        return True

def is_night():
    parameters ={
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0, 
    }

    url2 = "https://api.sunrise-sunset.org/json"
    response =requests.get(url=url2, params=parameters)
    # print(response.raise_for_status)
    data= response.json()
    # print(data)

    # sunrise = data['results']['sunrise']
    # sunset = data['results']['sunset']

    # print(sunrise)      # 2024-10-26T08:11:56+00:00
    # print(sunset)       # 2024-10-26T20:28:12+00:00
    # print(sunrise.split('T'))
    # print(sunrise.split('T')[1].split(':')[0])

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    # print(sunrise)
    # print(sunset)
    # time_now = datetime.now()  # 2024-10-26 20:56:38.549200
    # print(time_now.hour)
    time_now = datetime.now().hour  # 20
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg= f"Subject: Lookup ☝️☝️☝️ \n\n This ISS 🛰️ is above you in the sky")
    else:
        print(f"run at {datetime.now()}")
        time.sleep(60)