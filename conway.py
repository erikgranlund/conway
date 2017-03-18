import subprocess
import logging

def check_cell(matrix, row_to_check, column_to_check):
    '''
    Safely returns the value of a cell in the matrix passed.

    Returns 0 for cells outside of the matrix.
    '''
    try:
        return matrix[row_to_check][column_to_check]
    except IndexError:
        return 0

def clear_screen():
    '''
    Cler the terminal screen to display the next run of the simulation
    '''
    return subprocess.call('clear', shell=True)

def simulate(matrix):
    '''
    Run the rules of the conway simulation on each cell of the provided matrix.

    Returns the result of this simulation.
    '''

    for row_number in range(0, len(matrix)):
        for column_number in range(0, len(matrix)):
            my_value = matrix[row_number][column_number]
            neighbors = 0
            #logging.debug("Now at %d,%d", (row_number, column_number))

            # X X X
            # X O X
            # X X X
            neighbors = neighbors + check_cell(matrix, row_number-1, column_number-1)
            neighbors = neighbors + check_cell(matrix, row_number-1, column_number)
            neighbors = neighbors + check_cell(matrix, row_number-1, column_number+1)

            neighbors = neighbors + check_cell(matrix, row_number, column_number-1)
            neighbors = neighbors + check_cell(matrix, row_number, column_number+1)

            neighbors = neighbors + check_cell(matrix, row_number+1, column_number-1)
            neighbors = neighbors + check_cell(matrix, row_number+1, column_number)
            neighbors = neighbors + check_cell(matrix, row_number+1, column_number+1)
            #

            # live cells with <2 live neighbours dies
            # live cells with 2-3 live neighbours lives on to next generation.
            # live cell >3 live neighbours dies
            # dead cell 3 live neighbours becomes a live cell

            if my_value:
                if neighbors < 2 or neighbors > 3:
                    my_value = 0
                    logging.debug("Dead!")
            else:
                if neighbors == 3:
                    my_value = 1
                    logging.debug("Zombie!")

            matrix[row_number][column_number] = my_value

    return matrix

class ConwayPlanet(object):
    '''
    Contains the whole "planet" that each "organisim" on the simulation lives.
    '''
    def __init__(self):
        pass

    def meh(self):
        print "meh"

def init():
    '''
    Load an initial configuration of a matrix.

    Returns an array of arrrays.
    '''

    # Populate a 12x12 matrix with 0's
    size = 20
    matrix = [[0 for x in range(size)] for y in range(size)]

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

    return matrix


def run(matrix): 
    '''
    Run the simulation.
    '''
    count = 0
    #for i in range(0,100):
    while True:
        clear_screen()
        matrix = simulate(matrix)

    #    print "Output:"
        print "Simulation #" + str(count)
        for row in matrix:
            output = []
            for cell in row:
                if cell:
                    output.append('-')
                else:
                    output.append(' ')
            print 'R: ' + ' '.join(output)

        count = count + 1

#print init()

run(init())
