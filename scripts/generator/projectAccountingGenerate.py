from components.converTextData import ConverText
from components.dataExtract import ejecuteQueryNotDate, extracData



class ProjectAccountingEjecute():
    """
    Se encarga de realizar el repice de los asientos que se encuentran sin proyecto a nivel contable.
    """
    def __init__(self, schemeDB, initDate, endDate):
        self.schemeDB = schemeDB
        self.initDate = initDate,
        self.endDate = endDate
    
    
    def transformData(self):
        TransId = ConverText.converTextFormatSQL('EmptyProjectSeat.sql', self.schemeDB)
        data, descripcion  = extracData(TransId)
        for i in data:
            text = ConverText.converTextFormatSQL('projectAccounting.sql', self.schemeDB, i[1])
            ejecuteQueryNotDate(text)
            print("Asiento correjido: ", i[1])