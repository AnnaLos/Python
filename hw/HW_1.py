import math

# Создать переменную item_1 типа integer.
item_1 = 2
# Создать переменную item_2 типа integer.
item_2 = 3
#  Создать переменную result_sum в которой вы суммируете item_1 и item_2.
result_sum = item_1 + item_2
# Вывести result_sum в консоль.
print(result_sum)
# Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
result_subtr = item_2 - item_1
print(result_subtr)
#   Вывести result_multi в консоль.
result_multi = item_1 * item_2
print(result_multi)
# Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
result_exp = item_1 ** item_2
print(result_exp)
# Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
result_m_exp = math.pow(item_1, item_2)
print(result_m_exp)
# Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
result_s_root = item_2 ** 0.5
print(result_s_root)
# Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.
result_m_s_root = math.sqrt(item_2)
print(result_m_s_root)
# Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
result_mp_s_root = math.pow(item_2, 0.5)
print(result_mp_s_root)
# Создать переменную result_division в которой вы разделите item_1 на item_2.
result_division = item_1 / item_2
print(result_division)
# Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division..floor
result_m_floor = math.floor(result_division)
print(result_m_floor)
# Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division..ceil
result_m_ceil = math.ceil(result_division)
print(result_m_ceil)
# Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
result_int = int(result_division)
print(result_int)
# Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
result_no_division_loss = item_1 // item_2
print(result_no_division_loss)
# Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
result_division_loss = item_1 % item_2
print(result_division_loss)
# Создать переменную item_3 и присвоить ей целое число
item_3 = 8

# Прибавить 10 к item_3 с присвоением.
# Вывести item_3 в консоль.
# Отнять 5 от item_3 с присвоением.
# Вывести item_3 в консоль.
#  Умножить item_3 на 3 с присвоением.
# Вывести item_3 в консоль.
# Разделить item_3 на 2 с присвоением.
# Вывести item_3 в консоль.
# Возвести в степень 2 item_3 с присвоением.
# Вывести item_3 в консоль.
# Найти квадратный корень item_3 с присвоением.
# Вывести item_3 в консоль.
# Присвоить остаток от деления item_3
# Вывести item_3 в консоль.
item_3 += 10
print(item_3)
item_3 -= 5
print(item_3)
item_3 *= 3
print(item_3)
item_3 /= 2
print(item_3)
item_3 **= 2
print(item_3)
item_3 **= 0.5
print(item_3)
item_3 %= 19.5
print(item_3)
# Boolean operations
# Создать переменную b_item_t и присвоить True
b_item_t = True
b_item_f = False
# Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
b_item_result_sum = b_item_t + b_item_f
print(b_item_result_sum)
# Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
b_item_result_subtr = b_item_t - b_item_f
print(b_item_result_subtr)
# Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
b_item_result_multi = b_item_t * b_item_f
print(b_item_result_multi)
# Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f
b_item_result_division = b_item_t / b_item_f    # Error
print(b_item_result_division)
# Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int 
b_item_1_int = int(b_item_t)
print(b_item_1_int)
b_item_2_int = int(b_item_f)
print(b_item_2_int)