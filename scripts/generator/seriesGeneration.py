from components.converTextData import ConverText
from components.dataExtract import extracData
from model.modelSQL import Structure

"""
Modulo encardo de la conexión a la base y generación de informacion
"""

class SeriesInvoiceSend(Structure):
    """
    Se encarga de generar las series de facturas y notas credito, y sus respectivas fechas de vencimiento
    """

    def __init__(self, schemeDB, table):
        self.schemeDB = schemeDB
        self.table = table

    def transformData(self):
        text = ConverText.converTextFormatSQL('seriesInvoice.sql', self.schemeDB, self.table)
        datas, nameRows = extracData(text)
        return datas, nameRows