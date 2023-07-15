import re

import smtplib

import lucy
from lucy import engines
from lucy import settings
from lucy.core.console import ConsoleManager as cm
from lucy.utils.contact_list import  EMAIL_CONTACTS
class Mail:
   def __init__(self):
       self.email_user = settings.EMAIL_CONFIG.get('user')
       self.password   =  settings.EMAIL_CONFIG.get('password')
       self.email_recepient=None
       self.server = smtplib.SMTP('smtp.gmail.com', 587)
       cm.console_output("Email sever prepared")
   @staticmethod
   def validate_email(email):
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat, email):
            return True
        return False
   def connect(self):
       try:
           lucy.output_engine.respond("loggin in as "+ self.email_user)
           self.server.ehlo()
           self.server.starttls()
           self.server.login(self.email_user, self.password)
           #self.server.starttls()
           return True
       except smtplib.SMTPAuthenticationError:
           lucy.output_engine.respond("Unable to login to your mail id")
           return False
       except Exception as e:
          lucy.output_engine("Something went wrong")
          self.cm.console_output("error:"+ str(e))
          return False

   def send_to_recepient(self, email_recepient,message):
       self.server.sendmail(self.email_user, self.email_recepient, message)
       self.server.quit()
   @classmethod
   def send_email(cls,subject=None):
         cm.console_output(f"subject received {subject}")
         mail=Mail()
         if(mail.connect() is False):
            return False
         if( not subject):
             lucy.output_engine.respond("Recepient email")
             subject = lucy.input_engine.recognize_input()

         if( not cls.validate_email(subject)):
               subject=EMAIL_CONTACTS.get(subject)
         if(not subject):
             lucy.output_engine.respond('Cant send email to the specified recepient')
         mail.email_recepient=subject
         cm.console_output(f"recepient received:  {mail.email_recepient}")
         lucy.output_engine.respond('your message sir')
         message=lucy.input_engine.recognize_input()
         mail.send_to_recepient(mail.email_recepient,message)
         lucy.output_engine.respond("Email sent")

if __name__ == '__main__':
       Mail.send_email("ehsonmiraz@gmail.com")
