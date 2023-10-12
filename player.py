class Player:
    def __init__(self, value) -> None:
        self.value = value

    def get_pos(self):
        return tuple(map(int, input().split(",")))

    def __str__(self) -> str:
        return self.value
