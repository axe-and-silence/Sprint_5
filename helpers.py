import random,string

class Helpers:

    #Метод генерации валидного мыла нового пользовтеля
    def new_user_email ():
        # Определяем набор символов для локальной части (до @)
        chars = string.ascii_lowercase + string.digits  # Только буквы и цифры
    # Случайная длина имени пользователя от 5 до 10 символов
        username_length = random.randint(5, 10)
    # Генерируем случайное имя
        username = ''.join(random.choice(chars) for _ in range(username_length))
    # Гарантируем, что имя не начинается с цифры (по спецификации RFC)
        #if username.isdigit():
            #username = random.choice(string.ascii_lowercase) + username
    # Фиксированный домен
        domain = "@example.com"
        new_user_email = username + domain 
        return new_user_email

# Метод генерации невалидного мыла нового пользовтеля
    def new_user_invalid_email():
	# Определяем набор символов для локальной части (до @)
        chars = string.ascii_lowercase + string.digits  # Только буквы и цифры
    # Случайная длина имени пользователя от 5 до 10 символов
        username_length = random.randint(5, 10)
    # Генерируем случайное имя
        new_user_email = ''.join(random.choice(chars) for _ in range(username_length))
        return new_user_email