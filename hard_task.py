# пример №1

fl = open('24.txt') # открываем файл

# with open(’24.txt’) as fl: - другой вариант открытия файла

# инициализируем словарь для хранения 
# минимального количества символов в строке
mn_cnt = {'S':10**8} 

# запускаем цикл для каждой строки файла
for ln in fl:
    # инициализируем словарь для подсчета 
    # количества каждого символа в строке
    cnt = {}
    for ch in ln: # проходим по всем символам строки
         # увеличиваем счётчик для каждой буквы
        cnt[ch] = cnt.get(ch, 0) + 1
    # проверяем, реже ли встречается символ 'S' в текущей строке
    if cnt['S'] < mn_cnt['S']:
        # обновляем словарь значений
        mn_cnt = cnt 
        
# находим символ c максимальным количеством вхождений
mx_ch = max(mn_cnt, key=mn_cnt.get) 
print(mx_ch) # выводим найденный символ


# пример №2

# импортируем необходимую коллекцию из модуля
from collections import Counter

fl = open('24.txt') # открываем файл

# with open(’24.txt’) as fl: - другой вариант открытия файла

# инициализируем словарь для хранения 
# минимального количества символов в строке
mn_cnt = {'S':10**8}

# запускаем цикл для каждой строки файла
for ln in fl:
    # используем коллекцию Counter из модуля collections для 
    # подсчета количества каждого символа в строке
    cnt = Counter(ln) 
    # проверяем, реже ли встречается символ 'S' в текущей строке
    if cnt['S'] < mn_cnt['S']:
            # обновляем словарь значений
            mn_cnt = cnt 
    
# находим символ c максимальным количеством вхождений
mx_ch = max(mn_cnt, key=mn_cnt.get) 
print(mx_ch) # выводим найденный символ
