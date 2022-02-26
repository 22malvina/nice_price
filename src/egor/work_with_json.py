import json # импорт библиотеки



#json_string = json.dumps(data) # созадаем строковую переменную содержащую текс в офрмате json из переменной data



    
    
with open("Cities1.txt", "r") as read_file:
    data = json.load(read_file)
 
    a = 0
    b = 0
    for i in data:
        a = a + 1
        b = b + i["area"]
    avg = b/a
    print(avg)
        
# Выписал бы все найденные числа
    d = []
    for i in data:
        z = i["area"]
        print(z)
        d.append(z)
    print(max(d))
    c = {"avg_area":avg,
         "max_area":max(d),
         "min_area":min(d)}
    print(c)
    
with open("data_file.json", "w") as write_file: # открываем фаил на запись
    json.dump(c, write_file)
    
    
    
       
# Искал бы где больше цифр в числе
# Разбил бы по группам в соответствии с количеством цифр
# Выбрал группу с числами, где больше всего цифр
# Искал бы числа с наибольшей первой цифрой
# Так же с последующими цифрами

        

  
    
    
        
       
        
   
   
                
        
    
    

   

    
            



