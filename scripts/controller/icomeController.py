from components.dataExtract import extracData
from components.converTextData import ConverText
from components.transformData import dataFusion, exportExcel
from model.modelSQL import Structure
import pandas as pd
import os


def controllerIcome():
    modelo = Structure('HBTGELVEZ_CUCUTA', '006','20230604', '20230609',)
    text = ConverText.converTextFormatSQL('income.sql',modelo.initDate, modelo.endDate,modelo.schemeDB,modelo.wareHouse)
    data, description  =extracData(text)
    if not data:
        return False
    else:
        dataFusion(data,description).to_excel(os.path.join(os.path.dirname(os.path.abspath('docs')),'scripts/docs/'+'DATA.xlsx'))
    
    print(ConverText.ConverMenssajeHTML("menssage.html"))
    
