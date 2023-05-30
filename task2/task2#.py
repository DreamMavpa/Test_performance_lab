import argparse
import os


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return "<Position:{},{}>".format(str(self.x), str(self.y))

    def __repr__(self):
        return "<Position:{},{}>".format(str(self.x), str(self.y))


class CirclePosition:
    def __init__(self, center: Position, radius: int):
        self.center = center
        self.radius = radius

    def point_position(self, point: Position) -> int:
        equation = (point.x - self.center.x)**2 + (point.y - self.center.y)**2 - self.radius**2
        if equation == 0:
            result = 0
        elif equation < 0:
            result = 1
        elif equation > 0:
            result = 2
        return result

    def __str__(self):
        return "<CirclePosition: center: {}, radius: {}>".format(self.center, str(self.radius))

    def __repr__(self):
        return "<CirclePosition: center: {}, radius: {}>".format(self.center, str(self.radius))


def run_program():
    parser = argparse.ArgumentParser()
    parser.add_argument('circle_file', type=str, help='file containing circle center coordinates and radius')
    parser.add_argument('points_file', type=str, help='file containing a list of points to be checked')
    args = parser.parse_args()


    if not all(os.path.exists(file) for file in (args.circle_file, args.points_file)):
        raise Exception("File not found")


    with open(args.circle_file, 'r') as circle_file:
        center_coords = list(map(int, next(circle_file).split()))
        radius = int(next(circle_file))
        circle = CirclePosition(Position(*center_coords), radius)

 
    with open(args.points_file, 'r') as points_file:
        points = [list(map(int, line.split())) for line in points_file]
        for point in points:
            p = Position(*point)
            print(circle.point_position(p))

if __name__ == "__main__":
    run_program()
