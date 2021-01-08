import sys
import pygame
import random   

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

wood_bg = pygame.image.load('Wood_BG.png')
land_bg = pygame.image.load('Land_BG.png')
water_bg = pygame.image.load('Water_BG.png')
cloud1 = pygame.image.load('Cloud1.png')
cloud2 = pygame.image.load('Cloud2.png')
crosshair = pygame.image.load('crosshair.png')
crosshair_rect = None
duck_surface = pygame.image.load('duck.png')
gun_shot = pygame.mixer.Sound('gun_shot.wav')
duckduck = pygame.mixer.Sound('mixkit-battle-man-scream-2175.wav')
duuck = pygame.mixer.Sound('g3sg1_boltpull.wav')


game_font = pygame.font.Font(None, 70)
text_surface = game_font.render('You Win :D', True, (5, 255, 0))

land_position_y = 510
land_speed = 0.5
water_position_y = 650
water_speed = 2

duck_list = []
for duck in range(30):
    duck_pos_x = random.randrange(50, 1200)
    duck_pos_y = random.randrange(50, 600)
    duck_rect = duck_surface.get_rect(center = (duck_pos_x, duck_pos_y))
    duck_list.append(duck_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center = event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            gun_shot.play()
            for index, duck_rect in enumerate(duck_list):
                if duck_rect.collidepoint(event.pos):
                    del duck_list[index]
                    duckduck.play()
                    
                    


    #Backgrounds
    screen.blit(wood_bg, (0, 0))
    land_position_y += land_speed
    water_position_y += water_speed

    if land_position_y <= 500 or land_position_y >= 520:
        land_speed *= -1

    if water_position_y <= 600 or water_position_y >= 660:
        water_speed *= -1

    screen.blit(land_bg, (0, land_position_y))
    screen.blit(water_bg, (0, water_position_y))

 

    #duckz
    for duck_rect in duck_list:
        screen.blit(duck_surface, duck_rect)
    
    

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
    
    if len(duck_list) <= 0:
        screen.blit(text_surface, (550, 360))


    #crosshair
    if crosshair_rect is not None:
        screen.blit(crosshair, crosshair_rect)

    pygame.display.update()
    clock.tick(120)

