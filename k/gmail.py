
class mail:

  
 def emails():
   from speak import speak as s
   import smtplib
   from mic import mic
   email_user='ehsonmiraz@gmail.com'
   password='g13pics0077'
   server=smtplib.SMTP('smtp.gmail.com',587)
   server.starttls()
   try:
     server.login(email_user,password)

     s.say("to")
     email_send=mic.mic()
     print(email_send)
     s.say("loggin in as ehson miraaz")
     try: 
      if ('mail' in email_send or email_send in 'to me ') and len(email_send) is not 0:
       email_send='ehsonmiraz@gmail.com'
     except TypeError:
      return
     print(email_send)
     s.say('your message sir')
     message=mic.mic()
     server.sendmail(email_user,email_send,message)
     server .quit()
     print('Email sent')
     s.say("Email sent")
   except smtplib.SMTPAuthenticationError:
       s.say("sir your password , has been changed . make sure you have changed it .")  
 
 if __name__ == '__main__':
       emails()
