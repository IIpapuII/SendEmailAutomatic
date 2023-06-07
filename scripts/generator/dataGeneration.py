from hdbcli import dbapi
import os
from dotenv import load_dotenv
import pandas as pd
import openpyxl
from model.conectDB import conect

"""
Modulo Encardo de la conexión a la base y generación del archivo de ecxel 
"""
coon = conect()
class Proveedores:
    """
    Se encarga de generar el objeto del provedor junto con el iventario que maneja
    """
    def __init__(self,house, nameHouse, cellars, scheme):
        self.house = house
        self.nameHouse = nameHouse
        self.cellars = cellars
        self.sheme = scheme
    
    def triggersQuery(self):
        cursor = coon.cursor()
        querySQL = open(os.path.join(os.path.dirname(os.path.abspath('script')),'scripts/query/Iventory.sql'))
        cursor.execute(str(querySQL.read().format(self.house, self.cellars ,self.sheme)))
        return cursor.fetchall()
    
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
        Data_2 = pd.DataFrame(self.triggersQuery(), columns= nameRows )
        wb = openpyxl.Workbook()
        hoja = wb.active
        hoja.append(nameRows)
        for i in range(len(data)):
            hoja.append(list(data[i]))
        
        hoja['R{}'.format(len(data)+2)] = Data_2['TotalUltimoPrecioCompra'].sum()
        
        wb.save(os.path.join(os.path.dirname(os.path.abspath('docs')),'scripts/docs/'+self.nameArchivo()))

    def nameArchivo(self):
        return 'Iventario {}.xlsx'.format(self.nameHouse)

    