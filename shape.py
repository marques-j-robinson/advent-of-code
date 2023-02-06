from format_data import parse_coord, int_list


class Cube:

    def __init__(self, sides):
        self.sides = int_list(sides.split('x'))
        self.setup_smallest_side()

    def setup_smallest_side(self):
        self.sm_side = self.sides[:]
        self.sm_side.remove(max(self.sm_side))


class Grid:

    def __init__(self, directions, origin='0,0', boundries=None):
        self.directions = directions
        self.coord = origin
        self.seen = []
        self.history = []
        self.x = 0
        self.y = 0
        self.boundries = boundries

    def move(self, d):
        [x, y] = parse_coord(self.coord)
        if d == self.directions["up"]:
            y += 1
        elif d == self.directions["right"]:
            x += 1
        elif d == self.directions["down"]:
            y -= 1
        elif d == self.directions["left"]:
            x -= 1
        coord = f"{x},{y}"
        
        if self.boundries is not None and coord in self.boundries:
            pass
        else:
            self.x = x
            self.y = y
            self.coord = coord

    def move_auto(self, d):
        self.move(d)
        self.add_seen()
        self.add_history()

    def add_seen(self):
        if self.coord not in self.seen:
            self.seen.append(self.coord)

    def add_history(self):
        self.history.append(self.coord)