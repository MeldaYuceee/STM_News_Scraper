# STM News Scraper

STM News Scraper, STM web sitesindeki haberler ve basın bültenlerini otomatik olarak çeken basit bir Python projesidir. Proje, başlıkları ve linkleri toplar ve hızlıca görüntülemenizi sağlar. Öğrenci projeleri için uygun bir web scraping örneğidir.

---

## 🚀 Özellikler

- STM web sitesindeki **haberler** ve **basın bültenleri**ni toplar.
- Başlık ve linkleri çekip liste halinde gösterir.
- Kullanımı kolay ve anlaşılır bir kod yapısına sahiptir.
- Python ve Selenium/BeautifulSoup kullanır.
- Öğrenci seviyesinde bir scraping projesi olarak tasarlanmıştır.

---

## 🛠️ Teknolojiler

- Python 3.x
- Selenium
- BeautifulSoup
- pandas (opsiyonel, veri işleme için)

---

## 💻 Kurulum ve Kullanım

1. Projeyi bilgisayarına klonla:

```bash
git clone <repo-link>
cd stm-news-scraper
Sanal ortam oluştur ve aktifleştir:

python -m venv .venv
# Windows PowerShell
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


Gerekli kütüphaneleri yükle:
pip install -r requirements.txt
main.py dosyasını çalıştır:
python main.py


Çıktıda haber başlıkları ve linklerini görebilirsiniz:
27AĞU2025 - STM, TEKNOFEST Mavi Vatan’da Yerini Alıyor (https://www.stm.com.tr/tr/haberler/stm-teknofest-mavi-vatanda-yerini-aliyor)
07AĞU2025 - ALPAGUT, AKINCI TİHA’dan Atışını Başarıyla Tamamladı (https://www.stm.com.tr/tr/haberler/alpagut-akinci-tihadan-atisini-basariyla-tamamladi)
25TEM2025 - KarguFPV Yeni Zırhını Kuşandı (https://www.stm.com.tr/tr/haberler/kargufpv-yeni-zirhini-kusandi)
25TEM2025 - STM, Dikey-İniş Kalkış Yapan Taktik İHA’sı “STM VTOL”ü İlk Kez IDEF’te Tanıttı (https://www.stm.com.tr/tr/haberler/stm-dikey-inis-kalkis-yapan-taktik-ihasi-stm-vtolu-ilk-kez-idefte-tanitti)
