
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

service = Service(r"C:\Users\user\OneDrive\fizik\chromedriver-win64\chromedriver.exe")

chrome_options = Options()

driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.stm.com.tr/tr/medya/duyurular"
driver.get(url)

SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, "html.parser")
news_list = []

for item in soup.select(".card-body h3 a"):
    title = item.get_text(strip=True)
    link = "https://www.stm.com.tr" + item.get("href")
    news_list.append({"title": title, "link": link})

if news_list:
    for n in news_list[:10]:  # İlk 10 haberi göster
        print(f"📌 {n['title']} ({n['link']})")
else:
    print("Hiç haber bulunamadı.")

driver.quit()
