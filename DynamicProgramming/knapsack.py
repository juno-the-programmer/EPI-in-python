import collections
import functools
from typing import List

Item = collections.namedtuple('Item', ('value', 'weight'))

def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    @functools.lru_cache(None)
    def optimum_subject_to_item_and_capacity(k, available_capacity):
        if k < 0:
            return 0

        without_curr_item = optimum_subject_to_item_and_capacity(k - 1, available_capacity)
        with_curr_item = (0 if available_capacity < items[k].weight else
                            (items[k].value + optimum_subject_to_item_and_capacity(k - 1, available_capacity - items[k].weight)))
        return max(without_curr_item, with_curr_item)
    return optimum_subject_to_item_and_capacity(len(items) - 1, capacity)

table = [Item(60,5), Item(50,3), Item(70,4), Item(30,2)]
print(optimum_subject_to_capacity(table, 5))
    