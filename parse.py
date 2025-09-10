from bs4 import BeautifulSoup

def parse_news(html):
    soup = BeautifulSoup(html, "html.parser")
    headline_elements = soup.select("h2 a")
    headlines = [el.get_text(strip=True) for el in headline_elements]

    if headlines:
        print("Bulunan başlıklar:")
        for h in headlines:
            print(" -", h)
    else:
        print("Hiç başlık bulunamadı.")

    return headlines
