# 1) Создать переменную типа String строки
str_v = "anna"

# 2) Создать переменную типа Integer число
int_v = 34

# 3) Создать переменную типа Float дробные числа
float_v = 3.4

# 4) Создать переменную типа Bytes байты
bytes_v = b"Hello"
# 5) Создать переменную типа List список
list_v = [1, 2, 3];

# 6) Создать переменную типа Tuple кортеж
tuple_v = tuple( )

# 7) Создать переменную типа Set множество
set_v = {1,2,2}

# 8. Создать переменную типа Frozen set неизменяемое множство
frozenset_v = frozenset( )


# 9) Создать переменную типа Dict словарь
dict_v = {'1': 1,'5': 5}

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(str_v, type(str_v))
print(int_v, type(int_v))
print(float_v, type(float_v))
print(bytes_v, type(bytes_v))
print(list_v, type(list_v))
print(tuple_v, type(tuple_v))
print(set_v, type(set_v))
print(frozenset_v, type(frozenset_v))
print(dict_v, type(dict_v))

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
l = "cat"
c = "Tilda"
n = (l +' '+ c)
print(n)
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)

print(l, c)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(l + str (), str(c))