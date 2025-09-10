from config import keywords

def filter_news(headlines):
    filtered = []
    for h in headlines:
        for kw in keywords:
            if kw.lower() in h["title"].lower():
                filtered.append(h)
                break
    return filtered
