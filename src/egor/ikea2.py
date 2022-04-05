from  bs4 import BeautifulSoup
import requests
import re
import json




 #  В переменную доббавляем все содержимое файла
   

        


write_file = "ikea.json"
url = "https://www.ikea.com/ru/ru/"
page = requests.get(url,timeout=5)
print(page.status_code)
soup=BeautifulSoup(page.text,"html.parser")
allPrice=soup.findAll('a')
print(allPrice)
links=[]
for one_price in allPrice:
    print(one_price.get('href',None))    
    links.append({'link':one_price.get('href',None)})
with open(write_file, "w") as write_file: # открываем фаил на запись
    json.dump(links, write_file)
