# coding: utf-8
# ! /usr/bin/python
__author__ = 'Shahariar Rabby'


# # Sendy
# ### Importing Send mail file

# In[6]:

from Sendmail import *


# ** Take user email, text plan massage, HTML file **

# In[7]:

TO_EMAIL = raw_input("Enter reciver email : ") #Taking Reciver email as input
subject = raw_input("Enter Mail Subject : ") #taking mail subject
text = raw_input("Enter Plain message(or html format) : ") #Taking plane massage as input
filename = raw_input('Enter file name with location(if any) : ')
try:
    file = open(filename,'r') #reading HTML format message
    html = file.read() 
except:
    html = text

# **Calling send mail and sending mail **

# In[8]:

Send_Mail(login(),TO_EMAIL=TO_EMAIL,text=text,html=html,subject=subject)

