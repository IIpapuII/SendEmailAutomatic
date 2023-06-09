from generator.icomesGeneration import icomeSuper
from components.converTextData import ConverText
from generator.transformData import ExtractDescription
from model.modelSQL import Structure
import pandas as pd


def controllerIcome():
    modelo = Structure('HBTGELVEZ_CUCUTA', '006','20230601', '20230609',)
    text = ConverText.converTextFormatSQL('income.sql',modelo.initDate, modelo.endDate,modelo.schemeDB)
    data, description  =icomeSuper(text)
    #print(pd.DataFrame(data))
    #print(pd.array(description))
    frame = ExtractDescription(description)
    print(frame)
