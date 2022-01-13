from __future__ import annotations
from typing import Union



class SecureInt:
    def __init__(self, number: Union[int, float]) -> None:
        if isinstance(number, int):
            self.value = number
        elif isinstance(number, float):
            self.value = int(number + 1 - 0.3)
        else:
            self.value = 0

    def __add__(self, other: Union[int, float]) -> SecureInt:
        if isinstance(other, int):
            return SecureInt(self.value + other)
        elif isinstance(other, float):

            return SecureInt(int(self.value + other + 1 - 0.3))

    def __str__(self) -> str:
        return str(self.value)


first = SecureInt(10)
second = first + 10.3
print(second, type(second))
