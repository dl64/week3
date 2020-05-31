import csv

list_of_dictionaries = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

with open('output_file.txt', 'w', encoding='utf-8') as f:
    fields = ['name','age','job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for items in list_of_dictionaries:
        writer.writerow(items)
