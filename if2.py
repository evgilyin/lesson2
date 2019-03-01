def strings_comparison(string1, string2):
#Если они не строки, то вернуть 0
	if type(string1) and type(string2) != str:
		string_check = 0
#Если они строки и одинаковые, то вернуть 1
	elif type(string1) == type(string2) and string1 == string2:
		string_check = 1
#Если эти строки разные и первая длиннее, то вернуть 2
	elif string1 != string2 and len(string1) > len(string2):
		string_check = 2
#Если эти строки разные и вторая строка 'Learn', то вернуть 3
	elif string1 != string2 and string2 == 'learn':
		string_check = 3
	
	return string_check

a = strings_comparison('Hello', 1)
b = strings_comparison('Hello', '2')
c = strings_comparison('Hello', 'meow')
d = strings_comparison('Hello', 'learn')

print(a,b,c,d)
