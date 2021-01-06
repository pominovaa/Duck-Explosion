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
crosshair = pygame.image.load('crosshair.png')
crosshair_rect = None

land_position_y = 510
land_speed = 0.5
water_position_y = 650
water_speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center = event.pos)


    #Background
    
    screen.blit(wood_bg, (0, 0))
    land_position_y += land_speed
    water_position_y += water_speed

    if land_position_y <= 500 or land_position_y >= 520:
        land_speed *= -1

    if water_position_y <= 600 or water_position_y >= 660:
        water_speed *= -1

    screen.blit(land_bg, (0, land_position_y))
    screen.blit(water_bg, (0, water_position_y))




    #Clouds
    screen.blit(cloud1, (900, 123))
    screen.blit(cloud2, (878, 46))
    screen.blit(cloud1, (342, 146))
    screen.blit(cloud2, (678, 78))
    screen.blit(cloud1, (567, 46))
    screen.blit(cloud2, (345, 242))
    screen.blit(cloud1, (431, 65))
    screen.blit(cloud2, (834, 137))
    screen.blit(cloud1, (1189, 56))
    screen.blit(cloud2, (777, 44))
    screen.blit(cloud1, (111, 111))
    screen.blit(cloud2, (987, 98))
    screen.blit(cloud1, (498, 43))

    #crosshair
    if crosshair_rect is not None:
        screen.blit(crosshair, crosshair_rect)

    pygame.display.update()
    clock.tick(120)

