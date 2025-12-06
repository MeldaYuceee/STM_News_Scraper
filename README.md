# STM News Scraper – Automated Retrieval of STM News & Press Releases

> **Domain:** Web Scraping / OSINT-style Information Collection  
> **Level:** Prototype (Student R&D)  
> **Purpose:** Programmatically retrieve public STM news items (titles + URLs) and list them for quick review

---

## 1. Overview & Motivation
STM publishes regular announcements, press releases and defense-related updates. Keeping track of these manually becomes time-consuming as the volume increases.

This project builds a **minimal automated retrieval tool** that:
- visits STM’s official website,
- extracts recent news headlines and URLs,
- prints them in a structured format,
- prepares the data for further analysis (e.g., keywords, dates, topics).

The result is an introductory example of automation for **public information monitoring**.

---

## 2. What the Script Does
- Opens STM news page
- Scrapes all visible articles
- Extracts headline + link
- Outputs results in a clean list
- (Optional) converts data to CSV/JSON

This represents a simple baseline for automated information collection.

---

## 3. Technologies
- Python 3.x  
- Selenium  
- BeautifulSoup  
- Pandas (optional)

---

## 4. Installation & Run

Clone:
```bash
git clone <repo-link>
cd stm-news-scraper
