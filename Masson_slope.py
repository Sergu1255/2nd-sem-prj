import pygame

pygame.init()


WIDTH = 1000
HEIGHT = 1000

screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()

#varibles
gravity = 0.5
Wall_thickness = 10
bounce_stop = 0.3
def wall_draw():
    left = pygame.draw.line(screen,'white', (0,0), (0,HEIGHT), Wall_thickness)
    right = pygame.draw.line(screen,'white', (WIDTH,0), (WIDTH,HEIGHT), Wall_thickness)
    top = pygame.draw.line(screen,'white', (0,0), (WIDTH,0), Wall_thickness)
    bottom = pygame.draw.line(screen,'white', (0,HEIGHT), (WIDTH,HEIGHT), Wall_thickness)
    walls_list = [left, right,top,bottom]
    return walls_list
class Ball:
    def __init__(self,x_pos,y_pos,radius, color, mass, retention, y_speed, x_speed, id):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rad = radius
        self.color = color
        self.mass = mass
        self.reten = retention
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.id = id
        self.circle = ''
    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos,self.y_pos), self.rad)


    def check_grav(self):
        if self.y_pos < HEIGHT - self.rad - (Wall_thickness/2):
            self.y_speed += gravity
        else:
            if self.y_speed > bounce_stop:
                self.y_speed = self.y_speed * -1 * self.reten
            else:
                if abs(self.y_speed) <= bounce_stop:
                    self.y_speed = 0
        return self.y_speed
    def update_pos(self):
        self.y_pos += self.y_speed
        self.x_pos += self.x_speed

ball1 = Ball(50,50,30,'red',100, 0.9, 0,0,1)


run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    walls = wall_draw()
    ball1.draw()
    ball1.update_pos()
    ball1.y_speed = ball1.check_grav()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit

