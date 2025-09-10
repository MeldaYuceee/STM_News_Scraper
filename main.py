from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# ✅ ChromeDriver yolunu buraya yaz
chrome_driver_path = r"C:\Users\user\Desktop\STM News Scraper\chromedriver.exe"
service = Service(chrome_driver_path)

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=chrome_options)

websites = [
    "https://www.stm.com.tr/tr/haberler",
    "https://www.stm.com.tr/tr/basin-bultenleri"
]

news_list = []

for url in websites:
    driver.get(url)
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    for item in soup.select(".list_news .list_item"):
        link = "https://www.stm.com.tr" + item.get("href", "")
        tarih_tag = item.select_one(".item_date")
        baslik_tag = item.select_one(".item_title")
        if link and baslik_tag:
            news_list.append({
                "tarih": tarih_tag.text.strip() if tarih_tag else "",
                "baslik": baslik_tag.text.strip(),
                "link": link
            })

    for item in soup.select(".list_pressrelease .list_item"):
        link = "https://www.stm.com.tr" + item.get("href", "")
        tarih_tag = item.select_one(".item_date")
        baslik_tag = item.select_one(".item_title")
        if link and baslik_tag:
            news_list.append({
                "tarih": tarih_tag.text.strip() if tarih_tag else "",
                "baslik": baslik_tag.text.strip(),
                "link": link
            })

driver.quit()


if news_list:
    for n in news_list[:20]:  # İlk 20 haberi göster
        print(f"{n['tarih']} - {n['baslik']} ({n['link']})")
else:
    print("Hiç haber bulunamadı.")
