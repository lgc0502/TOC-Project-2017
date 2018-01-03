from bs4 import BeautifulSoup

import requests


def get_web_page(url):
    resp = requests.get(
        url=url,
        #cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text

def get_articles(dom):
    soup = BeautifulSoup(dom, 'html.parser')

    articles = []  # 儲存取得的文章資料
    trs = soup.find_all('div', 'TODAY_CONTENT')
   
    for t in trs:
        luck = t.find('span','txt_green').string
        luck_1 = t.find('p').next_sibling.string
        love = t.find('span','txt_pink').string
        love_1 = t.find('p').next_sibling.next_sibling.next_sibling.next_sibling.string
        work = t.find('span','txt_blue').string
        work_1 = t.find('p').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string
        money = t.find('span','txt_orange').string
        money_1 = t.find('p').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string
        #print(work_1)
        articles.append(luck)
        articles.append(luck_1)
#        articles.append("\n")
        articles.append(love)
        articles.append(love_1)
#        articles.append("\n")
        articles.append(work)
        articles.append(work_1)
#        articles.append("\n")
        articles.append(money)
        articles.append(money_1)
#        articles.append("\n")
    return articles

