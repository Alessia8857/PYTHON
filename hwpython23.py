# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int
import random

my_list = []

for (i) in range (10):
     my_list.append(random.randint(0,10))
      
print(my_list)


for i in range(10):
  num = random.randint(0,10)
  temp = my_list[i]
  my_list[i]= my_list[num]
  my_list[num] = temp
print(my_list)
