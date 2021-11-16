import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

page = 1
all_data = {'date': [],
            'topic_name': [],
            'topic_url': [],
            'description': [],
            'author': []}

for _ in range(3):
    link = 'https://www.nature.com/nature/research-articles?searchType=journalSearch&sort=PubDate&page='
    req = requests.get(link + str(page))
    html = bs(req.content, 'html.parser')
    items = html.select('.app-article-list-row > .app-article-list-row__item')

    for article in items:
        topic_name = article.select('.c-card__title > a')
        topic_name_ = str(topic_name[0].text)
        all_data['topic_name'].append(topic_name_)

        topic_url = article.find('a').get('href')
        topic_url_ = str(topic_url)
        all_data['topic_url'].append(topic_url_)

        topic_desc = article.select('.c-card__summary > p')
        if len(topic_desc) > 0:
            topic_desc_ = str(topic_desc[0].text)
            all_data['description'].append(topic_desc_)
        else:
            topic_desc_ = 'None'
            all_data['description'].append(topic_desc_)

        topic_auth = article.select('.c-author-list > li')
        topic_auth_ = ''
        for auth in topic_auth:
            auth_ = auth.select('span')
            topic_auth_ += str(auth_[0].text + ', ')
        all_data['author'].append(topic_auth_[:-2])

        date = article.find('time').get('datetime')
        all_data['date'].append(date)
    page += 1
df = pd.DataFrame(all_data)

df.to_csv('all_data.csv')