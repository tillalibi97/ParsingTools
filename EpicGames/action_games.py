import requests
from bs4 import BeautifulSoup

start = 0
txt = open('action_games.txt', 'w', encoding="utf-8")
counter = 1

while True:
    link = 'https://www.epicgames.com/store/ru/c/action-games?sortBy=releaseDate&sortDir=DESC&count=40&start='
    req = requests.get(link + str(start))
    html = BeautifulSoup(req.content, 'html.parser')
    items = html.select(".css-cnqlhg > .css-lrwy1y")
    if(len(items)):
        for game in items:
            title = game.select(".css-hkjq8i .css-1h2ruwl")
            name = str(title[0].text)
            txt.write(str(counter) + ' ' + name + '\n')
            counter += 1

        start += 40
    else:
        break
txt.close()