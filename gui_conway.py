import sys
import pygame
import conway

class Grid(conway.Planet):
    '''
    Grid that all organisms live on
    '''

    def __init__(self):
        self.size = [700, 700]
        self.screen = pygame.display.set_mode(self.size)

        self.organisms = []

        self.spacer = 2

        super(Grid, self).__init__()
        self.matrix = []

        # Populate the matrix based on the requirements passed
        size = 100
        for x in range(size):
            row = []
            for y in range(size):
                item = GridSpace(self)
                # Arrange items in a grid on the display
                item.set_location((x * (item.height + self.spacer)),(y * (item.width + self.spacer)))
                row.append(item)
            self.matrix.append(row)

        self.load_config()

    def simulate(self):
        '''
        Simulate the life/death of all organisms on the planet
        '''
        super(Grid, self).simulate()
        self.screen.fill((255,255,255))

        for row in self.matrix:
            for organism in row:
                organism.animate()                

class GridSpace(conway.Organism, pygame.Rect):
    ''' 
    Display of an organism
    '''

    def __init__(self,planet):
        super(GridSpace, self).__init__()
        
        self.left = 0
        self.top = 0
        self.width = 5
        self.height = 5

        self.color = (255, 255, 240)

        self.planet = planet

    def get_color(self):
        '''
        Returns the current color of the organism in RGB format (R, G, B)
        '''
        return self.color

    def get_collides(self):
        '''
        Returns a list of all rectangles on the "planet" that overlap
        '''
        organisms = []

        for x in self.planet.get_organisms():
            for y in x:
                organisms.append(y)
            
        collides = [organisms[x] for x in self.collidelistall(organisms)]
        #collides.remove(self)

        return collides

    def animate(self):
        '''
        Draw the organism on the planet
        '''
        if self.alive:
            self.color = (200, 10, 10)
        else:
            self.color = (240, 240, 240)

        pygame.draw.rect(self.planet.screen, self.color, self)

    def set_location(self,x,y):
        '''
        Move the organism to the location specified
        '''
        self.top = x
        self.left = y

if __name__ == "__main__":
    planet = Grid()

    pygame.init()

    while 1:
    #for meow in range(1, 500):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        planet.simulate()
        pygame.display.update()