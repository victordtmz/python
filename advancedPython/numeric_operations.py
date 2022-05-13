

from re import X


class Points():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'<Point x:{self.x}, y:{self.y}>'

    # TODO: implement addition
    def __add__(self, other):
        return Points(self.x + other.x, self.y + other.y)

    # TODO: implement subtraction
    def __sub__(self, other):
        return Points(self.x - other.x, self.y - other.y)

    # TODO: implement addition
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

def main():
    #declare pints
    p1 = Points(10, 20)
    p2 = Points(30, 30)

    print(p1, p2)

    # TODO: add two points
    p3 = p1 + p2
    print(p3)


    # TODO: subtract two points
    p4 = p2 - p1
    print(p4)

    # TODO: perform in-place addition
    p1 += p2
    print(p1)

if __name__=='__main__':
    main()

