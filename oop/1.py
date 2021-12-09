from typing import Union


class test:
    def __init__(self):
        pass

    def test(self):
        return "Tested"


print(test.test(""))


class Rectange:
    __height = 0
    __width = 0
    __area = 0
    __perimeter = 0

    def __init__(self) -> None:
        pass

    def getHigh(self) -> Union[int, float]:
        return self.__heigth

    def setHigh(self, new_height: Union[int, float]) -> None:
        assert new_height > 0, 'Height must greater than 0'
        self.__heigth = new_height

    def setLength(self, new_width: Union[int, float]) -> None:
        assert new_width > 0, 'Width must greater than 0'
        self.__width = new_width

    def getLength(self) -> Union[int, float]:
        return self.__width

    def getSquare(self) -> Union[int, float]:
        return self.__width * self.__heigth

    def getPeremeter(self) -> Union[int, float]:
        return 2 * (self.__width + self.__heigth)
