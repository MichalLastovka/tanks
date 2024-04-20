import pygame
import os

pygame.init()

# Window and fields
RESOLUTION = pygame.display.get_desktop_sizes()
WIDTH = RESOLUTION[0][0] * 0.8
HEIGHT = RESOLUTION[0][1] * 0.8
screen = pygame.display.set_mode((WIDTH, HEIGHT))
field_width = screen.get_width() * 0.8
field_height = screen.get_height() * 0.9
field = pygame.Surface((field_width, field_height))
field.fill("black")

game_pixel = field_width/16


clock = pygame.time.Clock()
running = True



current_fired_projectiles = []
bricks = []




projectile_speed = 9


# Image loadup
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

def check_wall_hit():
    for projectile in current_fired_projectiles:
        for brick in bricks:
            if pygame.Rect.colliderect(projectile[0], brick):
                print("Wall hit!")
                print(bricks)
                bricks.remove(brick)

def draw_wall(x, y):
    bricks.append(pygame.Rect((x, y, game_pixel, game_pixel)))


draw_wall(0, 0)
draw_wall(game_pixel * 2, 0)
draw_wall(game_pixel * 4, 0)
draw_wall(game_pixel * 6, 0)



current_direction = tank_image_up




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_projectile((tank_rect.x + tank_rect.width / 2), (tank_rect.y + tank_rect.height / 2))

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

    screen.fill("gray")
    screen.blit(field, (WIDTH / 2 - field_width / 2, HEIGHT / 2 - field_height / 2))
    screen.blit(current_direction, tank_rect)

    for projectile in current_fired_projectiles:
        pygame.draw.rect(screen, "white", projectile[0])
    

    

    move_projectiles()
    check_wall_hit()

    for brick in bricks:
        field.blit(field, brick)
    
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

