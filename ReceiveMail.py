# coding: utf-8
# ! /usr/bin/python
__author__ = 'Shahariar Rabby'

# main recive mail file. All recive mail, check mail, server file import it
# All function define here


# # Recive Mail
# #### Importing all dependency

# In[ ]:

import email
import imaplib
import ctypes
import getpass
import threading
from playsound import playsound


# #### User Details Function

# In[ ]:

def user():
#    ORG_EMAIL = "@gmail.com"
#    FROM_EMAIL = "your email" + ORG_EMAIL
#    FROM_PWD = "your pass"
    FROM_EMAIL = raw_input("Insert Your Email : ")
    #FROM_PWD = getpass.getpass("Input Your Password : ") getpass is not working in my terminal, try yours too
    FROM_PWD = raw_input("Input Your Password : ")
    return FROM_EMAIL,FROM_PWD


# ### Login function
# In this function we call user details function and get the user name and password, Than we use those details for IMAP login.
# ** IMAP (Internet Message Access Protocol) is a standard email protocol that stores email messages on a mail server, but allows the end user to view and manipulate the messages as though they were stored locally on the end user's computing device(s).**

# In[ ]:

def login():
    FROM_EMAIL,FROM_PWD = user()
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    mail.login(FROM_EMAIL, FROM_PWD)
    mail.select("INBOX")
    print 'Login successful'
    return mail


# In[ ]:
mail = login()

def read_email_from_gmail(read=10):
    try:
        type, data = mail.search(None, 'ALL') #Sharching all message frm inbox
        mail_ids = data[0] #Assining all mail id to mail_ids Variable
        id_list = mail_ids.split() #putting all mail id to id_list array
        first_email_id = int(id_list[0]) #getting first mail id
        latest_email_id = int(id_list[-1]) #getting last mail id

        for i in range(latest_email_id, latest_email_id - read, -1): #this loop reading last 10 message
            typ, data = mail.fetch(i, '(RFC822)') #fatch mail data, and putting it a tuple where i=tuple no and 'RFC822' is mail

            for response_part in data: #reading all data from i no message
                if isinstance(response_part, tuple): 
                    msg = email.message_from_string(response_part[1]) #Reading mail
                    email_subject = msg['subject'] #Email subject
                    email_from = msg['from'] #Sender address
                    print 'From : ' + email_from
                    print 'Subject : ' + email_subject
                    print "Read mail: https://gmail.com\n"

    except Exception, e:
        print (str(e)) #printing if there is any error


# ## Mail Server
# **This will start a server that notify user when there is new email**

# In[ ]:

def loop():
    mail.select("INBOX") #Selecting inbox
    n = 0
    (retcode, messages) = mail.search(None, '(UNSEEN)') #sharching unseen mail
    if retcode == 'OK': #if unseen
        for num in messages[0].split():
            n = n + 1 
            print n #print message number
            typ, data = mail.fetch(num, '(RFC822)') #fatching mail
            for response_part in data:
                if isinstance(response_part, tuple):
                    original = email.message_from_string(response_part[1])
                    print original['From']
                    data = original['Subject']
                    playsound('demonstrative.wav') #play sound when mail recive
                    print data
                    print "Read mail: https://gmail.com"
                    if data == 'eject': #make mail status unseen to seen
                        ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
                    typ, data = mail.store(num, '+FLAGS', '\\Seen')

    from sys import stdout
    stdout.write(str('#')) #printing mail server is alive

# In[ ]:

def server():
    loop()
    threading.Timer(15, server).start() #calling function evey 15 sec



