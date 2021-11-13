import requests
from bs4 import BeautifulSoup


image_number = 1
link = f"https://wallpapers.com/berserk"

responce = requests.get(f'{link}').text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('ul', class_ = 'card-columns')
all_image = block.find_all('li', class_ = 'card content')

for image in all_image:
    image_link = image.find('a').get('href')
    image_data = str(image_link[:23] + 'images/file' + image_link[33:-4] + 'jpg')

    image_bytes = requests.get(f'{image_data}').content

    with open(f'123/{image_number}.jpg', 'wb') as file:
        file.write(image_bytes)
    print(f"Изображение {image_number}.jpg yспешно скачано!")
    image_number += 1
