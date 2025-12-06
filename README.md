# STM News Scraper – Automated Web News Extraction

> **Domain:** Web Scraping / OSINT-like Data Collection  
> **Level:** Prototype (Student R&D)  
> **Purpose:** Retrieve recent STM news releases programmatically and list them in a structured format

---

## 1. Background & Overview
STM publishes frequent news articles and press releases related to defense projects, technology demonstrations and company announcements.  
This project provides a **minimal web scraping pipeline** that collects titles and URLs from the public STM website and displays them in a clean list.

The goal is to demonstrate basic scraping techniques using Python and Selenium/BeautifulSoup.

---

## 2. Features
- Fetch recent STM news and press releases  
- Extract title and URL for each entry  
- Print them in a readable output format  
- Simple code structure suitable for beginners  
- Includes optional Pandas handling for further processing  

---

## 3. Technologies
- Python 3.x  
- Selenium  
- BeautifulSoup  
- Pandas (optional)

---

## 4. Installation & Run

Clone the repository:
```bash
git clone <repo-link>
cd stm-news-scraper
Create a virtual environment:

bash
Kodu kopyala
python -m venv .venv
Activate:

bash
Kodu kopyala
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
Install dependencies:

bash
Kodu kopyala
pip install -r requirements.txt
Run:

bash
Kodu kopyala
python main.py
5. Example Output
perl
Kodu kopyala
27 AUG 2025 - STM, TEKNOFEST Participates… 
https://www.stm.com.tr/tr/haberler/stm-teknofest...

07 AUG 2025 - ALPAGUT Firing Test Completed…
https://www.stm.com.tr/tr/haberler/alpagut-akinci...
6. Notes
Works on public pages only

Execution time depends on page load and Selenium driver

Scraped results may vary based on STM website layout changes

7. Next Steps
Export results to CSV or JSON

Schedule periodic scraping (cron)

Filter by keywords

Store data locally

Add date normalization

