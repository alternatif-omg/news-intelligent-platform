TOPIC_KEYWORDS = {
    "politik": {"pemilu", "presiden", "parlemen"},
    "ekonomi": {"inflasi", "rupiah", "pasar"},
    "teknologi": {"ai", "teknologi", "startup"},
    "olahraga": {"liga", "gol", "pemain"}
}


def detect_topic(tokens):
    for topic, keywords in TOPIC_KEYWORDS.items():
        if set(tokens) & keywords:
            return topic
    return "umum"
