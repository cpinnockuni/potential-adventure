import smtplib
from email.mime.text import MIMEText


def send_confirmation_email(recipient_email):

    try: 
     smtp_server = 'smtp.gmail.com'
     smtp_port = 587
     smtp_username = 'your_email@gmail.com' 
     smtp_password = 'your_email_password'  
     sender_email = 'your_email@gmail.com'

     msg = MIMEText('Your email has been confirmed. Thank you!')
     msg['Subject'] = 'Confirmation Email'
     msg['From'] = sender_email
     msg['To'] = recipient_email

     smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
     smtp_conn.ehlo()
     smtp_conn.starttls()
     smtp_conn.ehlo()
     smtp_conn.login(smtp_username, smtp_password)
     #The function will only need to call indiviually so no need for looping
     smtp_conn.sendmail(sender_email, [recipient_email], msg.as_string())
     smtp_conn.quit()

    # return a message to the customer
     return 'Email confirmation successful!'
    
    except Exception as error:
       print(error)





