from enum import Enum
from typing import Tuple


class RPCtype(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class RESULTtype(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6


def decode_command(command: str) -> Tuple[RPCtype, RESULTtype]:
    opponent_mapping = {"A": RPCtype.ROCK, "B": RPCtype.PAPER, "C": RPCtype.SCISSORS}
    player_mapping = {"X": RESULTtype.LOSE, "Y": RESULTtype.DRAW, "Z": RESULTtype.WIN}

    opponent = opponent_mapping[command[0]]
    player = player_mapping[command[-1]]

    return opponent, player


def get_result(opponent: RPCtype, player: RESULTtype) -> int:
    result = int(player.value)
    base_value = None

    if player == RESULTtype.DRAW:
        base_value = int(opponent.value) + 1
    elif player == RESULTtype.LOSE:
        base_value = (int(opponent.value) - 1) % 3 + 1
    elif player == RESULTtype.WIN:
        base_value = (int(opponent.value) + 1) % 3 + 1

    return base_value + result


if __name__ == "__main__":
    f = open("input", "r")
    lines = f.readlines()
    lines = [x.split("\n")[0] for x in lines]
    results = [get_result(*decode_command(x)) for x in lines]
    print(sum(results))
