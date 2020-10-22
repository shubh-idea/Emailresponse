import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import imaplib,email


user = 'yourmail@gmail.com.com'
password = 'yourpass'
imap_url = 'imap.gmail.com'


# Function to get email content part i.e its body part 
def get_body(msg): 
    if msg.is_multipart(): 
        return get_body(msg.get_payload(0)) 
    else: 
        return msg.get_payload(None, True) 
  
  
  # Function to search for a key value pair  
def search(key, value, con):  
    result, data = con.search(None, key, '"{}"'.format(value)) 
    return data 
    
    
    # Function to get the list of emails under this label 
def get_emails(result_bytes): 
    msgs = [] # all the email data are pushed inside an array 
    for num in result_bytes[0].split(): 
        typ, data = con.fetch(num, '(RFC822)') 
        msgs.append(data) 
  
    return msgs 
    
    
# this is done to make SSL connnection with GMAIL 
con = imaplib.IMAP4_SSL(imap_url)  


# logging the user in 
con.login(user, password)


# calling function to check for email under this label 
con.select('Inbox')
result,data=con.fetch(b'40','(RFC822)')


raw=email.message_from_bytes(data[0][1])
print(raw)

#Search operation
msgs=get_emails(search('FROM','sender_id',con))
for msg in msgs:
    print(get_body(email.message_from_bytes(msg[0][1])))


