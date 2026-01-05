import time
from collections import defaultdict

RATE_LIMIT = 60  # requests
WINDOW = 60      # seconds
client_requests = defaultdict(list)


def rate_limit(client_ip: str):
    now = time.time()
    requests = client_requests[client_ip]

    client_requests[client_ip] = [
        t for t in requests if now - t < WINDOW
    ]

    if len(client_requests[client_ip]) >= RATE_LIMIT:
        return False

    client_requests[client_ip].append(now)
    return True
