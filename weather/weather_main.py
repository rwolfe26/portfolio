import requests
import smtplib
import os
from dotenv import load_dotenv
print("Script started")

load_dotenv()

api_key = os.getenv('OPENWEATHER_API_KEY')
print(api_key)
sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv("SENDER_PASSWORD")
receiver_number = os.getenv("RECEIVER_NUMBER")

lat,lon = "43.0831", "-73.7850"
units = "imperial"
base_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"


try:
    response = requests.get(base_url + f"&units={units}")
    response.raise_for_status()
    weather_data = response.json()
    temp = weather_data['current']['temp']
    description = weather_data['current']['weather'][0]['description']
    
    def send_text_message(temp,description):
        receiver_email = f'{receiver_number}@vtext.com'
        email_subject = "Daily Weather Update"
        email_body = f'Temperature: {temp} °F\nDescription: {description}'
        
        with smtplib.SMTP("smtp.gmail.com",587) as server:
            server.starttls()
            server.login(sender_email,sender_password)
            server.sendmail(sender_email,receiver_email, f"Subject: {email_subject}\n\n{email_body}")
        
    send_text_message(temp,description)
        
except requests.RequestException as e:
    print(f"Error in making API request: {e}")
except smtplib.SMTPException as e:
    print(f"Error in sending email: {e}")
except Exception as e:
    print(f"An error occured: {e}")
                            
                   


        
    

