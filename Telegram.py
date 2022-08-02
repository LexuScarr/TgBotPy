from aiogram import types, executor, Dispatcher, Bot
import requests
from bs4 import BeautifulSoup


bot = Bot('token TG bots')
dp = Dispatcher(bot)

#command /start
@dp.message_handler(commands=['start'])
async def start(message: types.message):
    await bot.send_message(message.chat.id, " Я бот для поиска аниме с сайта Animego "
    + "\n" + "Для начала поиска введите название аниме" + "\n",
    parse_mode="html", disable_web_page_preview=1)

#parser
@dp.message_handler(content_types=['text'])
async def parser(message: types.message):
    url = 'https://animego.org/search/all?q=' + message.text
    await bot.send_message(message.chat.id, "Начинаю поиск аниме для тебя по запросу:"
        + "\n" + message.text + "\n" + url)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
#Поиск ссылок, после чего переход по каждой ссылке и парсить начинаем уже оттуда
    all_links = soup.find_all("a", class_="d-block")
    for link in all_links:
        url = link['href']
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

#поиск названий аниме
        nazvanie = soup.find('div', {"class" :'anime-title'})
        nazvanie1 = nazvanie.find('h1').text
        # for nazvanie1 in nazvanie:
        #     nazvanie1 = nazvanie1.text

#вывод названий и ссылки на аниме
        # await bot.send_message(message.chat.id, "Нашёл пару аниме для тебя: " + '\n' + nazvanie1 + '\n' + f"<a href='{url}'>Ссылка на анимеху</a>", parse_mode="html")
#поиск фотографий
        img = soup.find("div", class_="anime-poster position-relative cursor-pointer")
        img1 = img.find("img")
        img1 = img1['src']
#вывод фото, названий и ссылки на аниме
        await bot.send_photo(message.chat.id, img1, "Нашёл пару аниме для тебя: " + '\n' + nazvanie1 + '\n' + f"<a href='{url}'>Ссылка на анимеху</a>", parse_mode="html")




#Остановка цикла тремя выводами
        if all_links.index(link) == 2:
            break

executor.start_polling(dp)
