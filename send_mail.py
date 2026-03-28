import smtplib
from email.mime.text import MIMEText

sender = "it.admin.support.g00gle@gmail.com"
receiver = "mitnick.user@gmail.com"
password = "your_app_password"

html = """
Subject: Critical Security Update Required

<html>
<body>
<p>Dear User,<br><br>

Click here to update your account:<br><br>

<a href="http://192.168.0.200/login">
https://accounts.google.com/security-update
</a>

<br><br>
Regards,<br>
Google Security Team
</p>
</body>
</html>
"""

msg = MIMEText(html, "html")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, msg.as_string())
server.quit()

print("Email sent successfully")
