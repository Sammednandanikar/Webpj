import smtplib, ssl


def send_email(message):
     host = "smtp.gmail.com"
     port = 465  # Use port 465 for SMTP SSL
     username = "samnandanikar704@gmail.com"
     password = "cfqo kxyb vlgm uglf"
     receiver = "samnandanikar704@gmail.com"
     context = ssl.create_default_context()

     try:
          with smtplib.SMTP_SSL(host, port, context=context) as server:
               server.login(username, password)
               server.sendmail(username, receiver, message)
               print("Email sent successfully!")
     except Exception as e:
          print(f"Error sending email: {str(e)}")


