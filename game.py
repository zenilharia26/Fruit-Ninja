import pygame, sys, os
import time
import random


width = 600
height = 800
clock = pygame.time.Clock()
g = 1
score = 0
fps = 13
fruits = ['watermelon', 'orange']

pygame.init()
gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill((255,255,255))

def generate_random_fruits(fruit):

    path = os.path.join(os.getcwd(), fruit+'.png')
    data[fruit] = {
        #'img' : pygame.image.load(r'C:\\Users\\Zenil\\Documents\\CSI\\Fruit-Ninja\\'+fruit+'.png'),
        'img' : pygame.image.load(path),
        'x' : random.randint(50, 550),
        'y' : 800,
        'speed_x' : random.randint(-10, 10),
        'speed_y' : random.randint(-101, -80),
        'throw' : False,
        't' : 0
    }

    if(random.random() >= 0.75):
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False

data = {}
for fruit in fruits:
    generate_random_fruits(fruit)

pygame.display.update()
print(data)

while True:
    gameDisplay.fill((255,255,255))
    for key,value in data.items():
        if value['throw']:
            value['x'] = value['x'] + value['speed_x']
            value['y'] = value['y'] + value['speed_y']
            value['speed_y'] += (g*value['t'])
            value['t'] += 1

            if value['y'] <= 800:
                gameDisplay.blit(value['img'], (value['x'],value['y']))
            else:
                generate_random_fruits(key)

            current_position = pygame.mouse.get_pos()
            #print(current_position)
            if current_position[0] > value['x'] and current_position[0] < value['x']+60 and current_position[1] > value['y'] and current_position[1] < value['y']+60:
                # value['img'] = pygame.image.load(r'C:\\Users\\Zenil\\Documents\\CSI\\Fruit-Ninja\\half_'+key+'.png')
                path = os.path.join(os.getcwd(),'half_'+key+'.png')
                value['img'] = pygame.image.load(path)
                value['speed_x'] += 10
                score += 1
                print('Hit, new score is', score)

        else:
            generate_random_fruits(key)

    pygame.display.update()
    clock.tick(fps)

    '''current_position = pygame.mouse.get_pos()
    if current_position[0] > init_x and current_position[0] < init_x+60 and current_position[1] > init_y and current_position[1] < init_y+60:
        print('Hit')'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


