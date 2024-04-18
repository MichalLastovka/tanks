import pygame
import os

pygame.init()
WIDTH = 2500
HEIGHT = 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

current_fired_projectiles = []
projectile_speed = 9

field = pygame.Surface((WIDTH*0.8, HEIGHT*0.9))
field.fill("black")

tank_image_up = pygame.image.load("res/tank_up.png").convert_alpha()
tank_image_right = pygame.image.load("res/tank_right.png").convert_alpha()
tank_image_left = pygame.image.load("res/tank_left.png").convert_alpha()
tank_image_down = pygame.image.load("res/tank_down.png").convert_alpha()

tank_rect = tank_image_up.get_rect(topleft=(100, 100))

def fire_projectile(x, y):
    current_fired_projectiles.append((pygame.Rect(x, y, 5, 5), current_direction))

def move_projectiles():
    for projectile in current_fired_projectiles:
        if projectile[1] == tank_image_up:
            projectile[0].y -= projectile_speed

        if projectile[1] == tank_image_down:
            projectile[0].y += projectile_speed

        if projectile[1] == tank_image_right:
            projectile[0].x += projectile_speed
        
        if projectile[1] == tank_image_left:
            projectile[0].x -= projectile_speed



current_direction = tank_image_up




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_projectile(tank_rect.x, tank_rect.y)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        current_direction = tank_image_up
        tank_rect.y -= 3
    if keys[pygame.K_s]:
        current_direction = tank_image_down
        tank_rect.y += 3
    if keys[pygame.K_d]:
        current_direction = tank_image_right
        tank_rect.x += 3
    if keys[pygame.K_a]:
        current_direction = tank_image_left
        tank_rect.x -= 3
    #if keys[pygame.K_SPACE]:
        #fire_projectile(tank_rect.x, tank_rect.y)  

    

    screen.fill("gray")
    screen.blit(field, ((WIDTH/2 - WIDTH*0.9/2), HEIGHT/2 - HEIGHT*0.9/2))
    screen.blit(current_direction, tank_rect)

    for projectile in current_fired_projectiles:
        print(projectile)
        pygame.draw.rect(screen, "white", projectile[0])
    
    move_projectiles()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

