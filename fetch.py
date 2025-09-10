import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.stm.com.tr/tr/medya/duyurular"

def fetch_news():
    news_list = []

    response = requests.get(BASE_URL)
    if response.status_code != 200:
        print("Haberler çekilemedi!")
        return news_list

    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.select(".card-body")

    for item in items:
        title_tag = item.select_one("a")
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = "https://www.stm.com.tr" + title_tag.get("href")
            news_list.append({"title": title, "link": link})

    return news_list
