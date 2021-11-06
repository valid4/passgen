import random 
#from database import DataBase
from datetime import datetime 
import sqlite3

conn = sqlite3.connect('password.db')
cur = conn.cursor()

def generator():
	LowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	CapitalLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '_', '=', '?', '&', '$', '%', '#', '\\', '|', '/']
	Password = None
	#
	ForNet = input('Для чего пароль? \n')

	Login = input('Вы можете указать логин.\nЕсли не хотите указывать логин нажмите Enter:\n')

	Password = input('Если вы хотите добавить существующий аккаунт, то введите пароль. Если создать новый, то нажмите Enter: \n' )

	# Создаю функцию генератора 
	def generated():

		# Пока while - True выполняется цикл(до того момента пока не будет указано число)
		while True:
			try:
				Len = input('Какой длины пароль? \n(Введите число)\n') # Ввожу длину пароля
				LenInt = int(Len) # Перевожу в целочисленный тип
				break
			except Exception:
				print('<|ПОЖАЛУЙСТА ВВЕДИТЕ ЧИСЛО|>')
				

		SymInp = input('Хотите использовать символы?\nВведите \"y\", если да и \"n\", если нет: \n')

		nonlocal Password

		# Условие 
		if SymInp == 'y' or SymInp == 'Y' or SymInp == 'yes' or SymInp == 'Yes' or SymInp == 'YES' or SymInp == 'д' or SymInp == 'да' or SymInp == 'Д' or SymInp == 'Да' or SymInp == 'ДА': 
			ListFinal = LowerLetters + CapitalLetters + numbers + symbols # Объединяем списки в один список с учетом списка символов
			Password = ''.join(random.sample(ListFinal, LenInt)) # Создаем рандомный пароль из общего списка с указанной длиной (преобразуем спсок в строку)
			#print('\n')
			#print(Password) # Выводим полученный пароль (преобразуем спсок в строку)

		#	
		elif SymInp == 'n' or SymInp == 'N' or SymInp == 'no' or SymInp == 'No' or SymInp == 'NO' or SymInp == 'н' or SymInp == 'нет' or SymInp == 'Н' or SymInp == 'Нет' or SymInp == 'НЕТ':
			ListFinal = LowerLetters + CapitalLetters + numbers # Объединяем списки в один список без списка символов
			Password = ''.join(random.sample(ListFinal, LenInt))
			#print('\n')
			#print(Password)
			#print(''.join(Password))

		#	
		else:
			print('\n')
			print('ОШИБКА: Не распознанная команда!')


	if Password == '':
		generated()

	Comment = input('Вы можете добавить комментарий к учетной записи. Если не хотите комментировать нажмите Enter:\n')	

	Date = datetime.now().strftime("%H:%M %d.%m.%Y")

	InpBase = (ForNet, Login, Password, Date, Comment)
	print(' '.join(InpBase))

	#conn = sqlite3.connect('password.db')
	#cur = conn.cursor()


	def Database():
		cur.execute("""CREATE TABLE IF NOT EXISTS password(
	   		ForSoc TEXT,
	   		Login TEXT,
	   		Pass TEXT,
	   		Data TEXT,
	   		Comment TEXT);
		""")
		conn.commit()


	def InputBase():
		cur.execute("INSERT INTO password VALUES(?, ?, ?, ?, ?);", InpBase)
		conn.commit()

	Database()
	InputBase()


def CheckBase():
	cur.execute("SELECT * FROM password;")
	result = cur.fetchall()

	print(result)
	#cur.execute("SELECT * FROM password;")
	#result = cur.fetchall()
	#print(result)
	#res = result
	#print(' '.join(res))

	#base = DataBase()
	#base.Database()
	#base.InputBase(self, inp = InpBase)	
#generator()	