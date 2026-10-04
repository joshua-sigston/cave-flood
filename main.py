class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

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

    def place_rocks(self, row, col):
        # places a rock at the coordinates in the grid
        self.grid[row][col] = Rock(row, col)

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


def game():

    b = Board(5, 5)
    b.print_board()

game()