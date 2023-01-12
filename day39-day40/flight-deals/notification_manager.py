import smtplib
import os
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL = "rp42dev@gmail.com"


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(self):
        self.message = ""
        self.flight_link = ""

    def send_emails(self, emails, message, flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=EMAIL_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{flight_link}".encode('utf-8')
                )
