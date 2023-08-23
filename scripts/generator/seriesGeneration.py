from components.converTextData import ConverText
from components.dataExtract import extracData
from model.modelSQL import Structure

"""
Modulo encardo de la conexión a la base y generación de informacion
"""

class SeriesInvoiceSend(Structure):
    """
    Se encarga de generar las series de facturas y sus fechas de vencimiento
    """

    def __init__(self, schemeDB):
        self.schemeDB = schemeDB

    def transformData(self):
        text = ConverText.converTextFormatSQL('seriesInvoice.sql', self.schemeDB)
        datas, nameRows = extracData(text)
        return datas, nameRows