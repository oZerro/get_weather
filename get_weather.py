import requests
from requests.exceptions import HTTPError


ALL_CITIES = ['Лондон', 'Шереметьево', 'Череповец']


def get_the_weather(city: str):
    params = {'lang': 'ru', 'n': '', 'T': '', 'm': '', 'q': ''}
    
    link = f"https://wttr.in/{city}"
    response = requests.get(link, params=params)
    response.raise_for_status()

    return response.text


def main():
    for city in ALL_CITIES:
        try:
            print(get_the_weather(city), sep="\n") 
        except HTTPError as ex:
            print("Ошибка подключения HTTPError")


if __name__ == '__main__':
    main()
    



