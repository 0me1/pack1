InsDict = {'Abra': 124.4, 'Bimbo': 244.4}
ComDict = {'Abra': 166.0, 'Bimbo': 300.0}
CashDict = {}
MyDict = {}


for k,x in InsDict.items():
    k = k.replace("Inscribed", "").strip()
    try:
        y = ComDict[k]
        cash = y / 1.15
        cash = cash - x
        cash = round(cash, 2)
        if 2.0 < cash < 200.0:
            cashstr = f"\nЦена {x}руб\nПрибыль {cash}руб"
            tempDict = {k:cashstr}
            CashDict.update(tempDict)

        if 15.0 < cash < 200.0:
            cash = f"\nЦена {x}руб\nПрибыль {cash}руб"
            tempDict = {k:cash}
            MyDict.update(tempDict)
    except:
        pass
print(CashDict)
print(MyDict)