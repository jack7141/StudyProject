

class Boundaries:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __contains__(self,item):
        x, y = item
        return 0 <= x < self.x and 0 <= y < self.y

class Grid:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.limits = Boundaries(width,height)

    def __contains__(self,item):
        return item in self.limits


def mark_coordinates(grid, coordinates):
    if coordinates in grid:
        grid[coordinates] = "MARKED"


if __name__ == "__main__":
    # Create a grid of size 5x5
    grid = Grid(5, 5)

    mark_coordinates(grid, (2, 3))  # Within bounds