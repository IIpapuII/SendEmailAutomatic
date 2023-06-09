from model.conectDB import conect

def icomeSuper(text):
    coon = conect()
    coon.execute(text)
    return coon.fetchall() , coon.description