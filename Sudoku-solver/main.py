

base = [
    [0,2,0,6,0,8,0,0,0],
    [5,8,0,0,0,9,7,0,0],
    [0,0,0,0,4,0,0,0,0],
    [3,7,0,0,0,0,5,0,0],
    [6,0,0,0,0,0,0,0,4],
    [0,0,8,0,0,0,0,1,3],
    [0,0,0,0,2,0,0,0,0],
    [0,0,9,8,0,0,0,3,6],
    [0,0,0,3,0,6,0,9,0]
]

def ans(base):
    find = find_zero(base)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if validation(base, i, (row, col)):
            base[row][col] = i

            if ans(base):
                return True

            base[row][col] = 0

    return False

def validation(base, number, position):
    # Row
    for i in range(len(base[1])):
        if base[position[0]][i] == number and position[1] != i:
            return False

    # Col
    for i in range(len(base)):
        if base[i][position[1]] == number and position[0] != i:
            return False

    # Box
    box_pos_x = position[1] // 3
    box_pos_y = position[0] // 3
    xrange = box_pos_x * 3
    yrange = box_pos_y * 3

    for i in range(yrange, yrange + 3):
        for j in range(xrange, xrange + 3):
            if base[i][j] == number and (i,j) != position:
                return False

    return True

def print_base(base):
    for i in range(len(base)):
        if i % 3 == 0 and i != 0:
            print("=========================")

        for j in range(len(base[1])):
            if j % 3 == 0 and j != 0:
                print(" || ", end="")

            if j == 8:
                print(base[i][j])
            else:
                print(str(base[i][j]) + " ", end="")

# print_base(base)

def find_zero(base):
    for i in range(len(base)):
        for j in range(len(base[1])):
            if base[i][j] == 0:
                # print(i, j)
                return(i, j)
    return None

# find_zero(base)

# print_base(base)
# ans(base)
# print("\n")
# print_base(base)