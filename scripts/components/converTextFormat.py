import os
class converText:
    def converTextSQL(fileNameSQL):
        querySQL = open(os.path.join(os.path.dirname(os.path.abspath('script')),'scripts/query/'+ fileNameSQL))
        return querySQL.read()

    def converTextFormatSQL(fileNameSQL,*vars):
        querySQL = open(os.path.join(os.path.dirname(os.path.abspath('script')),'scripts/query/'+ fileNameSQL))
        querySQL = str(querySQL.read()).format(*vars)
        return querySQL
