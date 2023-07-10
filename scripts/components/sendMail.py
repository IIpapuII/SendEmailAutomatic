from email.message import EmailMessage
import smtplib
from .dataExtract import getFilePath, getFilePathsEmail
from dotenv import load_dotenv 
import os
""" Modulo Encarado de Enviar correos"""
load_dotenv()
class sendMailEcxel():
    """ Clase Encargada de Gestinar el envio del correos con un archivo o sin archivo"""
    def __init__(self,sender: str, addressee: str, affair:str, menssage:str, nameArchive:str, password:str):
        self._sender = sender
        self.addressee = addressee
        self.menssage = menssage
        self.nameArchive = nameArchive
        #self.affair = 'Inventario de {} a corte de {}'
        self.affair = affair
        self.serverSMTP = "smtp-mail.outlook.com"
        self.portServerSMTP = 587
        self.password = password

    
    #Getters  del objeto sendMail
    @property
    def sender(self):
        return self._sender
    
    #Setter del objeto sendMail
    @sender.setter
    def set_sender(self,sender):
        self._sender = sender
    
    def sendProviderEmail(self):
        email = EmailMessage()
        email["From"] = self.sender
        email["To"] = (self.addressee)
        email["Subject"] = self.affair
        
        email.set_content(self.menssage, subtype= 'html')
        if self.nameArchive != None:
            with open(getFilePath('docs',self.nameArchive),'rb') as f:
                email.add_attachment(
                    f.read(),
                    filename = self.nameArchive,
                    maintype = "application",
                    subtype = "vnd.ms-excel"
                )
        
        smtp = smtplib.SMTP(self.serverSMTP, self.portServerSMTP)
        smtp.starttls()
        smtp.login(self.sender, self.password)
        smtp.sendmail(self.sender,
                      self.addressee,
                      email.as_string())
        print('Mensaje Enviado')

class sendMailEcxelMultiple():
    """ Clase encargada de generar el envio de correo con multiples adjuntos"""
    def __init__(self,sender: str, addressee: str, affair:str, menssage:str, nameArchive, password:str):
        self._sender = sender
        self.addressee = addressee
        self.menssage = menssage
        self.nameArchive = nameArchive
        #self.affair = 'Inventario de {} a corte de {}'
        self.affair = affair
        self.serverSMTP = "smtp-mail.outlook.com"
        self.portServerSMTP = 587
        self.password = password

    
    #Getters  del objeto sendMail
    @property
    def sender(self):
        return self._sender
    
    #Setter del objeto sendMail
    @sender.setter
    def set_sender(self,sender):
        self._sender = sender
    
    def sendProviderEmail(self):
        email = EmailMessage()
        email["From"] = self.sender
        email["To"] = (self.addressee)
        email["Subject"] = self.affair
        
        email.set_content(self.menssage, subtype= 'html')
        if self.nameArchive != None:
            fileNames = self.nameArchive
            filePaths = getFilePathsEmail('docs',fileNames)
            for filePath in filePaths:
                with open(filePath,'rb') as f:
                    fileName = os.path.basename(filePath)
                    email.add_attachment(
                        f.read(),
                        filename = str(fileName),
                        maintype = "application",
                        subtype = "vnd.ms-excel"
                )
        
        smtp = smtplib.SMTP(self.serverSMTP, self.portServerSMTP)
        smtp.starttls()
        smtp.login(self.sender, self.password)
        smtp.sendmail(self.sender,
                      self.addressee,
                      email.as_string())
        print('Mensaje Enviado')
        
        
        
