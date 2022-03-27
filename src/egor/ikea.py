from  bs4 import BeautifulSoup
import requests
import re
import json
links_1 = []
def get_url (url):
    links_2 = []
    try:
        print('.',)
        page = requests.get(url,timeout=5) # Отправляем запрос на  ссылку переменной j
        #print(page.status_code) # Ввыодим статус ответа при запросе этих ссылок
        #print(page.text) # Выводим текст всех ссылок
        soup=BeautifulSoup(page.text,"html.parser") # Создаем объект
        allPrice=soup.findAll('a' ) # Ищем все html элементы с тэгом а
      
        for one_price in allPrice:
            #print(one_price.get('href',None))
            links_2.append(one_price.get('href',None))
           # print(one_price.text)
            #print(links_2)
       
        
        
    except:
        print("Bad url")
    return links_2
 
with open("ikea.json", "r") as read_file: #Открываем файл с ссылками
    data = json.load(read_file) #  В переменную доббавляем все содержимое файла
    for i in data: # Пробегаемя по файлу
        n = i["link"] # Достаем значение с ключом link
       
       # print(n)
        links_1.append(n) # Добавляем эти значения в список
#Обрезаем количество ссылок до ста
links_1 = links_1[0:100]
print(links_1)

final_links_list = []
for j in links_1: # Пробегаемя по созданному списку
    if j: # Если в переменной j есть какое-либо значение
        pass # Оператор-заглушка, равноценный отсутствию операции.
    else: # В остальных случаях 
        continue # Перейти к следующей итерации
    if j in ('https://', 'http://'):
        continue
    #print(j)
   # print('---------')
    if len(j) < 8: # Если длина j меньше 8
        continue # Перейти к следующей итерации
    o = j[:7] # Переменная о, выделение первых 7 символов j
    if o == "http://": # Если о  равна  "http://"
        w  = get_url(j)
        for p in w:
            final_links_list.append(p)
        
        
    l = j[:8] # В переменную l добавлем выделение первых 8 символов j
    #print(l)
    if j == "hnf": # Если j  равна  "javascript:;"
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


#На входе передаем: Из большого списка ссылок
#На выходе получаем: Список из ста ссылок
def sto_url(spisok_url):
    #Мы хотим обрезать большой список до списка со ста элементов
    x = spisok_url[100]
    final_list_url = []
    for i in spisok_url:
        final_list_url.append(i)
        if i == x:
            break
   
    #Из основного списка ссылок мы дсстаем ссылки и добавляем их в новый список
    
    
    #До тех пор функция не выполниться сто раз мы
    return final_list_url
urls = sto_url(final_links_list)

def sto_url_v2(spisok_url_v2):

    final_list_url_v2 = []
    #Пустой список

    x = 0
    #Номер элемента списка

    while x < 100:
        # Пока номер элемента списка меньше ста
        final_list_url_v2.append(spisok_url_v2[x])
        #spisok_url_v2[x] - Элемент в списке под номером x
        #В список final_list_url_v2 добавляем элемент в списке под номером x
        x = x + 1
        #Переходим к следующему элементу списка
        
    


    return  final_list_url_v2



#Вызываем функции sto_url с параметром на входе final_links_list и на выходе получаем значение , которое присваиваем в переменную urls
    



#print("-----")
           
#print(final_links_list)
mnozhestva = set(final_links_list)
new_list = []
for k in mnozhestva:
    new_list.append({'link':k})
new_list_size_100 = new_list[0:100]
with open("ikea2.json", "w") as write_file: # открываем фаил на запись
    json.dump(new_list_size_100, write_file)
        
#ikea.com    
#https://www.ikea.com/ru/ru/p/   
#https://www.ikea.com/ru/ru/p/bagis-bagis-plechiki-d-doma-ulicy-belyy-10415971/
#https://www.ikea.com/ru/ru/p/thorgun-thorgun-pled-belyy-s-ottenkom-60513460/ 
#https://www.ikea.com/ru/ru/p/tvaellen-tvellen-odinarnaya-rakovina-90493837/   
#https://www.ikea.com/ru/ru/cat/hranenie-i-poryadok-st001/
#https://www.ikea.com/ru/ru/cat/nastennye-polki-10398/

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

