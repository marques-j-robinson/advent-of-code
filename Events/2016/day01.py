from main import CacheLayer, Grid


directions = ["N", "S", "W", "E"]
G = Grid(directions)
pivot = {
    "NR": "E",
    "NL": "W",
    "SR": "W",
    "SL": "E",
    "ER": "S",
    "EL": "N",
    "WR": "N",
    "WL": "S"
}


class S(CacheLayer):

    def is_intersection(self, G):
        G.save_coord()
        return self.p2 == 0 and G.coord in G.seen
    
    def check_intersection(self, G):
        if self.is_intersection(G):
            self.p2 = G.manhattan_distance()

    def solve(self):
        self.split_by_comma()
        self.list_of_tuples()
        direction = directions[0]
        for turn, steps in self.puzzle_input:
            direction = pivot[f'{direction}{turn}']
            while steps > 0:
                G.move(direction)
                self.check_intersection(G)
                G.add_seen()
                steps -= 1
        self.p1 = G.manhattan_distance()