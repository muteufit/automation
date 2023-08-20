import random
import smtplib
from email.mime.text import MIMEText
import schedule
import time
import requests
from bs4 import BeautifulSoup

# Email configuration
EMAIL_ADDRESS = 'your_email@example.com'  # Your email address
EMAIL_PASSWORD = 'your_email_password'    # Your email password
SMTP_SERVER = 'smtp.example.com'          # Replace with your SMTP server
SMTP_PORT = 587                           # Replace with the appropriate SMTP port

def get_random_word():
    response = requests.get('https://randomword.com/')
    soup = BeautifulSoup(response.content, 'html.parser')
    word = soup.find(id='random_word').get_text().strip()
    return word

def get_word_definition(word):
    response = requests.get(f'https://www.dictionary.com/browse/{word}')
    soup = BeautifulSoup(response.content, 'html.parser')
    definition = soup.find("meta", {"name": "description"})["content"]
    return definition

def send_word_email(word, definition, email):
    subject = "Word of the Day"
    message = f"Word: {word}\nDefinition: {definition}"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, [email], msg.as_string())
        print("Word email sent!")

    except Exception as e:
        print("An error occurred while sending the email:", str(e))

    finally:
        server.quit()

def send_daily_word():
    word = get_random_word()
    definition = get_word_definition(word)
    email = input("Enter your email address: ")
    send_word_email(word, definition, email)

if __name__ == "__main__":
    schedule.every().day.at("09:00").do(send_daily_word)

    print("Daily Word Tool is running. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)
