import random 
#from base import Database, InputBase
import sqlite3

LowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
CapitalLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '_', '=', '?', '&', '$', '%', '#', '\\', '|', '/']

#
print('Для чего пароль?')
ForNet = input()

print('Вы можете указать логин')
Login = input()

print('Если вы хотите добавить существующий аккаунт, то введите пароль. Если создать новый, то намите Enter')
Password = input()

# Создаю функцию генератора 
def generated():
	print('Какой длины пароль?')
	Len = input() # Ввожу длину пароля
	LenInt = int(Len) # Перевожу в целочисленный тип

	print('Хотите использовать символы?\n введите \"y\", если да и \"n\", если нет.')
	SymInp = input()

	global Password

	# Условие 
	if SymInp == 'y' or SymInp == 'Y' or SymInp == 'yes' or SymInp == 'Yes' or SymInp == 'YES' or SymInp == 'д' or SymInp == 'да' or SymInp == 'Д' or SymInp == 'Да' or SymInp == 'ДА': 
		ListFinal = LowerLetters + CapitalLetters + numbers + symbols # Объединяем списки в один список с учетом списка символов
		Password = ''.join(random.sample(ListFinal, LenInt)) # Создаем рандомный пароль из общего списка с указанной длиной (преобразуем спсок в строку)
		print('\n')
		print(Password) # Выводим полученный пароль (преобразуем спсок в строку)

	#	
	elif SymInp == 'n' or SymInp == 'N' or SymInp == 'no' or SymInp == 'No' or SymInp == 'NO' or SymInp == 'н' or SymInp == 'нет' or SymInp == 'Н' or SymInp == 'Нет' or SymInp == 'НЕТ':
		ListFinal = LowerLetters + CapitalLetters + numbers # Объединяем списки в один список без списка символов
		Password = ''.join(random.sample(ListFinal, LenInt))
		print('\n')
		print(Password)
		#print(''.join(Password))

	#	
	else:
		print('\n')
		print('ОШИБКА: Не распознанная команда!')


if Password == '':
	generated()


InpBase = (ForNet, Login, Password)
print(InpBase)

conn = sqlite3.connect('password.db')
cur = conn.cursor()


def Database():
	cur.execute("""CREATE TABLE IF NOT EXISTS password(
   		ForSoc TEXT,
   		Login TEXT,
   		Pass TEXT);
	""")
	conn.commit()


def InputBase():
	cur.execute("INSERT INTO password VALUES(?, ?, ?);", InpBase)
	conn.commit()

Database()
InputBase()