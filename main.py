import requests
from bs4 import BeautifulSoup

response = requests.get("https://yandex.ru/pogoda/moscow")
soup = BeautifulSoup(response.text, features="lxml")
cur_weather = soup.find("time").findNext("span").text
precipitation = soup.find('div', class_='link__condition')
weather = {"Ясно": "",
           "Облачно с прояснениями": "",
           "Пасмурно": "",
           "Небольшой дождь": "",
           "Малооблачно": "",
           "Небольшой снег": "",
           "Снег": "",
           "Дождь": ""
           }
print(f"{weather.get(precipitation.text)}  {cur_weather}°")

