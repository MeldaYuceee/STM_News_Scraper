import json
import os

def ensure_dirs():
    os.makedirs(os.path.join("..", "data"), exist_ok=True)
    os.makedirs(os.path.join("..", "reports"), exist_ok=True)

def save_news(news_list, file_path):
    ensure_dirs()
    with open(file_path, "a", encoding="utf-8") as f:
        for news in news_list:
            f.write(json.dumps({"news": news["title"]}, ensure_ascii=False) + "\n"
            print(f"{len(news_list)} haber kaydedildi -> {file_path}")
