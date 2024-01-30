# Основні оператори
# Оператор ‒ це символ мови програмування, який здатний оперувати значеннями.
# +
# -
# *
# /
# //
# %
# **

# print(2 ** 3)
# print(2 ** 3.)
# print(2. ** 3)
# print(2. ** 3.)

# print(2 * 3)
# print(2 * 3.)
# print(2. * 3)
# print(2. * 3.)

# print(6 / 3)    2.0
# print(6 / 3.)   2.0
# print(6. / 3)   2.0
# print(6. / 3.)  2.0
#Результат, отриманий в результаті виконання оператора ділення, завжди є числом з рухомою крапкою, незалежно від того, чи результат на перший погляд здається числом з рухомою крапкою: 1 / 2, чи він виглядає як чисте ціле число: 2 / 1.

# Цілочисельне ділення (частка від ділення)
# Знак // (подвійна коса риска) є оператором цілочисельного ділення. Він відрізняється від стандартного / оператора двома деталями:

# в його результаті відсутня дробова частина – вона відсутня (для цілих чисел) або завжди дорівнює нулю (для чисел з рухомою крапкою); це означає, що результати завжди округляються;
# дотримується правил цілих та чисел з рухомою крапкою.
# print(6 // 3)    2
# print(6 // 3.)   2.0
# print(6. // 3)   2.0
# print(6. // 3.)  2.0


# print(-6 // 4)   -2
# print(6. // -4)  -2.0
#Результат ‒ дві від'ємні двійки. Реальний (не округлений) результат дорівнює -1.5 в обох випадках. Однак результати підлягають округленню. Округлення відбувається в бік меншого цілого значення, а меншим цілим значенням є -2, отже: -2 і -2.0.

#print(12 % 4.5)  3.0

# Оператор віднімання - це, очевидно, знак - (мінус), хоча слід зазначити, що цей оператор має й інше значення - він може змінювати знак числа.
# Це прекрасна можливість показати важливу відмінність між унарними та бінарними операторами.

#print(9 % 6 % 2)  1 ліва асоціативність

#print(2 ** 2 ** 3) 256 піднесення до степеня використовується правостороння асоціативність

# print(-3 ** 2)
# print(-2 ** 3)
# print(-(3 ** 2))

# print(2 * 3 % 5)
# print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)    10.0

# print((2 ** 4), (2 * 4.), (2 * 4))
# print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))