import smtplib
import os
from dotenv import load_dotenv
import json
import datetime

load_dotenv()


def send_mail(msg):
    email = os.environ.get('MY_EMAIL')
    rev = os.environ.get('VED_EMAIL')
    token = os.environ.get('TOKEN')
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        try:
            server.login(email, token)
            print("Successfully Logged in")
            try:
                server.sendmail(email, rev, msg)
                print("Successfuly Send Email!")
            except:
                print("Error Sending Email")
        except:
            print("Error Logging in!!!")
    except:
        print("Error Starting Account!!!")

def check_bday(obj):
    name = obj["name"]
    phone = obj["phone_number"]
    CurrentDate = datetime.datetime.now().strftime('%Y-%m-%d')
    obj_date = obj["birthday"]
    obj_date = obj_date.split("-")
    CurrentDate = CurrentDate.split("-")
    if(int(obj_date[1]) == int(CurrentDate[1])):
        if (int(CurrentDate[2]) == (int(obj_date[2]) - 1)):
            wish = f"Its {name}'s birthday on {obj_date}, Phone Number: {phone}"
        
            send_mail(wish)


if __name__ == "__main__":
    email = os.environ.get('MY_EMAIL')
    rev = os.environ.get('VED_EMAIL')
    token = os.environ.get('TOKEN')
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        try:
            server.login(email, token)
            print("Successfully Logged in")
            try:
                with open('iste2024.json', 'r') as f:
                    data = json.load(f)
                print("Loaded Data")
                for person in data:
                    check_bday(person)
            except:
                    print("Error Importing JSON File")            
        except:
            print("Logging Unsuccessful")
    except:
        print("Server Unavailable")
