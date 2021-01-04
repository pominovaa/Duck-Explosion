import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

wood_bg = pygame.image.load('Wood_BG.png')
land_bg = pygame.image.load('Land_BG.png')
water_bg = pygame.image.load('Water_BG.png')
cloud1 = pygame.image.load('Cloud1.png')
cloud2 = pygame.image.load('Cloud2.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(wood_bg, (0, 0))
    screen.blit(land_bg, (0, 560))
    screen.blit(water_bg, (0, 640))
    screen.blit(cloud1, (900, 123))
    screen.blit(cloud2, (878, 46))
    screen.blit(cloud1, (342, 146))
    screen.blit(cloud2, (678, 78))
    screen.blit(cloud2, (567, 46))
    screen.blit(cloud2, (345, 242))
    screen.blit(cloud2, (431, 65))
    screen.blit(cloud2, (834, 137))
    screen.blit(cloud2, (1189, 56))
    screen.blit(cloud2, (777, 44))
    screen.blit(cloud2, (111, 111))
    screen.blit(cloud2, (987, 98))
    screen.blit(cloud2, (498, 43))


    pygame.display.update()
    clock.tick(120)

