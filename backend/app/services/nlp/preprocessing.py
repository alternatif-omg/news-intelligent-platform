import re
from typing import List

STOPWORDS_ID = {
    "yang", "dan", "di", "ke", "dari", "untuk", "dengan",
    "pada", "adalah", "ini", "itu", "oleh"
}


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+", "", text)      
    text = re.sub(r"[^a-z\s]", "", text)     
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str) -> List[str]:
    return text.split()


def remove_stopwords(tokens: List[str]) -> List[str]:
    return [t for t in tokens if t not in STOPWORDS_ID]


def preprocess_text(text: str) -> List[str]:
    cleaned = clean_text(text)
    tokens = tokenize(cleaned)
    tokens = remove_stopwords(tokens)
    return tokens
