def check_cell(matrix, row_to_check, column_to_check):
    try:
        return matrix[row_to_check][column_to_check]
    except IndexError:
        return 0

import curses  # Get the module
stdscr = curses.initscr()  # initialise it
stdscr.clear()  # Clear the screen

# Creates a list containing 12 lists, each of 12 items, all set to 0
w, h = 12, 12;
matrix = [[0 for x in range(w)] for y in range(h)] 

#     0 1 2 3 4 5 6 7 8 9 0 1
# 0 # X X . . . . . . . . . . 
# 1 # X X X . . . . . . . . . - (1,1) dies
# 2 # . . . . . . . . . . . .
# 3 # . . . . . . X X . . . . - (6,3) lives
# 4 # . . . . . . X . . . . .
# 5 # . . . . . . . . X . . .
# 6 # . . . . . . . X X X . . - (8,6) dies
# 7 # . . . . . . . . X . . .
# 8 # . . . . . . . . . . . .
# 9 # . . . . . . . . . . X .
# 0 # . . . . . . . . . X . . - (0,0) resurrects
# 1 # . . . . . . . . . . X .
#     0 1 2 3 4 5 6 7 8 9 0 1

matrix[0][0] = 1
matrix[0][1] = 1
matrix[1][0] = 1
matrix[1][1] = 1
matrix[1][2] = 1

matrix[3][6] = 1
matrix[3][7] = 1
matrix[4][6] = 1

matrix[5][8] = 1
matrix[6][7] = 1
matrix[6][8] = 1
matrix[6][9] = 1
matrix[7][8] = 1

matrix[9][10] = 1
matrix[10][9] = 1
matrix[11][10] = 1
#

for row_number in range(0,len(matrix)):
    for column_number in range(0,len(matrix)):
        my_value = matrix[row_number][column_number]
        count_of_neighbors = 0
        print "Now at %s,%s" % (row_number,column_number)

        # X X X
        # X O X
        # X X X
        count_of_neighbors = count_of_neighbors + check_cell(matrix,row_number-1,column_number-1)
        count_of_neighbors = count_of_neighbors + check_cell(matrix,row_number-1,column_number)
        count_of_neighbors = count_of_neighbors + check_cell(matrix,row_number-1,column_number+1)

        count_of_neighbors = count_of_neighbors + check_cell(matrix,row_number,column_number-1)
        count_of_neighbors = count_of_neighbors + check_cell(matrix,row_number,column_number+1)

        count_of_neighbors = count_of_neighbors + check_cell(matrix,row_number+1,column_number-1)
        count_of_neighbors = count_of_neighbors + check_cell(matrix,row_number+1,column_number)
        count_of_neighbors = count_of_neighbors + check_cell(matrix,row_number+1,column_number+1)
        #



for i in range(0,10):
    # live cells with <2 live neighbours dies
# live cells with 2-3 live neighbours lives on to next generation.
# live cell >3 live neighbours dies
# dead cell 3 live neighbours becomes a live cell

    if my_value:
        if count_of_neighbors < 2 and count_of_neighbors > 3:
            my_value = 0
            print "Dead!"
    else:
        if count_of_neighbors == 3:
            my_value = 1
            print "Zombie!"

    matrix[row_number][column_number] = my_value

    print "Output:"
    for row in matrix:
        output = []
        for cell in row:
            if cell:
                output.append('-')
            else:
                output.append(' ')
        print ' '.join(output)
#    stdscr.clear()  # Clear the screen