# Part 1
from collections import defaultdict

def distance(a, b):
    return abs(a - b)

def manhattan_distance(p1, p2):
    return distance(p1[0], p2[0]) + distance(p1[1], p2[1])

def find_closest_point(x, y):
    points = []
    for co_ord in co_ords:
        points.append((manhattan_distance((x, y), co_ord), co_ord))
    points.sort()
    if points[0][0] == points[1][0]:
        return None
    else:
        return points[0][1]

with open('input.txt') as f:
    co_ords = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in f]

# Work out the boundaries
minx, miny, maxx, maxy = co_ords[0][0], co_ords[0][1] , co_ords[0][0], co_ords[0][1]
for co_ord in co_ords:
    minx = co_ord[0] if co_ord[0] < minx else minx
    miny = co_ord[1] if co_ord[1] < miny else miny
    maxx = co_ord[0] if co_ord[0] > maxx else maxx
    maxy = co_ord[1] if co_ord[1] > maxy else maxy

# Draw the blank grid
grid = [ [None for x in range(maxx - minx + 1)] for y in range(maxy - miny + 1) ]

# Populate the grid with all the closest points
for y, row in enumerate(grid):
    actual_y = y + miny
    for x, column in enumerate(row):
        actual_x = x + minx

        # Find the closest point
        if (actual_x, actual_y) in co_ords:
            grid[y][x] = (actual_x,actual_y)
        else:
            grid[y][x] = find_closest_point(actual_x, actual_y)

# We only care about the areas that aren't on boundaries
possible_areas = set()
for row in grid:
    for column in row:
        if column is not None:
            if (minx != column[0]) and (miny != column[1]) and (maxx != column[0]) and (maxy != column[1]):
                possible_areas.add(column)


# Count up everything on the grid
results = defaultdict(int)
for possibility in possible_areas:
    for row in grid:
        for column in row:
            if possibility == column:
                results[possibility] += 1

result = sorted(results.items(), key=lambda x: x[1], reverse=True)[0]
print(result[1])