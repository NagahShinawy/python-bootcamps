class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Road:

    def __init__(self, source: Point, destination: Point):
        self.source = source
        self.destination = destination


pickup = Point(34.5, 67.9)
dropoff = Point(109.54, 45.756)

king_road = Road(source=pickup, destination=dropoff)

TAX = 0.14


def calc_payslip(basic, bonus, refund):
    cross = basic + bonus + refund
    net = cross - (cross * TAX)
    return net


print(calc_payslip(70, 20, 10))