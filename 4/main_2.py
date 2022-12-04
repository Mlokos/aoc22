import re


def is_one_into_another(line: str) -> bool:
    numbers = re.findall(r"\d+", line)
    numbers = [int(x) for x in numbers]

    if numbers[0] in range(numbers[2], numbers[3] + 1):
        return True
    elif numbers[1] in range(numbers[2], numbers[3] + 1):
        return True
    elif numbers[2] in range(numbers[0], numbers[1] + 1):
        return True
    elif numbers[3] in range(numbers[0], numbers[1] + 1):
        return True
    else:
        return False


if __name__ == "__main__":
    f = open("input", "r")
    lines = f.readlines()
    lines = [x.split("\n")[0] for x in lines]

    results = [is_one_into_another(x) for x in lines]
    results = list(filter(lambda x: x, results))
    print(len(results))
