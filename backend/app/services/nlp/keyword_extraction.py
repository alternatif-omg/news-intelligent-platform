from app.services.nlp.tfidf import compute_idf, compute_tfidf


def extract_keywords(docs, top_k=5):
    idf = compute_idf(docs)
    keywords = []

    for tokens in docs:
        tfidf = compute_tfidf(tokens, idf)
        sorted_words = sorted(
            tfidf.items(), key=lambda x: x[1], reverse=True
        )
        keywords.append([w for w, _ in sorted_words[:top_k]])

    return keywords
