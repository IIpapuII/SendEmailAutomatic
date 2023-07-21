from components.dataExtract import extracData
from components.converTextData import ConverText
from components.transformData import dataFusion
from model.modelSQL import Structure
import os

class SendInventoryReport (Structure):

    def __init__(self, schemeDB, wareHouse, initDate=None, endDate=None) -> None:
        super().__init__(schemeDB, wareHouse, initDate, endDate)

    def controllerInventoryReport(self):
        text = ConverText.converTextFormatSQL('IrInventoryReport.sql',self.initDate, self.endDate, self.schemeDB, self.wareHouse)
        data, description = extracData(text)
        if not data:
            return False
        else:
            dataFusion(data,description).to_excel(os.path.join(os.path.dirname(os.path.abspath('docs')),'scripts/docs/'+'Productos con mas de 60 dias en bodega.xlsx'))
            return True