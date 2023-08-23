from components.converTextData import ConverText
from components.dataExtract import extracData
from model.modelSQL import Structure

"""
Modulo Encardo de la conexión a la base y generación del archivo de ecxel 
"""


class SeriesInvoiceSend(Structure):
    """
    Se encarga de generar el objeto del proveedor junto con el inventario que maneja
    """

    def __init__(self, schemeDB):
        self.schemeDB = schemeDB

    def transformData(self):
        text = ConverText.converTextFormatSQL('seriesInvoice.sql', self.schemeDB)
        datas, nameRows = extracData(text)
        return datas, nameRows