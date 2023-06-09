from model.conectDB import conect
from components.converTextFormat import converText

def icomeSuper(text):
    coon = conect()
    coon.execute(converText.converTextFormatSQL('income.sql','20230601', '20230609','HBTGELVEZ_CUCUTA'))
    return coon.fetchall() , coon.description