import csv
import random

cinephiles_today = ['Кирилл', 'Эд', "Рита", "Настя С"]
all_films_for_watching = []
N = 5 # number of random films

class Film:
    def __init__(self, name, year, viewed=None):
        self.name = name
        self.year = year
        self.viewed = viewed

with open('filmclub.csv') as table:
    reader = csv.DictReader(table)
    
    for row in reader:
        
        title = row['Название'].rstrip('\n')
        # exit if there is end of film list
        if title == '': 
            break
        year = row['Год'].rstrip('\n')
        if year == '':
            year = '[год пропущен]'
        wathed = row['Смотрели'].rstrip('\n')
        
        person_wathed = [] # if someone wathed film
        for person in cinephiles_today:
            if wathed.find(person) != -1:
                person_wathed.append(person)

        if len(person_wathed) == 0: # no one from cinephiles_today wathed film  
            # print('-------------------------------------------')
            # print('|', title, '-', year)
            all_films_for_watching.append(Film(title, year, wathed))
        else:
            pass
            # print('-------------------------------------------')
            # print('|', title, '-', year, '- ПРОПУСК.')
            for person in person_wathed:
               pass
               # print('|', person, 'уже смотрел(а) этот фильм.')

# print('-------------------------------------------')

random_films_for_watching = []

while len(random_films_for_watching) < N:
    r = random.randint(0, len(all_films_for_watching)-1)
    brk = False
    for film in random_films_for_watching:
        if (film.name == all_films_for_watching[r].name) and \
            (film.year == all_films_for_watching[r].year):
            brk = True
            break
        
    if brk == False:
        random_films_for_watching.append(all_films_for_watching[r])

# printing result
print('\n-------------------------------------------')
print("       Список фильмов для просмотра       ")
print('-------------------------------------------')
i = 1
for line in random_films_for_watching:
    if line.viewed != "":
        print(f"{i}:", line.name, "-", line.year, f'(Для справки, этот фильм видели: {line.viewed})')
    else:
        print(f"{i}:", line.name, "-", line.year)
    i += 1

print('\n-------------------------------------------')
print("  Исходя из таблицы, их точно не смотрели")
print('-------------------------------------------')

for line in cinephiles_today:
    print('-', line)
print()
