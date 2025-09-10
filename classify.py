
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

training_data = [
    ("STM launches new UAV prototype", "drone"),
    ("Radar technology upgraded for national defense", "radar"),
    ("New export contract signed by STM", "ihracat"),
    ("New project on İHA development", "İHA"),
    ("STM develops new defense technology", "savunma")
]

texts, labels = zip(*training_data)

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X_train, labels)

def classify_headlines(headlines):

    if not headlines:
        return []

    X = vectorizer.transform(headlines)
    predicted = model.predict(X)
    return predicted

training_data = [
    ("STM launches new UAV prototype", "drone"),
    ("Radar technology upgraded for national defense", "radar"),
    ("New export contract signed by STM", "ihracat"),
    ("New project on İHA development", "İHA"),
    ("STM develops new defense technology", "savunma")
]

texts, labels = zip(*training_data)

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X_train, labels)

def classify_headlines(headlines):
    X = vectorizer.transform(headlines)
    predicted = model.predict(X)
    return predicted
