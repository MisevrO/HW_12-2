# Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати тільки
# обʼєкти класу Point.
# Використовуйте property
# Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point).
# Реалізуйте перевірку даних, аналогічно до класу Line.
# Визначет атрибут, що містить площу трикутника (за допомогою property).
# Для обчислень можна використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)
#
import math

class Point:
    _x = None
    _y = None

    @property  # getter
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._x = value

    @property  # getter
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._y = value

    def __init__(self, x_coord, y_coord):
        if not isinstance(x_coord, int) or not isinstance(y_coord, int):
            raise TypeError
        self.x = x_coord
        self.y = y_coord


point1 = Point(1, 2)
point2 = Point(4, 5)
point = Point(1, 6)



class Line:
    _begin = None
    _end = None


    @property  # getter
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._begin = value

    @property  # getter
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._end = value


    def __init__(self, begin_point, end_point):
        if not isinstance(begin_point, Point) or not isinstance(end_point, Point):
            raise TypeError
        self.begin = begin_point
        self.end = end_point

    @property
    def length(self):

        return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5

line1 = Line(point2, point1)

print(line1.length)

class Triangle:
    _point1 = None
    _point2 = None
    _point3 = None

    @property  # getter
    def point1(self):
        return self._point1

    @point1.setter
    def point1(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._point1 = value

    @property  # getter
    def point2(self):
        return self._point2

    @point2.setter
    def point2(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._point2 = value

    @property  # getter
    def point3(self):
        return self._point3

    @point3.setter
    def point3(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._point3 = value

    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        self.point1 = point_1
        self.point2 = point_2
        self.point3 = point_3

    @property
    def triangle_square(self):
        """
        Ініціалізація трикутника з прийнятих точокю
        Розрахунок площини за теоремою Герона

        """
        line1 = Line(self.point1, self.point2)
        line2 = Line(self.point2, self.point3)
        line3 = Line(self.point3, self.point1)
        line_A = line1.length
        line_B = line2.length
        line_C = line3.length

        half_perim = (line_A + line_B + line_C) / 2
        return math.sqrt(half_perim * (half_perim - line_A) * (half_perim - line_B) * (half_perim - line_C))


point1 = Point(1, 2)
point2 = Point(4, 5)
point3 = Point(1, 6)


triangl = Triangle(point1, point2, point3)

square = triangl.triangle_square
print(square)









