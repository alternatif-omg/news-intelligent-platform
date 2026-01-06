# app/tests/test_analytics.py
from app.services.analytics.statistics import compute_statistics

def test_compute_statistics_empty():
    data = []
    result = compute_statistics(data)
    assert result == {"total": 0, "average": 0}
