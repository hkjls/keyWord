from core.getKeyWord import kw
from core.extractData import extractData
from tkinter import filedialog
import shutil
from pathlib import Path
import pandas as pd

def main():
    try:
        srcFile = filedialog.askopenfilename(title = "Choose right file", filetypes=([("excel files", "*.xlsx")]))
    except Exception as e:
        print( "Warning: " + str(e))
        exit()

    importPath = f'{Path(__file__).resolve().parent}/Import/'
    filename = srcFile.split('/')[-1]
    copyTo = f"{importPath}{filename}"
    shutil.copy(srcFile, copyTo)

    dataObject = extractData(copyTo, 'Feuil1', 'DESCRIPTION', 4)
    keyDict = dataObject.getData()

    dt = pd.DataFrame(keyDict)

    dtConcated = pd.concat([dataObject.dt, dt], axis=1)

    dtConcated.to_excel("test.xlsx", index=False)



    return 

if  __name__ == "__main__":
    main()