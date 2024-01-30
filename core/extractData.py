import pandas as pd
from .getKeyWord import kw

class extractData:
    def __init__(self, pathFile, sheetName, columnName, degre = 0):
        self.sN = sheetName
        self.cN = columnName
        self.dg = degre

        try:
            extractData = pd.ExcelFile(pathFile)
        except Exception as e:
            print("something wrong")
            print(e)
            exit()
        
        self.dt = extractData.parse(sheetName)

    def getData(self):
        keydict = {}

        for i in range(self.maxKeyArray()):
            keydict[f'key{i+1}'] = []

        for desc in self.dt[self.cN]:
            spliter = kw()
            strSplit = spliter.getkw(desc, self.dg)
            
            # if len(strSplit) > 0:
            for j in range(self.maxKeyArray()):
                try:
                    keydict[f'key{j+1}'].append(strSplit[j])
                except Exception as e:
                    keydict[f'key{j+1}'].append("")

        return keydict
    
    def maxKeyArray(self):
        
        lenSS = 0
        for desc in self.dt[self.cN]:
            spliter = kw()
            strSplit = spliter.getkw(desc, self.dg)

            if len(strSplit) > lenSS:
                lenSS = len(strSplit)
            else:
                lenSS = lenSS

        return lenSS