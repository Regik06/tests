import pytest
from geo_id import unic_geo, ids

@pytest.mark.parametrize(
    'dict1', [{'key1': [1, 1, 15, 15, 1],
              'key2': [2, 22, 2, 3],
               'key3':[11, 15, 1, 3, 76]}]
)
def test_geo_id(dict1):
    '''проверяем на уникальность значений в списке'''
    assert len(unic_geo(dict1)) == len(set(unic_geo(dict1)))


def test_none():
    '''проверка на пустоту'''
    expected = []
    dicts = {}
    assert unic_geo(ids) != expected
    assert unic_geo(dicts) == expected