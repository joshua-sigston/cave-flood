import random

DIRECTIONS = [
    (-1, 0),
    (0, -1), (0, 1),
    (1, 0),
]

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.rock_count = 0

    def __repr__(self):
        return f"Cell({self.row}, {self.col})"

class Tunnel(Cell):
    def __init__(self, row, col):
        super().__init__(row, col)
        self.is_wet = False

    def toggle(self):
        self.is_wet = not self.is_wet

    def display(self):
        if self.is_wet:
            return "~"
        else:
            return "."
        
class Rock(Cell):
    def __init__(self, row , col):
        super().__init__(row, col)

    def display(self):
        return "#"

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.create_grid()
        self.num_of_rocks = 0


    # create grid
    def create_grid(self):
        # empty list for grid
        grid = []
        # create row
        for r in range(self.rows):
            row = []
            # add item at the col in the row
            for c in range(self.cols):
                row.append(Tunnel(r, c))
            grid.append(row)

        self.grid = grid

    def place_rocks(self):
        r = self.rows
        c = self.cols
        #  create a maximum number of rocks to place on the grid
        max_rocks = (r * c * 40) // 100
        number_of_rocks_to_place = random.randint(0, max_rocks)
        # list of every (row, col) coordinate on the board
        spots = [(row, col) for row in range(r) for col in range(c)]
        # print(spots)
        # pick that many unique spots at random so rocks do not overlap
        for row, col in random.sample(spots, number_of_rocks_to_place):
        # places a rock at the coordinates in the grid
            self.grid[row][col] = Rock(row, col)
        return number_of_rocks_to_place

    def print_board(self):
        print(" ", end=" ")
        # prints col numbers followed by space
        print(" ".join(str(i) for i in range(self.cols)))
        for r in range(self.rows):
            # prints row number followed by space
            print(r, end=" ")
            for c in range(self.cols):
                # displayes rock or tunnel
                print(self.grid[r][c].display(), end=" ")
            print()
    
    def in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
    
    def toggle(self, row, col):
        if not self.in_bounds(row, col):
            print("Those numbers are off the board.")
            return
        
        # calls toggle for tunnel at location
        self.grid[row][col].toggle()
        self.print_board()

    def get_neighbors(self, row, col):
        neighbors = []
        # for dr, dc means (dr, dc)
        for dr, dc in DIRECTIONS:
            # adds dr to row
            nr = row + dr
            # add dc to col
            nc = col + dc
            if self.in_bounds(nr, nc):
                neighbors.append((nr, nc))
        # print(neighbors)
        return neighbors

    def count_adjacent_rocks(self, row, col):
        n = self.get_neighbors(row, col)
        for row, col in n:
            cell = self.grid[row][col]
            if isinstance(cell, Rock):
                self.num_of_rocks += 1
        return self.num_of_rocks


def game():

    b = Board(9, 9)
    b.place_rocks()
    # print("num of adjacent rocks", b.count_adjacent_rocks(2, 2))
    print("num of rocks on the board", b.place_rocks())
    b.print_board()
    

game()