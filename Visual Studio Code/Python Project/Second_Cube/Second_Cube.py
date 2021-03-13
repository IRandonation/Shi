# -*- coding = utf-8 -*- #
"""
"""
import numpy as np


cube_color = ['b', 'g', 'r', 'o', 'y', 'w']

# Generate a perfect cube, for testing
def generate_test_cube():
    cube = np.zeros((2, 2, 2, 3), dtype='string_')
    cube[0][0][0] = ['b', 'o', 'w']
    cube[0][0][1] = ['b', 'r', 'w']
    cube[0][1][0] = ['g', 'o', 'w']
    cube[0][1][1] = ['g', 'r', 'w']
    cube[1][0][0] = ['b', 'o', 'y']
    cube[1][0][1] = ['b', 'r', 'y']
    cube[1][1][0] = ['g', 'o', 'y']
    cube[1][1][1] = ['g', 'r', 'y']
    return cube


def input_cube():
    cube = np.zeros((2, 2, 2, 3), dtype='string_')

    def hint():
        print('-------Please input the value of 8 cube zone.-------\n')
        print('Rubik Cube are indexed as below:')
        print('      ______________________\n'
              '    /           /           / |\n'
              '   / [0][0][0] / [0][0][1] /  |\n'
              '  ------------------------    |\n'
              ' /          /            / |  |\n'
              '/ [0][1][0]/ [0][1][1]  /  |  |\n'
              ' ______________________    | /|\n'
              '|          |           |   |/ |\n'
              '|[0][1][0] | [0][1][1] |   |  |\n'
              '|          |           |  /   |\n'
              '|          |           | / | <---[1][0][1]\n'
              '----------------------- /  |  |\n'
              '|          |           |   |  |\n'
              '|[1][1][0] | [1][1][1] |   |  |\n'
              '|          |           |   |/\n'
              '|          |           |  /\n'
              '----------------------- /\n')
        print('For each cube, colors are arranged by [x, y, z] order.\n'
              '    ------------\n'
              '  /     z      /|\n'
              ' /           /  |\n'
              ' -----------    |\n'
              '|           | y |\n'
              '|     x     |   |\n'
              '|           |  / \n'
              '|           | / \n'
              ' -----------/ \n')
        print('now please input your cube state.')

    def show_cube(cube):
        print(cube[0, 0, 0, 2])
        print('This is your cube:')
        print('      ______________________\n'
              '    /           /           / |\n'
              '   /     %s   /     %s     /  |\n'
              '  ------------------------    |\n'
              ' /          /            / |%s|\n'
              '/    %s    /     %s     /  |  |\n'
              ' ______________________    | /|\n'
              '|          |           |%s |/ |\n'
              '|    %s    |     %s    |   |  |\n'
              '|          |           |  /   |\n'
              '|          |           | / |%s|\n'
              '----------------------- /  |  |\n'
              '|          |           |%s |  |\n'
              '|    %s    |     %s    |   |  |\n'
              '|          |           |   |/\n'
              '|          |           |  /\n'
              '----------------------- /\n'
              % (str(cube[0, 0, 0, 2]), str(cube[0, 0, 1, 2]), str(cube[0, 0, 1, 1]), str(cube[0, 1, 0, 2]),
                 str(cube[0, 1, 1, 2]), str(cube[0, 1, 1, 1]), str(cube[0, 1, 0, 0]), str(cube[0, 1, 1, 0]),
                 str(cube[1, 0, 1, 1]), str(cube[1, 1, 1, 1]), str(cube[1, 1, 0, 0]), str(cube[1, 1, 1, 0])))

    hint()
    # input state from keyboard, divided with Space, press Enter to change different small cube
    for i in range(2):
        for j in range(2):
            for k in range(2):
                print('The value of cube[%d][%d][%d]:' % (i, j, k))
                value = [temp for temp in input().split()]
                while input_is_error(value):
                    print('current state in not correct, please check your input and try again.')
                    value = [temp for temp in input().split()]
                cube[i, j, k] = value
    show_cube(cube)

    return cube

# Detect whether the color of input is correct
def input_is_error(items):
    if len(items) < 3:
        return True
    for item in items:
        if item in cube_color:
            return False
        else:
            return True


def swap(item, axis):
    if axis == 'x':
        temp = item[2]
        item[2] = item[1]
        item[1] = temp
    elif axis == 'y':
        temp = item[2]
        item[2] = item[0]
        item[0] = temp
    elif axis == 'z':
        temp = item[1]
        item[1] = item[0]
        item[0] = temp
    else:
        print('ERROR: SWAP')
        exit(-1)

    return item


