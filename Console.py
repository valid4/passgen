from passgen import Gen #generator, CheckBase 

Generate = Gen()

while True:
	Command = input('Выберите действие:\n1) Создать пароль\n2) Посмотреть сохраненные пароли\n3) Удалить запись\n4) Завершить программу\n')

	if Command == '1':
		Generate.generator()
		print('\n')

	elif Command == '2':
		Generate.CheckBase()
		print('\n')

	elif Command == '3':
		Generate.Delite()
		print('\n')

	elif Command == '4':
		break

	else:
		print('ОШИБКА: Команда не распознана!')