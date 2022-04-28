from fileinput import filename
import smtplib 
from email.message import EmailMessage
import imghdr

msg = EmailMessage()
msg["Subject"] = "This is to test my Email"
msg["From"] = 'victor.m@enlacellc.com'
msg["To"] = 'victordmtz@hotmail.com'
#this option if for plain text
content = f""" This <h1>email</h1> it to test the functionality
    of my messages or may 
    email service    
    """
msg.set_content(content)
# for html mail
msg.add_alternative(F'''\
    <!DOCTYPE html>
    <h1>This is an HTML Message</h1>
    <p>{content}</p>
    </html>
''', subtype="html")

with open("account.png", "rb") as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
# Name is optional, but if not added, on will be given automatically. 
# use loop for multiple files
#pdf - maintype = Application .... subtype= octet-stream (generic information)
msg.add_attachment(file_data, maintype = "image", subtype = file_type, filename=file_name )

with smtplib.SMTP_SSL('smtp.flockmail.com',465) as smtp:
    account = 'victor.m@enlacellc.com'
    pwd = "--------"
    smtp.login(account, pwd)
    smtp.send_message(msg)
    