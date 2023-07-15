from model.modelSQL import Structure
from components.converTextData import ConverText
from components.dataExtract import extracData

class ParettoSales(Structure):
    def __init__(self, schemeDB, 
                 wareHouse, 
                 initDate=None, 
                 endDate=None,
                 wareCellers = None ) -> None:
        super().__init__(schemeDB, wareHouse, initDate, endDate)
        self.wareCellers = wareCellers
    
    def Controlle(self):
        text = ConverText.converTextFormatSQL('ParretoSales.sql',
                                              self.schemeDB, self.wareHouse, self.initDate, self.endDate, self.wareCellers)
        data , description = extracData(text)
        ConverText.ConverDataXlsx(description, data, 'SabanaDeVentas.xlsx')


