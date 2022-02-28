import json # импорт библиотеки



#json_string = json.dumps(data) # созадаем строковую переменную содержащую текс в офрмате json из переменной data



    
file = "src/egor/Cities1.txt"
write_file = "src/egor/data_file.json"
file = "Cities1.txt"
write_file = "data_file.json"
def calc_params_city_from_file(file,write_file):
    with open(file, "r") as read_file:
    
    
    
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
    
        c = {"avg_area":avg,
             "max_area":max(d),
             "min_area":min(d)}
        print(c)
    
    with open(write_file, "w") as write_file: # открываем фаил на запись
        json.dump(c, write_file)
    
calc_params_city_from_file(file,"data_file.json")

       
# Искал бы где больше цифр в числе
# Разбил бы по группам в соответствии с количеством цифр
# Выбрал группу с числами, где больше всего цифр
# Искал бы числа с наибольшей первой цифрой
# Так же с последующими цифрами
def test_cities():
    file1 = "src/egor/cities3.json"
    write_file1 = "src/egor/cities3_result.json"
    file1 = "cities3.json"
    write_file1 = "cities3_result.json"
    calc_params_city_from_file(file1,write_file1)
    result = {"avg_area": 5314.666666666667, "max_area": 15000, "min_area": 105}
    with open(write_file1, "r") as read_file:
         data1 = json.load(read_file)
         if data1 == result:
            return True
         else:
            assert False
            
    

test_cities()

  
    
    
        
       
        
   
   
                
        
    
    

   

    
            



