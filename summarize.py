import json
import matplotlib.pyplot as plt
from collections import Counter
from config import news_file, report_file, keywords

def summarize():
    counts = Counter()
    try:
        with open(news_file, "r", encoding="utf-8") as f:
            for line in f:
                obj = json.loads(line)
                text = obj.get("news", "")
                for kw in keywords:
                    if kw.lower() in text.lower():
                        counts[kw] += 1
    except FileNotFoundError:
        print("Henüz haber dosyası yok:", news_file)
        return

    if not counts:
        print("Özet: hiç ilgili haber yok.")
        return

    names = list(counts.keys())
    vals = [counts[n] for n in names]

    plt.figure(figsize=(6,4))
    plt.bar(names, vals)
    plt.title("STM News Count")
    plt.xlabel("Keyword")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(report_file)
    print("Grafik kaydedildi ->", report_file)
