from components.dataExtract import extracData, getFilePath
from components.converTextData import ConverText
from components.transformData import dataFusion
from model.modelSQL import Structure


class SendIcomes(Structure):
    
    def __init__(self, schemeDB, wareHouse, initDate=None, endDate=None) -> None:
        super().__init__(schemeDB, wareHouse, initDate, endDate)

    def controllerIcome(self):
        text = ConverText.converTextFormatSQL('income.sql',self.initDate, self.endDate, self.schemeDB, self.wareHouse)
        data, description  =extracData(text)
        if not data:
            return False
        else:
            dataFusion(data,description).to_excel(getFilePath('docs','IngresoMercancia.xlsx'), index=None)
            return True