from model.modelSQL import Structure
from components.converTextData import ConverText
from components.dataExtract import extracData





class ParettoSales(Structure):
    def __init__(self, schemeDB, 
                 wareHouse, 
                 initDate=None, 
                 endDate=None, ) -> None:
        super().__init__(schemeDB, wareHouse, initDate, endDate)
    
    def Controlle(self):
        text = ConverText.converTextFormatSQL('ParretoSales.sql',
                                              self.schemeDB, self.wareHouse, self.initDate, self.endDate)
        data , description = extracData(text)
        print(data[0])
        ConverText.ConverDataXlsx(description, data, 'ArchiveVentas.xlsx')


