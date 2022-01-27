class Transport:
    def __init__(self, passangers, team, speed) -> None:
        if speed < 0:
            raise ValueError("Speed must be greater zero")
        self.passangers = passangers
        self.team = team
        self.speed = speed
        self.matrix = [
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 0]
        ]

    def transfer(self, x, y):
        if self.matrix[y][x]:
            return True
        return False


class Car(Transport):
    def __init__(self, passangers=4, team=1, speed=100) -> None:
        super().__init__(passangers, team, speed)


class Train(Transport):
    def __init__(self, passangers=200, team=2, speed=150) -> None:
        super().__init__(passangers, team, speed)


class Plane(Transport):
    def __init__(self,  passangers=100, team=2, speed=200) -> None:
        super().__init__(passangers, team, speed)
