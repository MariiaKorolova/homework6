#3. Даны списки my_list_1 и my_list_2. Создать список my_result в который вначале поместить элементы на четных местах из
my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = [10, 20, 30, 40, 50]
my_list_2 = [15, 30, 45, 60]
my_result = [x for x in my_list_1 if not x % 2] + [x for x in my_list_2 if x % 2]
print(my_result)


#*5. Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.[1,2,3,4] -> [2,3,4,1].
Пересоздавать список нельзя! (используйте метод pop)

my_list = [1, 2, 3, 4]
list_value = my_list.pop(0)
my_list.append(list_value)
print(my_list)


#11. Дана строка my_str. Создать список в который поместить те символы из my_str, которые встречаются
в строке ТОЛЬКО ОДИН раз.

my_str = 'stroka'
my_set = set(my_str)
my_list = []
for i in my_set:
     my_list.append(i)
print(my_list)


