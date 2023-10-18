def battleship(grid: 'list[list[int]]', line: int, column: int) -> bool:
    if grid[line][column] == 1:
        return True
    else:
        return False
