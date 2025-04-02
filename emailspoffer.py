import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email account credentials (for Gmail)
your_email = "example@gmail.com"
your_password = ""  # Use an App Password if using 2FA

# Receiver's email (your faculty's email address)
receiver_email = "reciever@gmail.com"

# Fake "From" details (the spoofed name and email address)
spoofed_from_name = "fake club"
spoofed_from_email = "fake.spu@gmail.com"  # This can be any fake name

# Email content
subject = "Test Email with Spoofed From"
body = "This is an educational email for studying spoofing techniques."

# Prepare the email message
msg = MIMEMultipart()
msg['From'] = f"{spoofed_from_name} <{spoofed_from_email}>"
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Gmail's SMTP server settings
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Port for TLS

# Sending the email
try:
    # Set up the server and log in
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure connection
    server.login(your_email, your_password)  # Log in with your credentials

    # Send the email
    text = msg.as_string()
    server.sendmail(your_email, receiver_email, text)
    print("Email sent successfully to", receiver_email)
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()  # Close the server connection
