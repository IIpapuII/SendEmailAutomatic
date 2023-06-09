from email.message import EmailMessage
import smtplib
import os
from datetime import datetime
from dotenv import load_dotenv 
""" Modulo Encarado de Enviar correos"""
load_dotenv()
class sendMailEcxel():
    """ Clase Encargada de Gestinar el envio del correo a los proveedores"""
    def __init__(self,sender, addressee, affair, menssage, nameArchive):
        self._sender = sender
        self.addressee = addressee
        self.menssage = menssage
        self.nameArchive = nameArchive
        #self.affair = 'Inventario de {} a corte de {}'
        self.affair = affair
        self.serverSMTP = "smtp.gmail.com"
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
        text = open (os.path.join(os.path.dirname(os.path.abspath('templates')), 'Scripts/templates/menssage.html'),'r')
        self.menssage = str(text.read())
        self.menssage = self.menssage.format(self.nameHouse, self.nameCellers)
        self.menssage =self.menssage.replace('#','{')
        self.menssage =self.menssage.replace('+','}')
        return self.menssage

    def sendProviderEmail(self):
        email = EmailMessage()
        email["From"] = self.sender
        email["To"] = (self.addressee)
        email["Subject"] = self.affair
        
        email.set_content(self.menssage, subtype= 'html')
        with open(os.path.join(os.path.dirname(os.path.abspath('docs')),'scripts/docs/'+self.nameArchive),'rb') as f:
            email.add_attachment(
                f.read(),
                filename = self.nameArchive,
                maintype = "application",
                subtype = "vnd.ms-excel"
            )
        
        smtp = smtplib.SMTP_SSL(self.serverSMTP, self.portServerSMTP)
        smtp.login(self.sender, os.getenv('PASSWORDEMAIL'))
        smtp.sendmail(self.sender,
                      self.addressee,
                      email.as_string())
        print('Mensaje Enviado')
    

        
        
        
