# Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
age = 23
n = int(age)
print(n)
print(type(n))

foo = "23abc"
n = str(foo)
print(n)
print(type(n))

# Преобразуйте переменную age в Boolean
# age = 123abc
age = "123abc"
n = str(age)
print(bool("n"))

# Преобразуйте переменную flag в Boolean
# flag = 1
flag = 1
n = int(flag)
print(bool("n"))

# Преобразуйте значение  в Boolean
#str_one = "Privet"
#str_two = ""
str_one = "Privet"
str_two = ""
print(bool(str_one))
print(bool(str_two))

# Преобразуйте значение 0 и 1  в Boolean
bool(1)
bool(0)