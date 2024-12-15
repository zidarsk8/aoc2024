from data.day12 import test3, test1, test2, test4, test5, text


def to_arr(text):
    return list(map(list, text.splitlines()))


moves = [
    (-1,0),
    (1,0),
    (0,-1),
    (0,1),
]

def print_arr(arr):
    print("\n".join("".join(line) for line in arr))

def get_next_region(arr):
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if len(arr[y][x]) == 1:
                return (x,y)
    return None


def join_boundary_boxes(boxes):
    for x,y, bx, by in boxes:
        pass
    return boxes


def handle_region(arr, start_x, start_y):
    width = len(arr[0])
    height = len(arr)
    region = arr[start_y][start_x]
    dead = region+"."
    new_positions = {(start_x,start_y)}
    visited_positions = set()
    boundary_boxes = set()
    while new_positions:
        x,y = new_positions.pop()
        arr[y][x] = dead
        visited_positions.add((x,y))
        for dx, dy in moves:
            if -1 < y+dy < height and -1 < x+dx < width:
                if arr[y+dy][x+dx] == region:
                    new_positions.add((x+dx,y+dy))
                elif arr[y+dy][x+dx] != dead:
                    boundary_boxes.add((x,y, x+dx,y+dy))
            else:
                boundary_boxes.add((x,y, x+dx,y+dy))

    # join boundary groups
    boundary_groups = {b:i for i,b in enumerate(sorted(boundary_boxes))}
    for box, group in boundary_groups.items():
        for dx, dy in moves:
            x1, y1, x2, y2 = box
            box2 = (x1+dx, y1+dy, x2+dx, y2+dy)
            if box2 in boundary_groups:
                prev_group = boundary_groups[box2]
                new_group = boundary_groups[box]
                for b, g in boundary_groups.items():
                    if g == prev_group:
                        boundary_groups[b] = new_group
    
    return len(visited_positions), len(set(boundary_groups.values())) # len(boundary_boxes) <- part 1

def handle_regions(arr):
    result = 0 
    while start := get_next_region(arr):
        size, boundary = handle_region(arr, start[0], start[1])
        result += size*boundary
        print(arr[start[1]][start[0]], size, boundary)
    print(result)



# handle_region(to_arr(test2),0,0)


handle_regions(to_arr(test1))
print("----------")
handle_regions(to_arr(test2))
print("----------")
handle_regions(to_arr(test3))
print("----------")
handle_regions(to_arr(test4))
print("----------")
handle_regions(to_arr(test5))
print("----------")

handle_regions(to_arr(text))
print("----------")






(0, 0, -1, 0)
(0, 0, 0, -1)
(1, 0, 1, 1)
(3, 0, 3, 1)
(0, 1, 1, 1)
(4, 0, 5, 0)
(1, 2, 1, 1)
(1, 2, 1, 3)
(2, 1, 1, 1)
(2, 1, 3, 1)
(3, 2, 3, 1)
(3, 2, 3, 3)
(0, 3, 1, 3)
(4, 1, 3, 1)
(2, 3, 1, 3)
(2, 3, 3, 3)
(2, 4, 2, 5)
(0, 4, 0, 5)
(3, 4, 3, 3)
(4, 3, 3, 3)
(1, 4, 1, 3)
