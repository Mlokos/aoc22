from typing import Tuple


def get_compartments(line: str) -> Tuple[str, str]:
    comp_1 = line[: int(len(line) / 2)]
    comp_2 = line[-int(len(line) / 2) :]

    return comp_1, comp_2


def get_duplicate(comp_1: str, comp_2: str) -> str:
    set_1 = set(comp_1)
    set_2 = set(comp_2)

    set_sum = list(set_1) + list(set_2)

    duplicate = [item_type for item_type in set_sum if set_sum.count(item_type) > 1]
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

    results = [get_type_value(get_duplicate(*get_compartments(line))) for line in lines]
    print(sum(results))
