from itertools import groupby


if __name__ == "__main__":
    f = open("input", "r")
    lines = f.readlines()
    groups = (list(g) for _, g in groupby(lines, key=lambda x: x == "\n"))
    groups = list(filter(lambda x: x != ["\n"], groups))
    groups = [list(map(lambda x: int(x.split("\n")[0]), group)) for group in groups]
    g_sum = [sum(group) for group in groups]
    print(max(g_sum))
