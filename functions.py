from multiprocessing.sharedctypes import Value
import sqlite3

def insert(table, values):
    stringQuestions = '('
    stringValues = '(' + table + ', '

    for value in values:
        stringQuestions += '?, '
        stringValues += str(value) + ', '

    stringQuestions = stringQuestions[:-2]
    stringQuestions += ')'

    stringValues = stringValues[:-2]
    stringValues += ')'

    return "'''INSERT INTO ? VALUES " + stringQuestions + ", " + stringValues + "'''"

print()    

print()

def select(attributes, table, condition=None):
    if (attributes == '*'):
        return '"SELECT * FROM ' + table + ' WHERE ' + condition + '"'

    stringAttributes = ''

    for attribute in attributes:
        stringAttributes += str(attribute) + ', '
    
    stringAttributes = stringAttributes[:-2]

    if condition == None:
        return '"SELECT ' + stringAttributes + ' FROM ' + table + '"'

    return '"SELECT ' + stringAttributes + ' FROM ' + table + ' WHERE ' + condition + '"'

#print(select('*', 'Kaffesmaking', 'poeng = 10'))
#print(select(('Navn', 'Smaksnotat'), 'Kaffesmaking', 'poeng = 10'))
print()