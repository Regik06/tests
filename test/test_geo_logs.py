import pytest
from geo_logs import russia_visits, geo_logs

def test_russia_isinstanse():
    expected1 = [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]
    expected2 = [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Лиссабон', 'Португалия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]

    assert russia_visits(geo_logs) == expected1
    assert russia_visits(geo_logs) != expected2
