import requests
from datetime import datetime
import smtplib
import time

my_email = 'my_mail@gmail.com'
my_password = 'my_password'
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
my_latitude = 52.229675
my_longitude = 21.012230


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if my_latitude - 5 <= iss_latitude <= my_latitude + 5 and my_longitude - 5 <= iss_longitude <= my_longitude + 5:
        return True


def is_night():
    parameters = {
        "latitude": my_latitude,
        "longitude": my_longitude,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP(SMTP_SERVER, PORT)
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
