import sys
import pygame
import conway

class Grid(conway.Planet):
    '''
    Grid that all organisms live on
    '''

    def __init__(self):
        self.size = [640, 480]
        super(Grid, self).__init__()
        self.screen = pygame.display.set_mode(self.size)

        self.organisms = []

    def add_organism(self,organism):
        self.organisms.append(organism)
        organism.set_planet(self)

    def kill_organism(self,index):
        self.organisms.pop(index)
    
    def get_organisms(self):
        return self.organisms

    def simulate(self):
        self.screen.fill(white)

        for organism in self.organisms:
            organism.move()
            pygame.draw.rect(self.screen, (0, 0, 255), organism)

    def get_width(self):
        return self.size[0]

    def get_height(self):
        return self.size[1]

class GridSpace(pygame.Rect, conway.Organism):
    ''' 
    Display of an organism
    '''

    def __init__(self):
        super(GridSpace, self).__init__(0,0,0,0)

        self.left = 0
        self.top = 0
        self.width = 100
        self.height = 100

        self.speed = [2, 2]

        self.planet = None

    def set_planet(self, planet):
        self.planet = planet

    def set_speed(self, speed):
        self.speed = speed

    def is_collided_with(self):
        return self.collidelistall(self.planet.get_organisms())

    def move(self):
        if self.left < 0 or self.right > self.planet.get_width():
            self.speed[0] = -self.speed[0]
        if self.top < 0 or self.bottom > self.planet.get_height():
            self.speed[1] = -self.speed[1]

        self.left += self.speed[0]
        self.top -= self.speed[1]

        if self.is_collided_with():
            print(self.is_collided_with())


# colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

planet = Grid()
planet.add_organism(GridSpace())

x = GridSpace()
x.set_speed([3,3])
x.left = 100
x.top = 100
planet.add_organism(x)

pygame.init()

while 1:
#for meow in range(1, 500):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    planet.simulate()
    pygame.display.update()