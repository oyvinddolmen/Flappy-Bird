import random
import pygame

pygame.init()
screen_width = 470
screen_height = 750
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy bird")

bg = pygame.image.load("C:/Users/oyvin/OneDrive/programmering/Games/småprosjekter/flappy bird/background.jpg")
img_bird = pygame.image.load("C:/Users/oyvin/OneDrive/programmering/Games/småprosjekter/flappy bird/bird1.png")
button_img = pygame.image.load("C:/Users/oyvin/OneDrive/programmering/Games/småprosjekter/flappy bird/button.png")
ground_scroll = 0
scroll_speed = 2

clock = pygame.time.Clock()
score = 0
bird_width = 91
bird_height = 64

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gravity = 0.5
        self.vel = 0
        self.constant = 10
        self.stopped = False
        self.img_bird = pygame.image.load("C:/Users/Øyvind/OneDrive/PyCharm/Games/småprosjekter/flappy bird/bird1.png")

    def draw_bird(self, win):
        img_rotated = pygame.transform.rotate(self.img_bird, - self.vel * 2)
        if not bird.stopped:
            win.blit(img_rotated, (self.x, self.y))

    def move_bird(self):
        if not bird.stopped:
            self.vel += self.gravity
            bird.y += self.vel

    def jump(self):
        self.vel = -6.5


# PIPES
lower_x = 450
width = 50
lower_height = 140
margin = 110
lower_top = screen_height - lower_height - margin
gap = 150

upper_x = lower_x
upper_top = 0
upper_height = screen_height - lower_height - margin - gap
pipes_bottom = []
pipes_upper = []
pipes_bottom.append([lower_x, lower_top, width, lower_height])
pipes_upper.append([upper_x, upper_top, width, upper_height])

def draw_pipe():
    if not bird.stopped:                    # stopper bakgrunnen fra å gå etter kræsj
        for pipe in pipes_bottom:
            pygame.draw.rect(win, (0, 128, 0), pygame.Rect(pipe[0], pipe[1], pipe[2], pipe[3]))
            pipe[0] -= 3

        for pipe in pipes_upper:
            pygame.draw.rect(win, (0, 128, 0), pygame.Rect(pipe[0], pipe[1], pipe[2], pipe[3]))
            pipe[0] -= 3

def draw_button():
    pos = pygame.mouse.get_pos()            # får x og y kordinat for musen i en tuple
    if 200 < pos[0] < 250 and 400 < pos[1] < 440:
        if pygame.mouse.get_pressed(3)[0] == 1:
            restart_game()


def restart_game():
    bird.y = 100
    bird.stopped = False
    global score
    score = 0
    pipes_upper.pop()
    pipes_bottom.pop()
    pipes_bottom.append([lower_x, lower_top, width, lower_height])
    pipes_upper.append([upper_x, upper_top, width, upper_height])
    draw_pipe()

def draw_game():
    win.blit(bg, (ground_scroll, 0))
    bird.move_bird()
    bird.draw_bird(win)
    draw_pipe()

    if bird.stopped:
        font = pygame.font.SysFont("comicsans", 40, True)  # henter fonten
        lost_message = font.render("You lost!", True, (0, 0, 0))
        win.blit(lost_message, (180, 100))
        win.blit(button_img, (200, 400))                    # viser restart button

    # tegner score
    font_score = pygame.font.SysFont("comicsans", 25, True)
    score_message = font_score.render(f"Score: {score.__round__()}", True, (255, 255, 255))
    win.blit(score_message, (350, 100))

    pygame.display.update()


# MAIN LOOP
the_game_is_on = True
bird = Player(0, 100, 91, 64)
while the_game_is_on:
    clock.tick(50)

    # rullerende bakgrunn
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 30:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            the_game_is_on = False

    keys = pygame.key.get_pressed()     # lagrer tasten du trykket som en variabel
    if keys[pygame.K_SPACE]:
        bird.jump()

    # sjekke kræsj bunn
    if bird.y > screen_height - bird.height - 120:
        bird.stopped = True

    # lager nye obstacles
    for pipe in pipes_bottom:
        if pipe[0] < pipe[2] - width - 30:
            # nedre obstacles
            new_lower_x = 450
            new_lower_height = random.random() * 400
            new_lower_top = screen_height - new_lower_height - margin
            pipes_bottom.append([new_lower_x, new_lower_top, width, new_lower_height])
            pipes_bottom.pop(0)     # fjerner den tidligere pipen
            score += 1

            # øvre obstacles
            new_upper_x = 450
            new_upper_top = 0
            new_upper_height = screen_height - new_lower_height - margin - gap
            pipes_upper.append([new_upper_x, new_upper_top, width, new_upper_height])
            pipes_upper.pop(0)

        # sjekke kræsj øvre obstacles
        if not bird.stopped:
            for pipe in pipes_upper:
                if bird.y < pipe[3] and pipe[0] < bird_width:
                    bird.stopped = True

        # sjekke kræsj nedre obstacless
        if not bird.stopped:
            for pipe in pipes_bottom:
                if bird.y + bird_height > pipe[1] and pipe[0] < bird.width:
                    bird.stopped = True

        if bird.stopped:
            # tegner restart button
            draw_button()

    draw_game()
pygame.quit()
