import smtplib
import time
from datetime import datetime, timedelta

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with the appropriate SMTP port
EMAIL_ADDRESS = 'your_email@example.com'  # Your email address
EMAIL_PASSWORD = 'your_email_password'  # Your email password

def send_email(subject, message, to_email):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        email_content = f"Subject: {subject}\n\n{message}"
        server.sendmail(EMAIL_ADDRESS, to_email, email_content)

        print("Reminder email sent successfully!")

    except Exception as e:
        print("An error occurred while sending the email:", str(e))

    finally:
        server.quit()

def schedule_reminders(reminders):
    while True:
        current_time = datetime.now()

        for reminder in reminders:
            reminder_time = reminder["time"]
            task = reminder["task"]
            to_email = reminder["email"]

            if current_time.hour == reminder_time.hour and current_time.minute == reminder_time.minute:
                subject = f"Reminder: {task}"
                message = f"Don't forget to {task}!"
                send_email(subject, message, to_email)

        time.sleep(60)  # Check for reminders every minute

if __name__ == "__main__":
    # Customize your reminders here
    reminders = [
        {"time": datetime.strptime("09:00", "%H:%M"), "task": "drink water", "email": "your_email@example.com"},
        {"time": datetime.strptime("12:00", "%H:%M"), "task": "take a break", "email": "your_email@example.com"},
        {"time": datetime.strptime("15:00", "%H:%M"), "task": "exercise", "email": "your_email@example.com"},
        # Add more reminders here
    ]

    schedule_reminders(reminders)
