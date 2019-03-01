#Перепишите функцию ask_user() из задания про while, чтобы она перехватывала KeyboardInterrupt, писала пользователю "Пока!" и завершала работу при помощи оператора break

answers_catalogue = {'Как дела?': 'Хорошо',
'Что делаешь?': 'Программирую', 
'Ты кто по жизни?': 'Какая тебе разница?', 
'Любишь Python?': 'Конечно!',
'Как тебе погода': 'Фигня полная',
'А ты человек?': 'Ну конечно...',
'Ха-ха': 'Как смешно!'
}

def ask_user():
	while True:
		try:
			user_say = input('Спроси у меня что-нибудь: ')
			if user_say in answers_catalogue:
				print(answers_catalogue.get(user_say))
				continue
			else:
				print(f'Сам ты {user_say}')
		except KeyboardInterrupt:
			print("Пока!")
			break

ask_user()