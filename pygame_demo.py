import sys
import pygame

pygame.init()

class PaleBlueDot(pygame.Rect):
    ''' 
    Display of an organism
    '''

    def __init__(self):
        super(PaleBlueDot, self).__init__(0,0,0,0)

        self.left = 0
        self.top = 0
        self.width = 100
        self.height = 100

    def success(self):
        print("moo!")


size = width, height = 640, 480
speed = [2, 2]

# colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")

rectangle = PaleBlueDot() #pygame.Rect(0, 0, 100, 100)

#while 1:
for meow in range(1, 500):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    print rectangle
    rectangle.move_ip(speed)

    if rectangle.left < 0 or rectangle.right > width:
        speed[0] = -speed[0]
    if rectangle.top < 0 or rectangle.bottom > height:
        speed[1] = -speed[1]

    screen.fill(white)
    #screen.blit(ball, rectangle)
    pygame.draw.rect(screen, blue, rectangle)
    rectangle.success()
    #pygame.display.flip()
    pygame.display.update()