import pygame
import random

pygame.init()      # initaliserer modulene i pygame

SCREEN = pygame.display.set_mode((400, 600))    # størrelse skjerm

# background
BACKGROUND_IMAGE = pygame.image.load("C:/Users/Øyvind/OneDrive/PyCharm/Games/småprosjekter/flappy bird/background.jpg")

# bird
BIRD_IMAGE = pygame.image.load("C:/Users/Øyvind/OneDrive/PyCharm/Games/småprosjekter/flappy bird/bird1.png")
bird_x = 50
bird_y = 300
speed = 0

def display_bird(x, y):
    SCREEN.blit(BIRD_IMAGE, (x, y))

# OBSTACLES
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGTH = random.randint(150, 450)
OBSTACLE_COLOR = (0, 191, 16)
OBSTACLE_X_CHANGE = -0.2        # beveger seg til venstre
obstacle_x = 500            # starter ytterst til høyre

def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, pygame.Rect(obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_y = height + 200  # I chose 200 as the space between my top and bottom to make it easier instead of 150
    bottom_height = 635 - bottom_y
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, pygame.Rect(obstacle_x, bottom_y, OBSTACLE_WIDTH, bottom_height))

# COLLISION DETECTION
def collision_detection(obstacle_x, obstacle_height, bird_y, bottom_height):
    if 50 <= obstacle_x <= (50 + 64):
        if bird_y <= obstacle_height or bird_y >= bottom_height:
            return True
    return False

# DISPLAY SCORE FUNCTION
score = 0
SCORE_FONT = pygame.font.Font(None, 32)
def score_dispay(score):
    display = SCORE_FONT.render(f"score: {score}", True, (255, 255, 255))
    SCREEN.blit(display, (10, 10))

running = True
while running:
    SCREEN.fill((0, 0, 0))

    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # hvis du trykker exit stopper for løkken og spillet
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                speed = -0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                speed = 0.1

    bird_y += speed

    if bird_y <= 0:
        bird_y = 0
    if bird_y > 571:
        bird_y = 571

    obstacle_x += OBSTACLE_X_CHANGE         # moving the obstacle

    # generating new obstacles
    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGTH = random.randint(200, 400)
        score += 1
    display_obstacle(OBSTACLE_HEIGTH)       # display obsticles

    # COLLISION
    collision = collision_detection(obstacle_x, OBSTACLE_HEIGTH, bird_y, OBSTACLE_HEIGTH + 150)
    if collision:
        pygame.quit()

    # displaying the bird
    display_bird(bird_x, bird_y)

    # display the score
    score_dispay(score)

    pygame.display.update()                 # oppdaterer displayet

pygame.quit()
