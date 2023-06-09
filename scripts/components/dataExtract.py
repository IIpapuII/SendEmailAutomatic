from model.conectDB import conect
from .transformData import ExtractDescription

#SQL data extraction component using string query
def extracData(text):
    coon = conect()
    coon.execute(text)
    return coon.fetchall() , ExtractDescription(coon.description) 