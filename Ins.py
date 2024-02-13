import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import json



def getIns(url, InsDict,dollar):

    
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'
    }

    response = requests.get(url=url, headers=headers)
    data = response.json()
    response = data["results_html"]

    soup = BeautifulSoup(response, 'lxml')
    names = soup.find_all('div', class_='market_listing_item_name_block')
    prices = soup.find_all('div', class_='market_listing_right_cell market_listing_their_price')

    dollar = dollar

    schet = 0
    for i in names:
        name = i.text.replace("Dota 2", "").strip()
        i = prices[schet]
        i = i.find_next('span', class_='normal_price').find_next().find_next()
        i = i.text.replace("Starting at:","").strip().replace('\n', '').replace(".", ',').replace("$", '').replace("USD", '').strip()
        price = i.replace(',', '.')
        try:
            price = float(price)
        except:
            price = f"{price}0"
            rightNum = price[-4:-1]
            leftNum = price[-99:-4]
            leftNum = leftNum.replace('.', '')
            price = f"{leftNum+rightNum}"
            price = float(price)
        price = price*dollar
        price = round(price,2)
        tempDict = {name:price}
        InsDict.update(tempDict)
        schet += 1


    return(InsDict)
        




if __name__ == '__main__':
    start_from = 0
    batch = 100
    InsDict = {}
    for i in range(0, 4):
        urll = f"https://steamcommunity.com/market/search/render/?query=&start={start_from}&count={batch}&search_descriptions=0&sort_column=price&sort_dir=asc&appid=570&category_570_Hero%5B%5D=any&category_570_Slot%5B%5D=any&category_570_Type%5B%5D=tag_wearable&category_570_Quality%5B%5D=tag_strange&category_570_Rarity%5B%5D=tag_Rarity_Immortal"
        InsDict = getIns(url=urll, cookieF=cookieF, InsDict=InsDict)
        start_from += batch
        print(f"Complete! {i}")
    with open('dataIns.json', 'w') as file:
        data = InsDict
        json.dump(data, file, indent=4)

    