import pandas as pd

def ExtractDescription(DataDescription: list) -> list:
    frameData = []
    for i in range(len(pd.array(DataDescription))):
        frameData.append(DataDescription[i][0])
    return frameData

def dataFusion(dataDescription, DataFrame):
    pass

def passArray(Data):
    DatosConvert = []
    for i in Data:
        for j in i:
            DatosConvert.append(str(j))
    return DatosConvert