import csv
from pathlib import Path
"""
This function read csv file
Contain names and emails
Input: csv file
You should write file direction with name of csv file ex: - '/any_folder/csv_file_name.csv'

Output: return dictionary contain emails as keys and users names as value

"""
 
def read_csv(file_name):
    str_path = file_name
    path = Path(str_path)
    with open(path) as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       line_count = 0
       users = {}
       for row in csv_reader:
           if line_count == 0:
               line_count += 1
           else:
               users[row[1]] = row[0] 
    return(users)
    


"""
Send email function
Input: reciever email
Input: email message
Input: email subject
Output: Send email

"""
   
import smtplib, ssl

def send_email():
   sender_email = input("Type your email and press enter:")
   password = input("Type your password and press enter:")
   receiver_email = input("Type receiver email and press enter:")
   msg = input("Type email message and press enter:")
   subject = input("Type email subject and press enter:")
   port = 587  # For starttls
   smtp_server = "smtp.gmail.com"
   msg = """\
Subject: {}

{}""".format(subject,msg)
   context = ssl.create_default_context()    
   with smtplib.SMTP(smtp_server, port) as server:
       server.ehlo()  # Can be omitted
       server.starttls(context=context)
       server.ehlo()  # Can be omitted
       server.login(sender_email, password)
       server.sendmail(sender_email, receiver_email, msg)
   



#ex send_email('any@gmail.com',"hello from python","python task")



def send_emails_users():
   """

   You should enter your email and password to send emails

   """
   sender_email = input("Type your email and press enter: ")
   password = input("Type your password and press enter: ")
   """
   You should enter your csv file that contain names of users and emails

   """
   csv_file = input("""Type the pass of csv file contain names and emails in this format '/any_folder/csv_file_name.csv' 
   or 'csv_file_name.csv' if in the the same path:  """)
   users = read_csv(csv_file)
   

   """
   You should enter your message and Subject
   """
   msg = input("Type your email message want to send it to all users:  ")
   subject = input("Type your email subject want to send it to all users:  ")
   
   message = """\
Subject: {}

{}""".format(subject,msg)
   
   
   
   context = ssl.create_default_context()
   with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
       server.login(sender_email, password)
       for email  in users:
          server.sendmail(
             sender_email,
             email,
             message
             )
          print('this mail is sent to '+users[email])

"""
sned some email to users


"""

if '__name' == '__main__':
   pass

