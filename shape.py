from format_data import parse_coord, int_list


class Cube:

    def __init__(self, sides):
        self.sides = int_list(sides.split('x'))
        self.setup_smallest_side()

    def setup_smallest_side(self):
        self.sm_side = self.sides[:]
        self.sm_side.remove(max(self.sm_side))


class Grid:

    def __init__(self, directions, origin='0,0', boundry=None):
        self.directions = directions
        self.boundry = boundry
        self.seen = []
        self.coord = origin
        [x, y] = parse_coord(self.coord)
        self.x = x
        self.y = y

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
        
        if self.boundry is not None and coord in self.boundry:
            pass
        else:
            self.x = x
            self.y = y
            self.coord = coord

    def move_auto(self, d):
        self.move(d)
        self.add_seen()

    def add_seen(self):
        if self.coord not in self.seen:
            self.seen.append(self.coord)
