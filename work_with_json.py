import json # импорт библиотеки

#with open("data_file.json", "w") as write_file: # открываем фаил на запись
    #json.dump(data, write_file) # записываем переменную data преобразованную в json в фаил write_file 

#json_string = json.dumps(data) # созадаем строковую переменную содержащую текс в офрмате json из переменной data

with open("test_json.txt", "r") as read_file: 
    data = json.load(read_file)
    print(data)
    data['president']['year'] = data['president']['year'] + 10
    print(data)
    

#data = json.loads(json_string)

with open("data_file.json", "w") as write_file: # открываем фаил на запись
    json.dump(data, write_file)
