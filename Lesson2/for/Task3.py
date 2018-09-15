#Оценки
class_list = [
    {"class": "1A", "scores": [2.1, 5, 3, 2, 4, 5, 5, 3]}
    , {"class": "1B", "scores": [3, 5, 3, 2, 4, 5, 5, 3]}
    , {"class": "1C", "scores": [3, 3, 3, 3, 4, 5, 4, 3]}
    , {"class": "2A", "scores": [2, 5, 4, 5, 5, 5, 3]}
    , {"class": "2B", "scores": [3.3, 2.9, 4.5, 5.6, 5.7, 3]}
    , {"class": "3A", "scores": [2, 5, 3]}
    , {"class": "3B", "scores": [4]}
]

school_avg = 0

# Средняя оценка по классу
for i in class_list:
    avg = 0
    for x in i.get("scores"):
        avg += x
    final_avg = round(float(avg/len(i.get("scores"))), 2)
    print("Класс: " + i.get("class") + ", средняя оценка: " + str(final_avg))
    school_avg += round(float(avg/len(i.get("scores"))), 2)

# Средняя оценка по школе
print("\nСредняя оценка по школе: " + str(round(float(school_avg/len(class_list)), 2)))
