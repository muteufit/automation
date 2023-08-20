import schedule
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Email configuration
EMAIL_ADDRESS = 'your_email@example.com'  # Your email address
EMAIL_PASSWORD = 'your_email_password'    # Your email password
SMTP_SERVER = 'smtp.example.com'          # Replace with your SMTP server
SMTP_PORT = 587                           # Replace with the appropriate SMTP port

# List of birthdays (replace with actual names and dates)
birthdays = {
    'Friend 1': '2023-08-25',
    'Family Member 1': '2023-09-10',
    # Add more birthdays here
}

def send_birthday_reminder(name, email):
    subject = f"Reminder: Upcoming Birthday for {name}"
    message = f"Don't forget to wish {name} a happy birthday on their upcoming special day!"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, [email], msg.as_string())
        print(f"Reminder email sent for {name}'s birthday!")

    except Exception as e:
        print("An error occurred while sending the email:", str(e))

    finally:
        server.quit()

def check_birthdays():
    today = datetime.today().date()

    for name, birthdate in birthdays.items():
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
        days_until_birthday = (birthdate - today).days

        if days_until_birthday == 1:
            email = input(f"Enter the email address for {name}: ")
            send_birthday_reminder(name, email)

if __name__ == "__main__":
    schedule.every().day.at("09:00").do(check_birthdays)

    print("Birthday Reminder Script is running. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)
