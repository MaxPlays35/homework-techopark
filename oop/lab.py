from typing import Tuple, Union


class Segment:
    def __init__(self, x_1: Union[int, float], y_1: Union[int, float],
                 x_2: Union[int, float], y_2: Union[int, float]) -> None:
        self.x_1 = x_1
        self.y_1 = y_1

        self.x_2 = x_2
        self.y_2 = y_2

        self.k = (self.y_2 - self.y_1) / (self.x_2 - self.x_1)
        self.b = self.y_1 - self.k * self.x_1

    def line_eq(self, x):
        return self.k * x + self.b

    @property
    def line_args(self):
        return self.k, self.b


sg_1 = Segment(1, 1, 3, 3)

sg_2 = Segment(3, -1, 2, 2)


def intersection(sg_1: Segment, sg_2: Segment):
    k_1, b_1 = sg_1.line_args
    k_2, b_2 = sg_2.line_args

    x = (b_2 - b_1) / (k_1 - k_2)

    if sg_1.line_eq(x) == sg_2.line_eq(x):
        return True, x, sg_1.line_eq(x)

    return False, 0, 0


def check(sg_1, sg_2, point: Tuple[bool, any, any]):
    inter, x, y = point

    if inter and (min(sg_1.x_1, sg_1.x_2) <= x <= max(sg_1.x_1, sg_1.x_2)
            and min(sg_1.y_1, sg_1.y_2) <= y <= max(sg_1.y_1, sg_1.y_2)) and (
                min(sg_2.x_1, sg_2.x_2) <= x <= max(sg_2.x_1, sg_2.x_2)
                and min(sg_2.y_1, sg_2.y_2) <= y <= max(sg_2.y_1, sg_2.y_2)):
        return f"Intersection found: (x, y) {x, y}"
    return "Intersection was not found"


print(check(sg_1, sg_2, intersection(sg_1, sg_2)))
