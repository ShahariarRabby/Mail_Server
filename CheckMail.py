# coding: utf-8
# ! /usr/bin/python
__author__ = 'Shahariar Rabby'

#This file will check your mail from your gmail server

from ReceiveMail import *
read = int(raw_input("Enter how many message you want to read : "))
read_email_from_gmail(read=read)
