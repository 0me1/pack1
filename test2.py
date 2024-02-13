import json

with open('dataCash.json', 'r') as file:
    data = json.load(file)

for k,v in data.items():
    # link = k.replace(' ', '%20').replace("'", '%27')\
    link = k.replace(' ', '+')
    
    link = f"https://steamcommunity.com/market/search?q={link}&category_570_Hero%5B%5D=any&category_570_Slot%5B%5D=any&category_570_Type%5B%5D=any&category_570_Quality%5B%5D=tag_unique&category_570_Quality%5B%5D=tag_strange&appid=570"
    link = f"<a href='{link}'>Link</a>"
    v = v+'\n'+link
    print(v)

