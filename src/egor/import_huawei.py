from  bs4 import BeautifulSoup
import requests
import re
import json
links_1 = []
def get_url (url):
    links_2 = []
    try:
        
        page = requests.get(url,timeout=5) # Отправляем запрос на  ссылку переменной j
        print(page.status_code) # Ввыодим статус ответа при запросе этих ссылок
        print(page.text) # Выводим текст всех ссылок
        soup=BeautifulSoup(page.text,"html.parser") # Создаем объект
        allPrice=soup.findAll('a') # Ищем все html элементы с тэгом а
        for one_price in allPrice:
            print(one_price.get('href',None))
            links_2.append(one_price.get('href',None))
    except:
        print("Bad url")
    return links_2
 
with open("data_file_3.json", "r") as read_file: #Открываем файл с ссылками
    data = json.load(read_file) #  В переменную доббавляем все содержимое файла
    for i in data: # Пробегаемя по файлу
        n = i["link"] # Достаем значение с ключом link
        print(n)
        links_1.append(n) # Добавляем эти значения в список
final_links_list = []
for j in links_1: # Пробегаемя по созданному списку
    if j: # Если в переменной j есть какое-либо значение
        pass # Оператор-заглушка, равноценный отсутствию операции.
    else: # В остальных случаях 
        continue # Перейти к следующей итерации
    if j in ('https://', 'http://'):
        continue
    print(j)
    print('---------')
    if len(j) < 8: # Если длина j меньше 8
        continue # Перейти к следующей итерации
    o = j[:7] # Переменная о, выделение первых 7 символов j
    if o == "http://": # Если о  равна  "http://"
        w  = get_url(j)
        for p in w:
            final_links_list.append(p)
        
        
    l = j[:8] # В переменную l добавлем выделение первых 8 символов j
    #print(l)
    if j == "javascript:;": # Если j  равна  "javascript:;"
        pass # Оператор-заглушка, равноценный отсутствию операции.
    elif l == "https://" : # или если l  равна  "https://"
        
        
        v  = get_url(j)
        for p1 in v:
            final_links_list.append(p1)
        

        #break
    elif j[:2] == "//":
        url = "https:" + j
        
        i  = get_url(url)
        for p2 in i:
            final_links_list.append(p2)
        
        
        
       # page = requests.get(url) # Отправляем запрос на  ссылку переменной j
        #print(page.status_code) # Ввыодим статус ответа при запросе этих ссылок
        #print(page.text) # Выводим текст всех ссылок
        #soup=BeautifulSoup(page.text,"html.parser") # Создаем объект
        #allPrice=soup.findAll('a') # Ищем все html элементы с тэгом а
        #for one_price in allPrice:
           # print(one_price.get('href',None))
           # final_links_list.append(one_price.get('href',None))
print("-----")
print(final_links_list)
mnozhestva = set(final_links_list)
new_list = []
for k in mnozhestva:
    new_list.append({'link':k})
with open("data_file_4.json", "w") as write_file: # открываем фаил на запись
    json.dump(new_list, write_file)
        
    
    
   
    
    
#write_file = "data_file_1.json"
#url = "https://shop.huawei.ru/"
#page = requests.get(url)
#print(page.status_code)
#soup=BeautifulSoup(page.text,"html.parser")
#allPrice=soup.findAll('a')
#print(allPrice)
#links=[]
#for one_price in allPrice:
    #print(one_price.get('href',None))
   # links.append({'link':one_price.get('href',None)})
#with open(write_file, "w") as write_file: # открываем фаил на запись
    #json.dump(links, write_file)
