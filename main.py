from functions import send_emails_users, send_email

"""
sned some email to users
"""
choice = input("if you want to send email to one email press 1 if you want to send email to some emails  print 2")
if choice=="2":
   send_emails_users()
elif choice=="1":
   send_email()
else:
   print("please enter valid number")
   

