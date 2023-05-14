import pytest
from queries import count_world, count_, count_queries, queries


@pytest.mark.parametrize('lists', [['one people', 'two person', 'three mini dogs', 'four tall girl', 'five guys'],
                                   ['cow', 'one piece', 'baby']])
def test_count_world(lists):
    assert len(count_world(lists)) == len(lists)
    assert len(count_world(queries)) == len(queries)

