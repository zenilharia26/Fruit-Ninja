import pygame, sys
from pygame.locals import *
import time
import random


width = 600
height = 800
clock = pygame.time.Clock()

pygame.init()
gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill((0,0,0))

def generate_random_fruits():
    for key,value in data.items():
        if(random.random() >= 0.5):
            value['throw'] = True
        else:
            value['throw'] = False

data = {
    'watermelon' : {
        'img' : pygame.image.load(r'C:\\Users\\Zenil\\Documents\\CSI\\Fruit Ninja\\watermelon.png'),
        'x' : 0,
        'y' : 800,
        'speed_x' : 0,
        'speed_y' : -80,
        'throw' : False,
        't' : 0
    },

    'orange' : {
        'img' : pygame.image.load(r'C:\\Users\\Zenil\\Documents\\CSI\\Fruit Ninja\\orange.png'),
        'x' : 400,
        'y' : 800,
        'speed_x' : -10,
        'speed_y' : -80,
        'throw' : False,
        't' : 0
    }
}

g = 1

pygame.display.update()
generate_random_fruits()
print(data)

while True:
    gameDisplay.fill((0,0,0))
    for key,value in data.items():
        if value['throw']:
            value['x'] = value['x'] + value['speed_x']
            value['y'] = value['y'] + value['speed_y']
            value['speed_y'] += (g*value['t'])
            value['t'] += 1

            if value['y'] > 800:
                value['y'] = 800
                value['speed_y'] = -80
                value['t'] = 0

            gameDisplay.blit(value['img'], (value['x'],value['y']))
    
    pygame.display.update()
    clock.tick(13)
    
    '''current_position = pygame.mouse.get_pos()
    if current_position[0] > init_x and current_position[0] < init_x+60 and current_position[1] > init_y and current_position[1] < init_y+60:
        print('Hit')'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    