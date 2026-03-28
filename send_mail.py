import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "it.adminsupport2@gmail.com"
receiver = "mitnick.user@gmail.com"
password = "your_app_password"

msg = MIMEMultipart()
msg["Subject"] = "Critical Security Update Required"
msg["From"] = sender
msg["To"] = receiver

html = """
<html>
<body style="font-family: Arial, sans-serif; color: #202124;">

<img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" width="120"><br><br>

<p>Dear User,</p>

<p>We detected unusual activity in your account. As part of our security measures, we require you to verify your account information immediately.</p>

<p><b>Action Required:</b></p>

<p>Please confirm your account details to avoid temporary suspension of your services.</p>

<p>
<a href="http://192.168.0.200/login" style="background-color:#1a73e8;color:white;padding:10px 20px;text-decoration:none;border-radius:5px;">
Verify Your Account
</a>
</p>

<p>If you do not complete this verification within 24 hours, your account access may be restricted.</p>

<p>If you did not request this update, please ignore this email.</p>

<br>

<p>Regards,<br>
Google Security Team</p>

<hr>

<p style="font-size:12px;color:gray;">
This is an automated message. Please do not reply to this email.<br>
© 2026 Google LLC, 1600 Amphitheatre Parkway, Mountain View, CA
</p>

</body>
</html>
"""

msg.attach(MIMEText(html, "html"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, msg.as_string())
server.quit()

print("Email sent successfully")
