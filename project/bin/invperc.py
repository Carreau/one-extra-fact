#!/usr/bin/env python

import sys
import getopt
import random


RANGE_MIN = 1
SIZE_MIN = 3
SETTINGS = {
    'range'   : RANGE_MIN,
    'seed'    : 12345,
    'size'    : SIZE_MIN,
    'verbose' : False
}
FILLED = -1


def main(args):
    settings = parse_args(args)
    grid, candidates = make_world(settings)
    while update(grid, candidates):
        if settings['verbose']:
            display(grid)
    display(grid)


def parse_args(args):
    settings = SETTINGS.copy()
    options, extras = getopt.getopt(args, 'r:s:z:v')
    assert not extras, \
        'Trailing command-line arguments "{}" not understood'.format(' '.join(extras))
    for (opt, arg) in options:
        if opt == '-r':
            settings['range'] = int(arg)
            assert settings['range'] >= RANGE_MIN, \
                'Range {} out of bounds (must be at least {})'.format(settings['range'], RANGE_MIN)
        elif opt == '-s':
            settings['seed'] = int(arg)
            assert settings['seed'] > 0, \
                'Seed {} out of bounds (must be positive)'.format(settings['seed'])
        elif opt == '-z':
            settings['size'] = int(arg)
            assert settings['size'] >= SIZE_MIN, \
                'Size {} out of bounds (must be at least {})'.format(settings['size'], SIZE_MIN)
            assert settings['size'] % 2 == 1, \
                'Invalid size {} (must be odd)'.format(settings['size'])
        elif opt == '-v':
            settings['verbose'] = True
    return settings


def make_world(settings):
    random.seed(settings['seed'])
    size = settings['size']
    upper = settings['range']

    grid = []
    for i in range(size):
        grid.append([random.randrange(upper) for j in range(size)])
    mid = int((size - 1) / 2)
    grid[mid][mid] = FILLED

    candidates = [set() for i in range(upper)]
    add_all_neighbors(grid, candidates, (mid, mid))

    return grid, candidates


def update(grid, candidates):
    point = select_point(grid, candidates)
    grid[point[0]][point[1]] = FILLED
    add_all_neighbors(grid, candidates, point)
    return not on_edge(grid, point)


def select_point(grid, candidates):
    for (i, c) in enumerate(candidates):
        if c:
            break
    assert c, \
        'No candidates found in {}'.format(str(candidates))
    point  = random.sample(c, 1)[0]
    c.remove(point)
    return point


def on_edge(grid, point):
    size = len(grid)
    x, y = point
    return (x == 0) or (x+1 == size) or (y == 0) or (y+1 == size)


def add_all_neighbors(grid, candidates, point):
    size = len(grid)
    x, y = point
    if x   > 0:    add_neighbor(grid, candidates, (x-1, y))
    if x+1 < size: add_neighbor(grid, candidates, (x+1, y))
    if y   > 0:    add_neighbor(grid, candidates, (x, y-1))
    if y+1 < size: add_neighbor(grid, candidates, (x, y+1))


def add_neighbor(grid, candidates, point):
    x, y = point
    val = grid[x][y]
    if val != FILLED:
        candidates[val].add(point)


def display(grid):
    size = len(grid)
    ruler = '+' + '-' * size + '+'
    print(ruler)
    for row in grid:
        chars = []
        for cell in row:
            chars.append('X' if cell == FILLED else ' ')
        print('|' + ''.join(chars) + '|')
    print(ruler)


if __name__ == '__main__':
    main(sys.argv[1:])
