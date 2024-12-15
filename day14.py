from data.day14 import text, test
# Python code to demonstrate namedtuple()
from collections import namedtuple, defaultdict

# Declaring namedtuple()
Field = namedtuple('Field', ['w', 'h'])
Robot = namedtuple('Robot', ['pos', 'vel'])
Point = namedtuple("Point", ["x", "y"])

seconds = 1000
field = Field(101, 103)
test_field = Field(11, 7)

def parse_robots(text:str):
    robots = []
    for line in text.splitlines():
        pos,vel = line.split()

        robots.append(
            Robot(
                Point(*list(map(int, pos.split("=")[1].split(",")))),
                Point(*list(map(int, vel.split("=")[1].split(",")))),
            )
        )
    return robots

def print_field(field:Field, robots:dict[str, tuple]):
    robot_positions = defaultdict(int)
    for robot in robots:
        robot_positions[robot.pos] += 1

    for y in range(field.h):
        for x in range(field.w):
            print(robot_positions.get((x,y), "."),end="")
        print()
    print()

def move_robots(field:Field, robots: list[Robot[Point]]):
    new_robots = []
    for robot in robots:
        new_robots.append(
            Robot(
                Point(((robot.pos.x + robot.vel.x) % field.w), ((robot.pos.y + robot.vel.y) % field.h)),
                robot.vel,
            )
        )
    return new_robots

def sum_quadrants(field:Field, robots: list[Robot]):
    robot_positions = defaultdict(int)
    for robot in robots:
        robot_positions[robot.pos] += 1

    quadrants = defaultdict(int)

    yq = 0
    for y in range(field.h):
        if ((field.h-1)/2) == y:
            yq +=1
            print()
            continue
        xq = 0
        for x in range(field.w):
            if ((field.w-1) /2) == x:
                print(" ",end="")
                xq += 1
                continue
            print(robot_positions.get((x,y), "."),end="")
            quadrants[(xq, yq)] += robot_positions[(x,y)]
        print()

    return quadrants[(0,0)]*quadrants[(0,1)]*quadrants[(1,0)]*quadrants[(1,1)]

robots = parse_robots(text)
print_field(field, robots)

def move_seconds(field, robots, seconds):
    for i in range(seconds):
        robot_positions = defaultdict(int)
        for robot in robots:
            robot_positions[robot.pos] += 1
            
                    
        print("-----")
        print(i)
        print_field(field, robots)
        robots = move_robots(field, robots)
    
move_seconds(field, robots, 10000)

print_field(field, robots)


# print(sum_quadrants(field, robots))
