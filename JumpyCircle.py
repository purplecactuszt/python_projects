import pygame
import random

pygame.init()

score = 0
white = (255, 255, 255)
black = (0, 0, 0)
X = 0
Y = 700

window = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Leonardova čudesna igrica")
clock = pygame.time.Clock()

run = True

position = [350, 620]
grav = 20
enemy_pos = [random.randint(50, 650), random.randint(0, Y // 2), 25, 25]
enemy_side_grav = random.randint(-30, 30)
enemy_top_grav = random.randint(-30, 30)

while run:
    clock.tick(20)

    font = pygame.font.SysFont("Palatino Linotype", 20, bold=True)
    text = font.render("Score: " + str(score), True, white, black)

    textRect = text.get_rect()

    player = pygame.draw.circle(window, (150, 150, 0), position, 20, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position[1] -= 30
            score += 1
    position[1] += 5

    if position[1] - 15 <= 0:
        position[1] = 15
    elif position[1] + 15 >= 700:
        print("Your score was:", score)
        pygame.quit()
    if position[0] - 15 <= 0:
        position[0] = 15
        grav *= -1
    elif position[0] + 15 >= 700:
        position[0] = 685
        grav *= -1

    position[0] += grav

    enemy = pygame.draw.rect(window, (255, 0, 0), enemy_pos)

    enemy_pos[0] += enemy_side_grav
    enemy_pos[1] += enemy_top_grav
    if enemy.right >= 700:
        enemy_pos[0] = 674
        enemy_side_grav = random.randint(10, 30)
        enemy_side_grav *= -1
    elif enemy.left <= 0:
        enemy_pos[0] = 26
        enemy_side_grav = random.randint(-30, -10)
        enemy_side_grav *= -1
    if enemy.bottom >= 700:
        enemy_pos[1] = 674
        enemy_top_grav = random.randint(10, 30)
        enemy_top_grav *= -1
    elif enemy.top <= 0:
        enemy_pos[1] = 26
        enemy_top_grav = random.randint(-30, -10)
        enemy_top_grav *= -1

    if player.top - 15 <= enemy.bottom and player.left <= enemy.right and player.right >= enemy.left:
        if player.bottom < enemy.top:
            pass
        else:
            print("Your score was:", score)
            pygame.quit()
    try:
        window.blit(text, textRect)

        pygame.display.update()

        window.fill((0, 0, 0))
    except:
        print("Thanks for playing")
        pygame.quit()

pygame.quit()
