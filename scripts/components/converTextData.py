import os


class ConverText:
    """Class element utils
    
    Keyword arguments:
    argument -- Se ecnarga de generar la transformacion de consultas
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
    
    def ConverMenssajeHTML(fileNameHTML):
        text = open (os.path.join(os.path.dirname(os.path.abspath('templates')), 'Scripts/templates/'+ fileNameHTML),'r')
        return text.read()


