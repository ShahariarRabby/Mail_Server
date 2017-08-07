# coding: utf-8
# ! /usr/bin/python
__author__ = 'Shahariar Rabby'

# This is main send mail file, All function define here.
# other file import it and work

# ### Send email Clint
# #### Importing all dependency

# In[33]:

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import getpass


# #### User Details Function

# In[36]:

def user():
    # ORG_EMAIL = "@gmail.com"
    # FROM_EMAIL = "your email" + ORG_EMAIL
    # FROM_PWD = "your pass"
    FROM_EMAIL = raw_input("Insert Your Email : ")
    #FROM_PWD = getpass.getpass("Input Your Password : ") getpass is not working in my terminal, try yours too
    FROM_PWD = raw_input("Input Your Password : ")
    return FROM_EMAIL,FROM_PWD


# ### Login function
# In this function we call user details function and get the user name and password, Than we use those details for IMAP login.
# ** SMTP is Simple Mail Transfer Protocol**

# In[55]:

def login():
    gmail_user, gmail_pwd = user() #calling the user function for get user details
    smtpserver = smtplib.SMTP("smtp.gmail.com",587) #Declaring gmail SMTP server address and port 
    smtpserver.starttls() #Starting tls service, Transport Layer Security (TLS) are cryptographic protocols that provide communications security over a computer network.
    smtpserver.login(gmail_user, gmail_pwd) #Login to Gmail server using TLS
    print 'Login successful'
    return smtpserver


# ### Send mail function. 
# This function takes 5 argument. 1. Login Data. 2. To Email 3. From Email  4. HTML format massage 5. Normal text 
# 
# **The HTML message, is best and preferred.**

# In[75]:

# text = "Hi!\n5633222222222222222http://www.python.org"
# html = """\
#     <html>
#       <head></head>
#       <body>
#         <p>Hi!<br>
#            How are you?<br>
    
#            Here is the <a href="http://www.python.org">link</a> you wanted.
#         </p>
#       </body>
#     </html>
#     """
def Send_Mail(smtpserver,TO_EMAIL,text=None,html=None,subject='Subject',FROM_EMAIL='Shahariar'):
# Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative') # In turn, use text/plain and text/html parts within the multipart/alternative part.
    msg['Subject'] = subject #Subject of the message
    msg['From'] = formataddr((str(Header(FROM_EMAIL, 'utf-8')), FROM_EMAIL)) #Adding custom Sender Name
    msg['To'] = TO_EMAIL #Assining Reciver email

    part1 = MIMEText(text, 'plain') #adding text part of mail
    part2 = MIMEText(html, 'html') #Adding HTMLpart of mail

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1) #attach Plain text
    msg.attach(part2) #attach HTML text

    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    try:
        smtpserver.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
        print " Message Send"
        smtpserver.quit() #stopping server
    except Exception:
        print Exception



