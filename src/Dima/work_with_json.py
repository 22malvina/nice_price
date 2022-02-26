import json # импорт библиотеки

#with open("data_file.json", "w") as write_file: # открываем фаил на запись
    #json.dump(data, write_file) # записываем переменную data преобразованную в json в фаил write_file 

#json_string = json.dumps(data) # созадаем строковую переменную содержащую текс в офрмате json из переменной data

with open("Homework.txt", "r") as read_file: 
    data = json.load(read_file)
    print(data)
    x = 0
    y = 0
    for i in data:
        x += 1
        y += i["Budget"]
    avg = y / x

        

    max_budget = 0
    for i in data:
        if i["Budget"] > max_budget:
           max_budget = i["Budget"]



    min_budget = data[0]["Budget"]
    for i in data:
        if i["Budget"] < min_budget:
            min_budget = i["Budget"]

statistics = {
       "Avg_budget" : avg,
       "Max_budget" : max_budget,
       "Min_budget" : min_budget
       }
print(statistics)
with open("data_file.json", "w") as write_file: 
    json.dump(statistics, write_file)
