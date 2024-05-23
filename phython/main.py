import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '34fb76d3650bb5a5d1a11d198738c696'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
# регистрация тренера
body_registration = {
    "trainer_token": TOKEN,
    "email": "Vladislav1995k@yandex.ru",
    "password": "Iloveqa11111"
} 
# активация тренера
body_confirmation  = {
    "trainer_token": TOKEN
}
# создание покемона
body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
# поменял имя покемона
body_to_change  = {
    "pokemon_id": "26229",
    "name": "Тетя Зина",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
}
# поймал покемона
body_add_pokeball = {
    "pokemon_id": "26229"
}

# регистрация тренера
response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)

# активация тренера
response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)

# создание покемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code)

message = response_create.json()['message']
print(message)

# поменял имя покемона
response_to_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_to_change)
print(response_to_change.text)

message = response_to_change.json()['message']
print(message)

# поймал покемона
response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

message = response_add_pokeball.json()['message']
print(message)



