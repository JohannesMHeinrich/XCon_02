# -*- coding: utf-8 -*-
"""
Created on Wed Dec 07 18:18:01 2016

@author: JohannesMHeinrich
"""
import smtplib
from email.mime.text import MIMEText

import poplib
from email import parser


import os

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage



class e_mail():
    def __init__(self):

        self.sender = 'linear.trap@gmail.com'
        
    def send_message(self, recipients, the_answer_headline, the_answer):
        # make up message
        msg = MIMEText(the_answer)
        msg['Subject'] = the_answer_headline
        msg['From'] = self.sender
        msg['To'] = ", ".join(recipients)

        # sending
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(self.sender, 'pw_lin_trap')
        session.sendmail(self.sender, recipients, msg.as_string())
        session.quit()


    def send_message2(self,recipients, the_answer_headline, the_answer):
        img_data = open('pic_ion_pump.png', 'rb').read()
        msg = MIMEMultipart()
        msg['Subject'] = the_answer_headline
        msg['From'] = self.sender
        msg['To'] = ", ".join(recipients)
    
        text = MIMEText(the_answer)
        msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename('pic_ion_pump.png'))
        msg.attach(image)
    
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(self.sender, 'pw_lin_trap')
        s.sendmail(self.sender, recipients, msg.as_string())
        s.quit()        
        
    def read_messages(self):
        pop_conn = poplib.POP3_SSL('pop.gmail.com')
        pop_conn.user('linear.trap')
        pop_conn.pass_('pw_lin_trap')
        
        
        #Get messages from server:
        messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
        # Concat message pieces:
        messages = [str('\n').join([str(mssg_part) for mssg_part in mssg[1]]) for mssg in messages]
        #Parse message intom an email object:
        messages = [parser.Parser().parsestr(mssg) for mssg in messages]
        
        
        
        # since the parse methods didn't provide me with the information i wanted here
        # below is a filter to search the body of the emails. it saves only
        # the orders = [[date_string, from_string, subject_string],...]
        
        the_orders = []
        
        for message in messages:
            
            message_as_string = message.get_payload()
            
        
            # find the time of the message and put it in date_string
            to_search_for = str("b'Date: ")
            
            date_start = message_as_string.find(to_search_for)  
            date_stop = message_as_string.find(str("'"), date_start + len(to_search_for))
            date_string = message_as_string[date_start + len(to_search_for):date_stop]    
            
        
            # find the sender of the message and put it in from_string
            to_search_for = str("b'From: ")
            
            from_start = message_as_string.find(to_search_for)  
            from_stop = message_as_string.find(str("'"), from_start + len(to_search_for))
            from_string = message_as_string[from_start + len(to_search_for):from_stop]
            
        
            # find the subject of the message and put it in subject_string
            to_search_for = str("b'Subject: ")
                
            subject_start = message_as_string.find(to_search_for)    
            subject_stop = message_as_string.find(str("'"), subject_start + len(to_search_for))
            subject_string = message_as_string[subject_start + len(to_search_for):subject_stop]
            
        
        
            # get the email adress of the sender of the message and put it in from_string
            to_search_for = str("<")
                
            adress_start = from_string.find(to_search_for)    
            adress_stop = from_string.find(str(">"), subject_start + len(to_search_for))
            adress_string = from_string[adress_start + len(to_search_for):adress_stop]
            
            the_orders.append([date_string,from_string,subject_string,adress_string])   
                    
        
        pop_conn.quit()
        
        
        
        return the_orders










#import os
#import smtplib
#from email.mime.text import MIMEText
#from email.mime.image import MIMEImage
#from email.mime.multipart import MIMEMultipart


#def SendMail(ImgFileName):
#    img_data = open(ImgFileName, 'rb').read()
#    msg = MIMEMultipart()
#    msg['Subject'] = 'subject'
#    msg['From'] = 'e@mail.cc'
#    msg['To'] = 'e@mail.cc'
#
#    text = MIMEText("test")
#    msg.attach(text)
#    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
#    msg.attach(image)
#
#    s = smtplib.SMTP(Server, Port)
#    s.ehlo()
#    s.starttls()
#    s.ehlo()
#    s.login(UserName, UserPassword)
#    s.sendmail(From, To, msg.as_string())
#    s.quit() 