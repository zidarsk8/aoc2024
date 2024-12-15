from data.day15 import test1, test2, text, test3, test4
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Grid = namedtuple("Grid", ["w", "h"])



def parse_data(data:str):
    grid, moves = data.split("\n\n")
    grid = [list(line) for line in grid.splitlines()]
    grid_size = Grid(len(grid[0]), len(grid))
    robot = Point(0,0)
    for x in range(grid_size.w):
        for y in range(grid_size.h):
            if grid[y][x] == "@":
                robot = Point(x, y)

    moves = list(moves.replace("\n", ""))
    return grid_size, robot, grid, moves


def apply_move(grid: list[list[str]], robot:Point, move:str):
    vectors = {
        ">": Point(1,0),
        "<": Point(-1,0),
        "v": Point(0,1),
        "^": Point(0,-1),
    }
    vector = vectors[move]

    point = robot
    current_char = "."

    new_grid = list(map(list, grid))
    
    move_blocks = [{
        "current_char": ".",
        "point": point,
    }]
    while current_char != "#":
        for move_block in list(move_blocks):
            next_char = new_grid[point.y][point.x]
            if move in "^v" and next_char == "[":
                move_blocks.append({
                    "current_char": ".",
                    "point": Point(point.x+1, point.y)
                })
            elif move in "^v" and next_char == "]":
                move_blocks.append({
                    "current_char": ".",
                    "point": Point(point.x-1, point.y)
                })

        for move_block in list(move_blocks):
            breakpoint()
            print()
            print("\n".join("".join(line) for line in new_grid))
            point = move_block["point"]
            next_char = new_grid[point.y][point.x]

            new_grid[point.y][point.x] = current_char
            point = Point(point.x+vector.x, point.y+vector.y)
            current_char = next_char

            move_block["point"] = point
            move_block["current_char"] = current_char
            
            print()
            print("\n".join("".join(line) for line in new_grid))
            print()

        if all(mb["current_char"] == "." for mb in move_blocks):
            return new_grid, Point(robot.x+vector.x, robot.y+vector.y)
    return grid, robot

def apply_moves(grid:list[list[str]], robot:Point, moves:list[str]):
    for move in moves:
        grid, robot = apply_move(grid, robot, move)
    return grid, robot


def gps(grid: list[list[str]], grid_size:Grid):
    s = 0
    for x in range(grid_size.w):
        for y in range(grid_size.h):
            if grid[y][x] == "O":
                s += y*100 + x
    return s
    

def expand_data(data:str):
    return data.replace("#", "##").replace(".","..").replace("O","[]").replace("@","@.")

def main(data:str):
    data = expand_data(data)

    grid_size, robot, grid, moves = parse_data(data)
    print(grid_size, robot)
    print("----------")
    print("\n".join("".join(line) for line in grid))
    print("----------")
    # grid, robot = apply_moves(grid, robot, moves)
    # grid, robot = apply_move(grid, robot, '<')
    # grid, robot = apply_move(grid, robot, 'v')
    # grid, robot = apply_move(grid, robot, 'v')
    # grid, robot = apply_move(grid, robot, '<')
    # grid, robot = apply_move(grid, robot, '<')
    grid, robot = apply_move(grid, robot, '^')

    print("----------")
    print("\n".join("".join(line) for line in grid))
    print("----------")
    result = gps(grid, grid_size)
    print(f"GPS: {result}")


if __name__ == "__main__":
    main(test4)
    # main(test2)
    # main(text)