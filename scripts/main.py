
from sendMail import sendMail
from dataGeneration import Proveedores

if __name__ == "__main__":
    provedor = Proveedores('144','Kimberly', '006,030,008',['compras.cede@gmail.com','compras.distribucionesgelvez@gmail.com'],'GELVEZ')
    provedor.transformData()
    data = sendMail('sistemasgelvez@gmail.com',provedor.emailProveedor)
    data.sendProviderEmail(provedor.nameArchivo())