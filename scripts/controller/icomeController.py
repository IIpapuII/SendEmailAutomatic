from generator.icomesGeneration import icomeSuper
import pandas as pd


def controllerIcome():
    data, description  =icomeSuper()
    print(pd.DataFrame(data))
    print(pd.array(description))

