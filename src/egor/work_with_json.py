import json # импорт библиотеки

#with open("data_file.json", "w") as write_file: # открываем фаил на запись
   # json.dump(data, write_file) # записываем переменную data преобразованную в json в фаил write_file 

#json_string = json.dumps(data) # созадаем строковую переменную содержащую текс в офрмате json из переменной data
def calc_avg(counts):
    peoples = 0
    cities = 0
    for i in counts:
        peoples = peoples + i
        cities = cities + 1
    avg1 = int(peoples / cities)
    return avg1

    
    
with open("Cities1.txt", "r") as read_file:



    data = json.load(read_file)
    print(data)    
    avg = data["cities"].values()
    print(avg)
    
        
    avg1 = calc_avg(avg)
    avg2 = {
            "avg":avg1
            }


    
    print(int(avg1))
with open("data_file.json", "w") as write_file: # открываем фаил на запись
    json.dump(avg2, write_file)
    
            

def test_calc_avg():
    my_list = [2,4]
    desired_result = 3
    if desired_result == calc_avg(my_list):
        return True
    else:
        assert False
test_calc_avg()
    
    
    
    

#data = json.loads(json_string)

