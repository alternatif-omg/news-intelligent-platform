TOPIC_KEYWORDS = {
    "politik": {"pemilu", "presiden", "parlemen", "pemerintah"},
    "ekonomi": {"inflasi", "rupiah", "pasar", "bisnis", "crypto"},
    "teknologi": {"ai", "teknologi", "startup", "digital", "blockchain"},
    "olahraga": {"liga", "gol", "pemain", "tim","pelatih", "lapangan"}
}


def detect_topic(tokens):
    for topic, keywords in TOPIC_KEYWORDS.items():
        if set(tokens) & keywords:
            return topic
    return "umum"
