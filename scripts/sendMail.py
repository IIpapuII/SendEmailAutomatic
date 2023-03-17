from email.message import EmailMessage
import smtplib
from dataGeneration import Proveedores
import os
from dotenv import load_dotenv 

load_dotenv()
class sendMail():

    def __init__(self,sender, addressee, menssage):
        self._sender = sender
        self._addressee = addressee
        self._menssage = menssage
        self.affair = 'Envio Prueba'
        self.serverSMTP = "smtp.gmail.com"
        self.portServerSMTP = 465

    
    #Getters  del objeto sendMail
    @property
    def sender(self):
        return self._sender
    
    @property
    def addressee(self):
        return self._addressee
    
    @property
    def menssage(self):
        return self._menssage
    
    #Setter del objeto sendMail
    @sender.setter
    def set_sender(self,sender):
        self._sender = sender
    
    def sendProviderEmail(self,nameArchive):
        email = EmailMessage()
        email["From"] = self.sender
        email["To"] = self.addressee
        email["Subject"] = self.affair
        
        email.set_content(self.menssage, subtype= 'html')
        with open(nameArchive,'rb') as f:
            email.add_attachment(
                f.read(),
                filename = nameArchive,
                maintype = "application",
                subtype = "vnd.ms-excel"
            )
        
        smtp = smtplib.SMTP_SSL(self.serverSMTP, self.portServerSMTP)
        smtp.login(self.sender, os.getenv('PASSWORDEMAIL'))
        smtp.sendmail(self.sender,
                      self.addressee,
                      email.as_string())
        print('Mensaje Enviado')
    

        
        
        
