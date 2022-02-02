import time
import requests
import datetime as dt
import smtplib

MY_LAT = "your latitude"
MY_LONG = "your longitude"
MY_EMAIL = "your email"
MY_PASSWORD = "your password"


def is_night_and_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()["iss_position"]
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split("+")[0].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split("+")[0].split(":")[0])

    time_now = dt.datetime.now().hour

    if 17.0 <= iss_latitude <= 27.0 and 83.0 <= iss_longitude <= 93.0 and sunrise < time_now < sunset:
        return True


while True:
    time.sleep(60)
    if is_night_and_overhead():
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look UP!\n\n The ISS is above you in the sky.")
