import requests
import fake_useragent
from bs4 import BeautifulSoup


session = requests.Session()
link = "https://bfme-modding.ru/index/sub/"
user = fake_useragent.UserAgent()
header = {
    'user-agent': user.random
}
data = {
    'a': '2',
    'user': 'powerful_thor',
    'password': 'qwert123',
    'ajax': '1',
    'rnd': '228',
    '_tp_': 'xml',
}
responce = session.post(link, data=data, headers=header)
profile_info = "https://bfme-modding.ru/index/8"
profile_responce = session.get(profile_info, headers = header).text


cookies_dict = [
    {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
    for key in session.cookies
]

session2 = requests.Session()

for cookies in cookies_dict:
    session2.cookies.set(**cookies)
resp = session2.get(profile_info, headers = header)
# print(resp.text)
soup = BeautifulSoup(resp.text, 'lxml')
block = soup.find('div', class_ = "profile")

# Show profile name

check_pro = block.find('div', class_ = 'profile-full-name-row')
status_pro = check_pro.find_all('span')[0].text
result_pro = f'Your profile name is {status_pro}'
print(result_pro)