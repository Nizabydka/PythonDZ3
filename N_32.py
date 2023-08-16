#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#(т.е. не меньше заданного минимума и не больше заданного максимума)

import random
myList = [random.randint(0, 100) for _ in range(10)]
min = 20
max = 80
filtred_indices = [index for index, value in enumerate(myList) if min <= value <= max]
print(filtred_indices)