from typing import List
from itertools import islice


def get_groups(lines: List):
    iter_0 = islice(lines, 0, len(lines), 3)
    iter_1 = islice(lines, 1, len(lines), 3)
    iter_2 = islice(lines, 2, len(lines), 3)

    return list(zip(iter_0, iter_1, iter_2))


def get_duplicate(comp_1: str, comp_2: str, comp_3) -> str:
    set_1 = set(comp_1)
    set_2 = set(comp_2)
    set_3 = set(comp_3)

    set_sum = list(set_1) + list(set_2) + list(set_3)

    duplicate = [item_type for item_type in set_sum if set_sum.count(item_type) > 2]
    return duplicate[0]


def get_type_value(character: str) -> int:
    raw = ord(character)

    if raw < 95:
        return raw - 65 + 27
    else:
        return raw - 97 + 1


if __name__ == "__main__":
    f = open("input", "r")
    lines = f.readlines()
    lines = [x.split("\n")[0] for x in lines]

    results = [get_type_value(get_duplicate(x, y, z)) for x, y, z in get_groups(lines)]
    print(sum(results))
