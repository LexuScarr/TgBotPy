from os import close
import requests
from bs4 import BeautifulSoup


print("Добро пожаловать в рандомайзер аниме\n"
      "Для поиска случайно аниме введите 1\n"
      "Для выхода из приложения введите 0. \nУдачи")
number = int(input())
while number == 1:
    url = 'https://animego.org/anime/random'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    # print(f"подключение : {response.status_code}")
    soup = BeautifulSoup(response.content, "html.parser")
    nazvanie = soup.find('div', {'class' :'anime-title'}).find('h1')
    print ('Аниме: ' + nazvanie.text)
    animetyp = soup.find('div', class_= 'anime-info').find_all("dt")
    animetyp1 = soup.find('div', class_= 'anime-info').find_all("dd")
    print(animetyp[0].get_text(strip=True), animetyp1[0].get_text(strip=True))
    print(animetyp[1].get_text(strip=True), animetyp1[1].get_text(strip=True))
    print(animetyp[5].get_text(strip=True), animetyp1[5].get_text(strip=True))
    print('Для поиска введите цифру 1 \n')
    number = int(input())
    print("Ищем следующее... \n")
if number == 0:
      print('poka')
else:
      print('ne ponual')
