import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Function to read data from a CSV file
def read_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data


# Function to send emails
def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Set up the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")


# Main automation function
def automate_emails(csv_path, sender_email, sender_password):
    data = read_csv(csv_path)
    for row in data:
        recipient_email = row['Email']
        name = row['Name']
        subject = "Hello from Custom Automation"
        body = f"Hi {name},\n\nThis is a personalized email sent via Python automation.\n\nBest Regards,\nYour Automation System"

        send_email(sender_email, sender_password, recipient_email, subject, body)


# Execution starts here
if __name__ == "__main__":
    # Replace with your details
    csv_file_path = 'contacts.csv'  # Path to your CSV file
    your_email = 'devmarce12@gmail.com'
    your_password = 'eqmq qwxc oklz fvpo'

    automate_emails(csv_file_path, your_email, your_password)
