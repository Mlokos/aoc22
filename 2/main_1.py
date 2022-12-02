from enum import Enum
from typing import Tuple


class RPCtype(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


def decode_command(command: str) -> Tuple[RPCtype, RPCtype]:
    opponent_mapping = {"A": RPCtype.ROCK, "B": RPCtype.PAPER, "C": RPCtype.SCISSORS}
    player_mapping = {"X": RPCtype.ROCK, "Y": RPCtype.PAPER, "Z": RPCtype.SCISSORS}

    opponent = opponent_mapping[command[0]]
    player = player_mapping[command[-1]]

    return opponent, player


def get_result(opponent: RPCtype, player: RPCtype) -> int:
    base_value = int(player.value) + 1
    result = 0

    if opponent == player:
        result = 3
    elif (int(opponent.value) + 1) % 3 == int(player.value):
        result = 6

    return base_value + result


if __name__ == "__main__":
    f = open("input", "r")
    lines = f.readlines()
    lines = [x.split("\n")[0] for x in lines]
    results = [get_result(*decode_command(x)) for x in lines]
    print(sum(results))
