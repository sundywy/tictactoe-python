WINNING_MOVES = [
    [[0, 0], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
    [[0, 0], [1, 1], [2, 2]],
    [[0, 2], [1, 1], [2, 0]],
]


class Board:
    def __init__(self) -> None:
        self.grid = [[None for _ in range(3)] for _ in range(3)]

    def __str__(self) -> str:
        strs = []
        for c in self.grid:
            strs.append("-------")
            strs.append(" ".join([f"{x} " if x else " " for x in c]))
        strs.append("-------")

        return "\n".join(strs)

    def __getitem__(self, loc):
        x, y = loc
        return self.grid[x][y]

    def __setitem__(self, loc, value):
        if not self._is_in_bound(loc):
            raise ValueError("Location not in bound")

        if not self._is_empty(loc):
            raise ValueError("Location is not empty")

        x, y = loc
        self.grid[x][y] = value

    def _is_in_bound(self, loc):
        x, y = loc
        return 0 <= x <= 2 and 0 <= y <= 2

    def _is_empty(self, loc):
        return self[loc] is None

    @property
    def is_full(self):
        for c in self.grid:
            if not all([x is not None for x in c]):
                return False
        return True

    @property
    def is_have_winner(self):
        for move in WINNING_MOVES:
            vals = [self[x] for x in move]
            if not all(vals):
                continue

            if len(set(vals)) == 1:
                return True

        return False
