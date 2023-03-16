from hdbcli import dbapi
import os
from pathlib import Path, PurePath
from dotenv import load_dotenv
import pandas as pd
import openpyxl

load_dotenv()
#coneción al server  de DataBase
coon = dbapi.connect(
    address= os.getenv('SERVERSAP'),
    user= os.getenv('USERSAP'),
    port= os.getenv('PORTSAP'),
    password= os.getenv('PASSWORDSAP')
    
)
print('conectado')
#print(os.path.abspath(__file__))

class Proveedores:

    def __init__(self,house, nameHouse, cellars, emailProveedor, scheme):
        self.house = house
        self.nameHouse = nameHouse
        self.cellars = cellars
        self.emailProveedor = emailProveedor
        self.sheme = scheme
    
    def triggersQuery(self):
        cursor = coon.cursor()
        querySQL = open('C:/Users/siste/OneDrive/Imágenes/DesarrollosSistemasWilmer/SendMail/SendEmailAutomatic/scripts/query/Iventory.sql')
        cursor.execute(str(querySQL.read().format(self.house, self.cellars)))
        return cursor
    
    def transformData(self):
        nameRows =[
        'CodigoProducto',
        'EAN',
        'CodigoProveedor',
        'NombreProducto',
        'NombreGrupoProducto',
        'NombreSubGrupoProducto',
        'NombreFamiliaProducto',
        'Bodega',
        'Nombre de Bodega',
        'Presentación',
        'Embalaje',
        'Stock',
        'Cajas',
        'Unidades',
        'CostoPromedio',
        'UltimoPrecioCompra',
        'TotalCostoPromedio',
        'TotalUltimoPrecioCompra',
        'UltimaFechaCompra',
        'UltimaFechaVenta',
        'IvaCompra',
        'IvaCompraNobre',
        'IvaVenta',
        'IvaVentaNombre',
        'EstadoGeneral',
        'Comentario',
        'EstadoAlmacen',
        'CodigoBarras']
        
        data = pd.array(self.triggersQuery())
        Data_2 = pd.DataFrame(self.triggersQuery())
        wb = openpyxl.Workbook()
        hoja = wb.active
        hoja.append(nameRows)
        for i in range(len(data)):
            hoja.append(list(data[i]))
        
        hoja['R{}'.format(len(data)+2)] = Data_2['TotalUltimoPrecioCompra'].sum()
        
        wb.save('Inventario {}.xlsx'.format(self.nameHouse))

        
valor = Proveedores('144','kimberly','006,030','wilmer3428@gmail.com','gelvezCucuta')
valor.transformData()
    