def rotate(cube, axis):
    if axis == 'x':
        temp = cube[0, 1, 1].copy()
        cube[0, 1, 1] = swap(cube[0, 1, 0], 'x')
        cube[0, 1, 0] = swap(cube[1, 1, 0], 'x')
        cube[1, 1, 0] = swap(cube[1, 1, 1], 'x')
        cube[1, 1, 1] = swap(temp, 'x')
    elif axis == 'y':
        temp = cube[0, 1, 1].copy()
        cube[0, 1, 1] = swap(cube[1, 1, 1], 'y')
        cube[1, 1, 1] = swap(cube[1, 0, 1], 'y')
        cube[1, 0, 1] = swap(cube[0, 0, 1], 'y')
        cube[0, 0, 1] = swap(temp, 'y')
    elif axis == 'z':
        temp = cube[0, 1, 1].copy()
        cube[0, 1, 1] = swap(cube[0, 0, 1], 'z')
        cube[0, 0, 1] = swap(cube[0, 0, 0], 'z')
        cube[0, 0, 0] = swap(cube[0, 1, 0], 'z')
        cube[0, 1, 0] = swap(temp, 'z')
    elif axis == ' ':
        pass
    else:
        print('ERROR:ROTATE')
        exit(-1)

    return cube


def cube_is_perfect(cube):
    complete_facets = 0
    # check the top side
    if cube[0, 0, 0, 2] == cube[0, 0, 1, 2] == cube[0, 1, 0, 2] == cube[0, 1, 1, 2]:
        complete_facets += 1
    # check the front side
    if cube[0, 1, 0, 0] == cube[0, 1, 1, 0] == cube[1, 1, 0, 0] == cube[1, 1, 1, 0]:
        complete_facets += 1
    # check the right side
    if cube[0, 1, 1, 1] == cube[0, 0, 1, 1] == cube[1, 1, 1, 1] == cube[1, 0, 1, 1]:
        complete_facets += 1
    # check the down side
    if cube[1, 0, 0, 2] == cube[1, 0, 1, 2] == cube[1, 1, 0, 2] == cube[1, 1, 1, 2]:
        complete_facets += 1
    # check the back side
    if cube[0, 0, 0, 0] == cube[0, 0, 1, 0] == cube[1, 0, 0, 0] == cube[0, 0, 1, 0]:
        complete_facets += 1
    # check the left side
    if cube[0, 0, 0, 1] == cube[0, 1, 0, 1] == cube[1, 0, 0, 1] == cube[1, 1, 0, 1]:
        complete_facets += 1

    if complete_facets == 6:
        return True
    else:
        return False


def cube_is_the_same(cube, target_cube):
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if cube[i][j][k] == target_cube[i][j][k]:
                    continue
                else:
                    return False
    return True


def restore_convert(cube, target_cube):
    steps_records = []
    number_of_god = 11
    depth = 0

    def reverse(cube, operation):
        return rotate(rotate(rotate(cube, operation), operation), operation)

    def pre_traverse(cube, operation, depth):
        global steps
        global mode

        depth += 1

        if operation == ' ':
            pass
        else:
            cube = rotate(cube, operation)

        if depth <= number_of_god:
            steps_records.append(operation)
        # print(depth)
        # print(steps_records)

        if mode == '0':
            if cube_is_perfect(cube):
                print('The cube is in perfect state with in ' + str(steps) + ' steps,')
                print('The step is:' + str(steps_records[1:]))
                exit(0)
        elif mode == '1':
            if cube_is_the_same(cube, target_cube):
                print('The cube is in target state with in ' + str(steps) + ' steps,')
                print('The step is:' + str(steps_records[1:]))
                exit(0)
        else:
            print('ERROR:MODE')
            exit(0)

        if depth >= number_of_god:
            depth -= 1
            cube = reverse(cube, operation)
            steps_records.pop()
            return

        steps += 1

        if steps > 88572:
            print('The cube can not be restored, please check your input')

        pre_traverse(cube, 'x', depth)
        pre_traverse(cube, 'y', depth)
        pre_traverse(cube, 'z', depth)
        cube = reverse(cube, operation)
        steps_records.pop()

    pre_traverse(cube, ' ', depth)
    print(steps)


steps = 0

mode = '0'
mode = input('Select mode: [0]Restore   [1]Convert to target state')
if mode == '0':
    cube = input_cube()
    restore_convert(cube.copy(), None)
elif mode == '1':
    current_cube = input_cube()
    print('Now Please input your target cube.\n')
    target_cube = input_cube()
    restore_convert(current_cube.copy(), target_cube.copy())
else:
    print('ERROR:MODE SELECT')
    exit(-1)


