import os


class ConverText:
    """Class element utils
    
    Keyword arguments:
    argument -- Se encarga de generar la transformacion de consultas
    y elementos de marcado como HTML
    Return: strings
    """
    
    def converTextSQL(fileNameSQL):
        querySQL = open(os.path.join(os.path.dirname(os.path.abspath('script')),'scripts/query/'+ fileNameSQL))
        return querySQL.read()

    def converTextFormatSQL(fileNameSQL,*vars):
        querySQL = open(os.path.join(os.path.dirname(os.path.abspath('script')),'scripts/query/'+ fileNameSQL))
        querySQL = str(querySQL.read()).format(*vars)
        return querySQL
    
    def ConverMenssajeHTML(fileNameHTML, *vars):
        menssage = ''
        text = open (os.path.join(os.path.dirname(os.path.abspath('templates')), 'scripts/templates/'+ fileNameHTML),'r')
        menssage = str(text.read())
        menssage = menssage.format(*vars)
        menssage = menssage.replace('#','{')
        menssage = menssage.replace('+', '}')
        return menssage

    def ConverAffairText(menssage, *vars):
        text = menssage.format(*vars)
        return menssage
    
    

