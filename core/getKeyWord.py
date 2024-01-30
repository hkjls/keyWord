import re

class kw:
    def __init__(self):
        pass

    def getkw(self, txt, degre = 0):
        txtSplit = re.split(" ", txt)
        txtFilter = []
        txtDict = {}

        for t in txtSplit:
            if len(t) > degre and not any(chr.isdigit() for chr in t):
                txtFilter.append(t)
                txtDict[t] = len(t)
            
        dictfilter = sorted(txtDict,  key=lambda k: (txtDict[k], k), reverse=False)

        return dictfilter