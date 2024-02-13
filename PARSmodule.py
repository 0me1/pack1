import json
import pandas as pd

def module():

    CashDict = {}
    MyDict = {}

    with open('dataIns.json', 'r') as file:
        InsDict = json.load(file)
    with open('dataCom.json', 'r') as file:
        ComDict = json.load(file)
    
    # for i in InsDict.keys():
    #     i = i.replace("Inscribed", "").strip()
    #     try:
    #         if i not in ComDict:
    #             khal = 1
    #     except:
    #         print(f"{i} not in ComDict")
        

    for k,x in InsDict.items():
        k = k.replace("Inscribed", "").strip()
        try:
            y = ComDict[k]
            cash = y / 1.15
            cash = cash - x
            cash = round(cash, 2)
            if 2.0 < cash < 200.0:
                cash_str = f"\nЦена {x}руб\nПрибыль {cash}руб"
                tempDict = {k:cash_str}
                CashDict.update(tempDict)
            if 15.0 < cash < 200.0:
                cash = f"\nЦена {x}руб\nПрибыль {cash}руб"
                tempDict = {k:cash}
                MyDict.update(tempDict)

            
        except:
            tempDict = {k:0}


    with open('dataCash.json', 'w') as file:
        json.dump(CashDict, file, indent=4)

    with open('dataMy.json', 'w') as file:
        json.dump(MyDict, file, indent=4)




if __name__ == '__main__':
    module()