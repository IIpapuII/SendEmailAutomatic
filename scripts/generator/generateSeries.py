from components.dataExtract import extracData
from components.converTextData import ConverText
from components.transformData import dataFusion, exportExcel
from model.modelSQL import Structure

class SendSeries (Structure):

    def __init__(self, schemeDB, wareHouse, initDate=None, endDate=None) -> None:
        super().__init__(schemeDB, wareHouse, initDate, endDate)

    def controllerSeries(self):
        text = ConverText.converTextFormatSQL('seriesInvoice.sql',self.initDate, self.endDate, self.schemeDB, self.wareHouse)
        data, description = extracData(text)
        if not data:
            return False
        else:
            return True