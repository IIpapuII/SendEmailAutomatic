from model.conectDB import conect
from components.converTextData import ConverText
from components.dataExtract import ejecuteQueryNotDate


coon = conect()
class ProjectAccountingEjecute():
    """
    Se encarga de realizar el repice de los asientos que se encuentran sin proyecto a nivel contable.
    """
    def __init__(self, schemeDB, initDate, endDate):
        self.schemeDB = schemeDB
        self.initDate = initDate,
        self.endDate = endDate
    
    
    def transformData(self):
        text = ConverText.converTextFormatSQL('projectAccounting.sql', self.schemeDB, self.initDate, self.endDate)
        ejecuteQueryNotDate(text)
        print("asientos correjidos.")