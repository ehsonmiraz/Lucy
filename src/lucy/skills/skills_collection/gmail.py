import lucy
from lucy import engines
import smtplib
from lucy import settings
from lucy.core.console import ConsoleManager
class Mail:
   def __init__(self):
       self.email_user = settings.EMAIL_CONFIG.get('user')
       self.password   =  settings.EMAIL_CONFIG.get('password')
       self.email_recepient=None
       self.server = smtplib.SMTP('smtp.gmail.com', 587)
       self.cm=ConsoleManager()
       self.cm.console_output("Email sever prepared")

   def connect(self):
       try:
           lucy.output_engine.say("loggin in as "+ self.email_user)
           self.server.ehlo()
           self.server.starttls()
           self.server.login(self.email_user, self.password)
           #self.server.starttls()
           return True
       except smtplib.SMTPAuthenticationError:
           lucy.output_engine.say("Unable to login to your mail id")
           return False
       except Exception as e:
          lucy.output_engine("Something went wrong")
          self.cm.console_output("error:"+ str(e))
          return False

   def send_to_recepient(self, email_recepient,message):
       self.server.sendmail(self.email_user, self.email_recepient, message)
       self.server.quit()
   @staticmethod
   def send_email():
         mail=Mail()
         if(mail.connect() is False):
            return False
         lucy.output_engine.say("Recepient email")
         mail.email_recepient = lucy.input_engine.recognize_input()

         try:
            if ('my mail' in mail.email_recepient or mail.email_recepient in 'to me ') and len(mail.email_recepient)!=0:
                 email_recepient = 'ehsonmiraz@gmail.com'
         except TypeError:
                   return False
         mail.cm.console_output(mail.email_recepient)
         lucy.output_engine.say('your message sir')
         message=lucy.input_engine.recognize_input()
         mail.send_to_recepient(mail.email_recepient,message)
         lucy.output_engine.say("Email sent")

if __name__ == '__main__':
       Mail.send_email()
