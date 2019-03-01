#Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
#Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в словаре, программа давала ему соотвествующий ответ

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
		user_say = input('Спроси у меня что-нибудь: ')
		if user_say in answers_catalogue:
			print(answers_catalogue.get(user_say))
			continue
		else:
			print(f'Сам ты {user_say}')

ask_user()