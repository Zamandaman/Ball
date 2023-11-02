import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32) # size of app window
background_color = (255, 255, 255)  # Black background color
sprite_color = (111, 55, 0)     # Blue sprite color

gravity = 0.2
x = 0.
y = 100.

x2 = 0.
y2 = 100.
#
x3 = 0.
y3 = 100.

ball_width = 20.
ball_height = 20.
x_speed = 4.
y_speed = 4.

x2_speed = 10.
y2_speed = 10.

x3_speed = 4.
y3_speed = 4.

sprite_color2 = (0,255,0)
ball2_width = 20.
ball2_height =20.

sprite_color3 = (0,0,255)
ball3_width = 20.
ball3_height =20.


clock = pygame.time.Clock()  # Create a clock object for controlling frame rate
frame_rate = 60  # Number of frames per second
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill(background_color)
    pygame.draw.ellipse(screen, sprite_color, (x, y, ball_width, ball_width))
    y_speed += gravity 
    x += x_speed  # reverse movement
    if x > 620. or x < 0:
        x_speed = -x_speed
    x += x_speed  # reverse movement

    if y > 460. or y < 0:
        y_speed = -y_speed
        ball_width += 50
    y += y_speed

    pygame.draw.ellipse(screen, sprite_color2, (x2, y2, ball2_width, ball2_width))
    y2_speed += gravity 
    x2 += x2_speed

    if x2 > 640. or x2 < 0:
        x2_speed = -x2_speed
    x2 += x2_speed
    
    if y2 > 460. or y2 < 0:
        y2_speed = -y2_speed
        ball2_width += 50
    y2 += y2_speed

    pygame.draw.ellipse(screen, sprite_color3, (x3, y3, ball3_width, ball3_height))
    y3_speed += gravity 
    if x3 > 640. or x3 < 0:
        x3_speed = -x3_speed
    x3 += x3_speed
    
    if y3 > 460. or y3 < 0:
        y3_speed = -y3_speed
        ball3_width += 50
        ball3_height += 50 
    y3 += y3_speed
    
    


    
    


    

    pygame.display.update()
    clock.tick(frame_rate)  # Limit the frame rate
