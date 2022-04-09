from  bs4 import BeautifulSoup
import requests
import re
import json
links_2 = []
with open("ikea2.json", "r") as read_file: #Открываем файл с ссылками
        data = json.load(read_file) #  В переменную доббавляем все содержимое файла      
        for i in data: # Пробегаемя по файлу
            n = i["link"] # Достаем значение с ключом link            
            page = requests.get(n,timeout=5) # Отправляем запрос на  ссылку переменной j          
            soup=BeautifulSoup(page.text,"html.parser") # Создаем объект
            #allPrice=soup.findAll('a' )
            allPrice=soup.findAll('span', class_ = 'pip-price__integer'  )
            for one_price in allPrice:             
                links_2.append(one_price.text)
            print(links_2)

        new_list = []
        
        for k in links_2:
            new_list.append({'price':k})
        new_list_size_100 = new_list[0:100]

with open("ikea2.json", "w") as write_file: # открываем фаил на запись
    json.dump(new_list_size_100, write_file)

