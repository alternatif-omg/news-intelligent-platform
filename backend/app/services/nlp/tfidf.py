from collections import Counter
import math


def compute_tf(tokens):
    tf = Counter(tokens)
    total = len(tokens)
    return {k: v / total for k, v in tf.items()}


def compute_idf(docs):
    idf = {}
    total_docs = len(docs)

    for doc in docs:
        for word in set(doc):
            idf[word] = idf.get(word, 0) + 1

    return {
        word: math.log(total_docs / (1 + count))
        for word, count in idf.items()
    }


def compute_tfidf(tokens, idf):
    tf = compute_tf(tokens)
    return {
        word: tf[word] * idf.get(word, 0)
        for word in tf
    }
