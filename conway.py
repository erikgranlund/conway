import subprocess

class Planet(object):
    '''
    Contains the whole "planet" that each "organisim" on the simulation lives.
    '''
    def get_times_simulated(self):
        '''
        Return the number of simulations the planet has been through
        '''
        return self.times_simulated

    def __init__(self):
        self.times_simulated = 0

        size = 12
        self.matrix = [[Organism() for x in range(size)] for y in range(size)]

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

        self.matrix[0][0].set_alive(True)
        self.matrix[0][1].set_alive(True)
        self.matrix[1][0].set_alive(True)
        self.matrix[1][1].set_alive(True)
        self.matrix[1][2].set_alive(True)

        self.matrix[3][6].set_alive(True)
        self.matrix[3][7].set_alive(True)
        self.matrix[4][6].set_alive(True)

        self.matrix[5][8].set_alive(True)
        self.matrix[6][7].set_alive(True)
        self.matrix[6][8].set_alive(True)
        self.matrix[6][9].set_alive(True)
        self.matrix[7][8].set_alive(True)

        self.matrix[9][10].set_alive(True)
        self.matrix[10][9].set_alive(True)
        self.matrix[11][10].set_alive(True)

    def __str__(self):
        output = "Simulation #%d\n" % (self.times_simulated)
        for row in self.matrix:
            row_str = []
            for cell in row:
                row_str.append(str(cell))
            output += 'R: ' + ' '.join(row_str) + '\n'
        return output

    def simulate(self):
        '''
        Run one "round" of simulation according to the rules of the planet
        '''
        self.times_simulated += 1

        for row_number in range(0, len(self.matrix)):
            for column_number in range(0, len(self.matrix)):
                neighbors = 0

                # X X X
                # X O X
                # X X X
                neighbors += int(self.check_cell(row_number-1, column_number-1))
                neighbors += int(self.check_cell(row_number-1, column_number))
                neighbors += int(self.check_cell(row_number-1, column_number+1))

                neighbors += int(self.check_cell(row_number, column_number-1))
                neighbors += int(self.check_cell(row_number, column_number+1))

                neighbors += int(self.check_cell(row_number+1, column_number-1))
                neighbors += int(self.check_cell(row_number+1, column_number))
                neighbors += int(self.check_cell(row_number+1, column_number+1))
                #

                # live cells with <2 live neighbours dies
                # live cells with 2-3 live neighbours lives on to next generation.
                # live cell >3 live neighbours dies
                # dead cell 3 live neighbours becomes a live cell
                if self.matrix[row_number][column_number].is_alive():
                    if neighbors < 2 or neighbors > 3:
                        #print "Killed at %d %d" % (row_number, column_number)
                        self.matrix[row_number][column_number].kill()
                else:
                    if neighbors == 3:
                        self.matrix[row_number][column_number].resurrect()

    def get_organism(self, row_to_check, column_to_check):
        '''
        Safely returns the organism from a cell on the planet

        Returns None for cells outside of the matrix.
        '''
        try:
            return self.matrix[row_to_check][column_to_check]  
        except IndexError:
            return None      

    def check_cell(self, row_to_check, column_to_check):
        '''
        Safely returns the value of a cell on the planet

        Returns False for cells outside of the matrix.
        '''
        cell = self.get_organism(row_to_check,column_to_check)

        if cell:
            return cell.is_alive()
        else:
            return False


class Organism(object):
    '''
    An individual within the Conway simulation, lives on a ConwayPlanet
    '''
    def __init__(self):
        self.alive = False
        self.times_killed = 0
        self.times_resurrected = 0

    def is_alive(self):
        '''
        Determine whether the organism is dead or alive.
        '''
        return self.alive

    def set_alive(self, alive):
        '''
        Set whether the organism is dead or alive.

        Use the kill and resurrect methods if you want to keep track.
        '''
        if alive:
            self.alive = True
        else:
            self.alive = False

    def kill(self):
        '''
        Kill the organism living in this cell.
        '''
        self.times_killed += 1
        self.alive = False

    def resurrect(self):
        '''
        Bring the organism back to life.
        '''
        self.times_resurrected += 1
        self.alive = True

    def __str__(self):
        if self.alive:
            return "*"
        else:
            return " "



def clear_screen():
    '''
    Cler the terminal screen to display the next run of the simulation
    '''
    return subprocess.call('clear', shell=True)

def run(planet):
    '''
    Run the simulation.
    '''
    while True:
    #for i in range(0,10):
        clear_screen()
        planet.simulate()
        print(str(planet))

run(Planet())
