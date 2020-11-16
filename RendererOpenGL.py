import pygame
from pygame.locals import *

from gl import Renderer
import shaders



deltaTime = 0.0

# Inicializacion de pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

# Inicializacion de nuestro Renderer en OpenGL
r = Renderer(screen)
r.setShaders(shaders.vertex_shader, shaders.fragment_shader)
r.createObjects()


cubeX = 0
cubeY = 0
cubeZ = 0
cubeP = 0
cubeR = 0
cubeYawl = 0

isPlaying = True
while isPlaying:

    # Para revisar si una tecla esta presionada
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        cubeX -= 2 * deltaTime
    if keys[pygame.K_d]:
        cubeX += 2 * deltaTime
    if keys[pygame.K_w]:
        cubeY -= 2 * deltaTime
    if keys[pygame.K_s]:
        cubeY += 2 * deltaTime
    if keys[pygame.K_z]:
        cubeZ -= 2 * deltaTime
    if keys[pygame.K_x]:
        cubeZ += 2 * deltaTime
    if keys[pygame.K_UP]:
        cubeP += 25 * deltaTime        
    if keys[pygame.K_DOWN]:
        cubeP -= 25 * deltaTime 
    if keys[pygame.K_LEFT]:
        cubeR += 25 * deltaTime 
    if keys[pygame.K_RIGHT]:
        cubeR -= 25 * deltaTime 
    if keys[pygame.K_y]:
        cubeYawl -= 25 * deltaTime 
    if keys[pygame.K_u]:
        cubeYawl += 25 * deltaTime 
    if keys[pygame.K_F5]:
        cubeX = 0
        cubeY = 0
        cubeZ = 0
        cubeP = 0
        cubeR = 0
        cubeYawl = 0

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            # para revisar en el momento que se presiona una tecla
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False


    r.translateCube(cubeX, cubeY, cubeZ)
    r.rollCube(cubeR)
    r.pitchCube(cubeP)
    r.yawlCube(cubeYawl)
    # Main Renderer Loop
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000


pygame.quit()
