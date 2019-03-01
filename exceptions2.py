#Напишите функцию get_summ(num_one, num_two), которая принимает на вход два целых числа (int) и складывает их
#Оба аргумента нужно приводить к целому числу при помощи int() и перехватывать исключение ValueError если приведение типов не сработало

def get_summ(num_one, num_two):
	try:
		a = int(num_one)
		b = int(num_two)
		return a+b
	except ValueError:
		return 'Что-то пошло не так'

print(get_summ(1, 2))
print(get_summ('1','2'))
print(get_summ('1','jka@'))
