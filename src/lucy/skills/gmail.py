from speak import Speak as s
import smtplib
from mic import Mic


class Mail:
   def __init__(self):

       self.email_user = EMAIL_USER
       self.password   =  PASSWORD
       self.email_recepient=None
       self.server = smtplib.SMTP('smtp.gmail.com', 587)
       print("server made")

   def connect(self):
       try:
           s.say("loggin in as "+ EMAIL_NAME)
           self.server.ehlo()
           self.server.starttls()
           self.server.login(self.email_user, self.password)
           #self.server.starttls()
           return True
       except smtplib.SMTPAuthenticationError:
           s.say("Unable to login to your mail id")
           return False
       except Exception as e:
          s.say("Something went wrong")
          print("error:"+ str(e))
          return False

   def send_to_recepient(self, email_recepient,message):
       self.server.sendmail(self.email_user, self.email_recepient, message)
       self.server.quit()

   def send_email(self):
         if(self.connect() is False):
            return False
         s.say("Recepient email")
         self.email_recepient = Mic.mic()

         try:
            if ('my mail' in self.email_recepient or self.email_recepient in 'to me ') and len(self.email_recepient)!=0:
                 email_recepient = 'ehsonmiraz@gmail.com'
         except TypeError:
                   return False
         print(self.email_recepient)
         s.say('your message sir')
         message=Mic.mic()
         self.send_to_recepient(self.email_recepient,message)
         s.say("Email sent")

if __name__ == '__main__':
       mail=Mail()
       mail.send_email()
