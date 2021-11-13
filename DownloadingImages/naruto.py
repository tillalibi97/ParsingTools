import requests
from bs4 import BeautifulSoup


image_number = 0
link = f"https://wall.alphacoders.com/by_collection.php?id=654&lang=Russian"

responce = requests.get(f'{link}').text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id = 'big_container').find('div', class_ = 'center')
all_image = block.find_all('div', class_ = 'thumb-container-big')

for image in all_image:
    image_link = image.find('a').get('href')
    download_storage = requests.get(f'https://wall.alphacoders.com/{image_link}').text
    download_soup = BeautifulSoup(download_storage, 'lxml')
    download_block = download_soup.find('div', class_ = 'center img-container-desktop')
    result_link = download_block.find('a').get('href')

    # Download image
    image_bytes = requests.get(f'{result_link}').content

    with open(f'naruto/{image_number}.jpg', 'wb') as file:
        file.write(image_bytes)
    print(f"Изображение {image_number}.jpg yспешно скачано!")
    image_number += 1

