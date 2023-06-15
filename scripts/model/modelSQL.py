
class Structure():
    def __init__(self, schemeDB, wareHouse, initDate= None, endDate= None ) -> None:
        self.schemeDB = schemeDB
        self.wareHouse = wareHouse
        self.initDate = initDate
        self.endDate = endDate

class Proveedor:
    def __init__(self,
            nameCellers = None,
            nameHouse = None,
            codeHouse = None
            
    ):
        self.nameCellers = nameCellers
        self.nameHouse = nameHouse
        self.codeHouse = codeHouse
        

