from email.message import EmailMessage
import smtplib
from dataGeneration import Proveedores
import os
from dotenv import load_dotenv 

load_dotenv()
class sendMail():

    def __init__(self,sender, addressee,nameCellers,nameHouse):
        self._sender = sender
        self.addressee = addressee
        self.menssage = ''
        self.affair = 'Envio Prueba'
        self.serverSMTP = "smtp.gmail.com"
        self.nameCellers = nameCellers
        self.nameHouse = nameHouse
        self.portServerSMTP = 465

    
    #Getters  del objeto sendMail
    @property
    def sender(self):
        return self._sender
    
    #Setter del objeto sendMail
    @sender.setter
    def set_sender(self,sender):
        self._sender = sender
    
    def set_menssage(self):
        text = open ('C:/Users/siste/OneDrive/Imágenes/DesarrollosSistemasWilmer/SendMail/SendEmailAutomatic/scripts/menssage.html','r')
        self.menssage = str(text.read())
        self.menssage = self.menssage.format(self.nameHouse, self.nameCellers)
        self.menssage =self.menssage.replace('#','{')
        self.menssage =self.menssage.replace('+','}')
        return self.menssage

    def sendProviderEmail(self,nameArchive):
        email = EmailMessage()
        email["From"] = self.sender
        email["To"] = (self.addressee)
        email["Subject"] = self.affair
        
        email.set_content(self.set_menssage(), subtype= 'html')
        with open(os.path.join(os.getcwd(),'SendEmailAutomatic/scripts/'+nameArchive),'rb') as f:
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
    

        
        
        
