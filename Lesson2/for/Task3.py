#Оценки
class_list = [
    {"class": "1A", "scores": [2, 5, 3, 2, 4, 5, 5, 3]}
    , {"class": "1B", "scores": [3, 5, 3, 2, 4, 5, 5, 3]}
    , {"class": "1C", "scores": [3, 3, 3, 3, 4, 5, 4, 3]}
    , {"class": "2A", "scores": [2, 5, 4, 5, 5, 5, 3]}
    , {"class": "2B", "scores": [3, 2, 4, 5, 5, 3]}
    , {"class": "3A", "scores": [2, 5, 3]}
    , {"class": "3B", "scores": [4]}
]

school_avg = 0
school_counter = 0

# Средняя оценка по классу
for i in class_list:
    avg = 0
    counter = 0

    for x in i.get("scores"):
        avg += x
        counter += 1
    print("Класс: " + i.get("class") + ", средняя оценка: " + str(int(avg/counter)))

    school_avg += avg
    school_counter += counter

# Средняя оценка по школе
print("\nСредняя оценка по школе: " + str(int(school_avg/school_counter)))