from random import randint
import turtle


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def falls_in_rectangle(self, rectangle_area):
        return rectangle_area.point1.x < self.__x < rectangle_area.point2.x and \
               rectangle_area.point1.y < self.__y < rectangle_area.point2.y


class Rectangle:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    @property
    def point1(self):
        return self.__point1

    @property
    def point2(self):
        return self.__point2

    def area(self):
        return (self.__point2.x - self.__point1.x) * \
               (self.__point2.y - self.__point1.y)


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):
    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)

        canvas.pendown()
        canvas.dot(size, color)

        turtle.done()


rectangle = GuiRectangle(
    Point(randint(0, 200), randint(0, 200)),
    Point(randint(10, 200), randint(10, 200))
)

print("Rectangle Coordinates:",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

print("Your point was inside rectangle: ",
      user_point.falls_in_rectangle(rectangle))

print("Your area was off by: ",
      rectangle.area() - user_area)

myturtle = turtle.Turtle()
rectangle.draw(myturtle)
user_point.draw(myturtle)