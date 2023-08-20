import random
import smtplib
from email.mime.text import MIMEText
import schedule
import time

# Email configuration
EMAIL_ADDRESS = 'your_email@example.com'  # Your email address
EMAIL_PASSWORD = 'your_email_password'    # Your email password
SMTP_SERVER = 'smtp.example.com'          # Replace with your SMTP server
SMTP_PORT = 587                           # Replace with the appropriate SMTP port

# List of inspirational quotes
quotes = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The future depends on what you do today. - Mahatma Gandhi",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    # Add more quotes here
]

def send_quote_email(quote, email):
    subject = "Your Daily Inspirational Quote"
    message = quote
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, [email], msg.as_string())
        print("Quote email sent!")

    except Exception as e:
        print("An error occurred while sending the email:", str(e))

    finally:
        server.quit()

def send_daily_quote():
    quote = random.choice(quotes)
    email = input("Enter your email address: ")
    send_quote_email(quote, email)

if __name__ == "__main__":
    schedule.every().day.at("09:00").do(send_daily_quote)

    print("Daily Quote Script is running. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(1)
