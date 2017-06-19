# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:33:50 2016

@author: JohannesMHeinrich
"""


from time import localtime, strftime
from class_email_bot import e_mail



def start_email_bot(p_t):
    
    # create instance of email bot
    emailbot = e_mail()
    
    # check emails and collect querys
    requests = emailbot.read_messages()
    for i in range(len(requests)):
                
        # build answer ------------------  
        question = requests[i][2]
        
        if question in['pressure','Pressure']: 
            
            answer = 'you were asking for the pressure. Currently it is at ' + str(p_t)
                        
        else:          
            answer = """
i am very sorry, but i did not understand the question.
------------
up to now i only have one function: i can answer you if you ask for the pressure.
in order to do so, send an email with the topic "pressure", "Pressure" or "p".
            """
        # end build answer ------------------
            
        answer_adress = requests[i][3]
        
        answer_topic = 'Your request from the ' + str(strftime("%a, %d %b %Y %H:%M:%S +0100", localtime()))
     
   
        # send answer   
        emailbot.send_message2([answer_adress], answer_topic, answer)
        
        
        
        
        
        