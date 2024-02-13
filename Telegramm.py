import time
import json
import requests
import logging

logging.basicConfig(level=logging.INFO)

def load():
  with open('dataCash.json', 'r') as file:
    data = json.load(file)
  return (data)

def loadmy():
  with open('dataMy.json', 'r') as file:
    data = json.load(file)
  return (data)


def Bot(name):
  BOT_TOKEN = "6336774602:AAHMZ3bB3YE4Ad88pIQMcN4rRa-p4hDzUbk"
  count = 0
  redline = 18
  chat_id = "-915691294"
  data = load()

  for k, v in data.items():
    if count > redline:   #Телега имеет кд после ~20 запросов и дальше данные теряются 
      time.sleep(35)
      redline += 18
    elif count < redline:
      count += 1

    temp = k.replace(' ', '%2B')
    link = f"steamcommunity.com/market/search?q={temp}".replace('&', '%26')
    link = f'<a href="{link}">LINK</a>'
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text=<b>{k}</b> {v}\n {link}"
    response = requests.post(url).json()
    time.sleep(1.5)

  requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ").json()
  data.clear()

  print("All Message SEND")

  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=1844292880&parse_mode=HTML&text=<b>{name} run bot</b>"
  requests.get(url).json()
  # mydata = loadmy()
  # for k,v in mydata.items():
  #   url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=1844292880&parse_mode=HTML&text=<b>{k} </b> {v}"
  #   requests.get(url).json()
  #   time.sleep(1.5)
  # requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=1844292880&text=▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ").json()
  # mydata.clear()

if __name__ == "__main__":
  Bot("name")