from  bs4 import BeautifulSoup
import requests
import re
import json




url = 'https://www.dns-shop.ru/'
final_links_list = []
page = requests.get(url) # Отправляем запрос на  ссылку переменной j
#print(page.status_code) # Ввыодим статус ответа при запросе этих ссылок
#print(page.text) # Выводим текст всех ссылок
soup=BeautifulSoup(page.text,"html.parser") # Создаем объект
allPrice=soup.findAll('a') # Ищем все html элементы с тэгом а
for one_price in allPrice:
    #print(one_price.get('href',None))
    final_links_list.append(one_price.get('href',None))

mnozhestva = set(final_links_list)
new_list = []
for k in mnozhestva:
    new_list.append({'link':k})

with open("dns.json", "w") as write_file: # открываем фаил на запись
    json.dump(new_list, write_file)

