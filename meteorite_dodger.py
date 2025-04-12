import pygame
import random
import time

# Initialize Pygame library
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meteorite Dodger")

# Load game images (player, obstacles, background, lives, power-up)
rover_image = pygame.image.load('assests/rover.png')
meteorite_image = pygame.image.load('assests/meteorite.png')
mars_bg = pygame.image.load('assests/mars_surface.png')  # background image
heart_image = pygame.image.load('assests/heart.png')  # heart symbol for lives
shield_image = pygame.image.load('assests/shield.png')  # shield for temporary invincibility

# Scale images to in-game sizes
rover_image = pygame.transform.scale(rover_image, (80, 80))
meteorite_image = pygame.transform.scale(meteorite_image, (60, 60))
heart_image = pygame.transform.scale(heart_image, (30, 30))
shield_image = pygame.transform.scale(shield_image, (40, 40))

# Define commonly used colors
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)
BLACK = (0, 0, 0)

# Set initial player position and speed
rover_x = WIDTH // 2
rover_y = HEIGHT - 100
rover_speed = 5

# Initialize gameplay state
meteorites = []  # list to hold active meteorites
shield_powerups = []  # list to hold active shield power-ups
lives = 3  # total lives the player starts with
is_invincible = False  # whether player is currently invincible
invincible_start_time = 0  # when invincibility was activated
invincible_duration = 5  # how long invincibility lasts in seconds

# Set up game clock and font for UI
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

# Draw a clickable button with hover effect
def draw_button(text, rect, hover):
    pygame.draw.rect(screen, DARK_GRAY if hover else GRAY, rect)
    label = font.render(text, True, WHITE)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)

# Generate a meteorite with random position and falling speed
#-----------------------TASK 1-------------------------------
# TASK: Complete the line below to randomly assign a falling speed to the meteorite
# Hint:
# random.randint(a, b) – Returns a random integer between a and b (inclusive).
# random.uniform(a, b) – Returns a random float between a and b.
# random.random() – Returns a random float between 0.0 and 1.0.

def create_meteor():
    x = random.randint(0, WIDTH - 40)
    y = -40
    speed = #insert random function
    meteorites.append([x, y, speed])

#Generate a shield power-up with set speed
def create_shield_powerup():
    x = random.randint(0, WIDTH - 40)
    y = -40
    speed = 3
    shield_powerups.append([x, y, speed])

#Move any falling object (meteor or shield); return False if off screen
def move_item(item):
    item[1] += item[2]
    return item[1] <= HEIGHT

#Detect collision between two rectangular areas
#Uses pygame.Rect objects and the built-in colliderect() method
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)


#Display hearts on screen to represent player lives
def draw_hearts():
    for i in range(lives):
        screen.blit(heart_image, (10 + i * 25, 10))


#Draw the full game screen, including background, player, enemies, and UI
def draw_game():
    screen.blit(mars_bg, (0, 0))

    #pygame.Rect is used to define the position and size of game objects
    #Even though you're drawing images, the game tracks them with invisible rectangles
    rover_rect = pygame.Rect(rover_x, rover_y, 60, 60)

    #Highlight the rover with a glowing border when invincible
    if is_invincible:
        pygame.draw.rect(screen, (255, 255, 0), rover_rect.inflate(10, 10), 3)

    screen.blit(rover_image, (rover_x, rover_y))

    for m in meteorites:
        screen.blit(meteorite_image, (m[0], m[1]))
    for s in shield_powerups:
        screen.blit(shield_image, (s[0], s[1]))

    draw_hearts()
    pygame.display.flip()


#Show the opening start screen and wait for player to click "Start Game"
def start_screen():
    while True:
        screen.blit(mars_bg, (0, 0))

        start_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
        mouse = pygame.mouse.get_pos()
        hover = start_rect.collidepoint(mouse)
        draw_button("Start Game", start_rect, hover)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and hover:
                return True


#Display Game Over screen with options to Replay or Quit
def game_over_screen():
    while True:
        screen.blit(mars_bg, (0, 0))
        game_over_text = font.render("Game Over!", True, WHITE)
        text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(game_over_text, text_rect)

        replay_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
        quit_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 70, 200, 50)
        mouse = pygame.mouse.get_pos()

        replay_hover = replay_rect.collidepoint(mouse)
        quit_hover = quit_rect.collidepoint(mouse)

        draw_button("Replay", replay_rect, replay_hover)
        draw_button("Quit", quit_rect, quit_hover)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if replay_hover:
                    return True
                elif quit_hover:
                    pygame.quit()
                    return False


#Core gameplay loop
def main_game():
    global rover_x, lives, is_invincible, invincible_start_time, meteorites, shield_powerups

    #Reset game variables for a new session
    rover_x = WIDTH // 2
    lives = 3
    is_invincible = False
    invincible_start_time = 0
    meteorites = []
    shield_powerups = []

    while True:
        clock.tick(60)  #run at 60 frames per second

        #Disable invincibility after duration ends
        if is_invincible and time.time() - invincible_start_time > invincible_duration:
            is_invincible = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        # Handle player input for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and rover_x > 0:
            rover_x -= rover_speed
        if keys[pygame.K_RIGHT] and rover_x < WIDTH - 60:
            rover_x += rover_speed

        #---------------------- TASK 2 -------------------------
        #TASK: Add code to randomly spawn meteorites and shields
        #HINT1: random.random() gives a float between 0.0 and 1.0
        #HINT2: A smaller number means a lower probability of the meteorite or shield appearing.

        if random.random() < #insert a float:
            #insert line to add a meteorite to the game

        if random.random() < #insert a float:
            #insert line to add a shield to the game

        # Update positions of all falling objects
        meteorites[:] = [m for m in meteorites if move_item(m)]
        shield_powerups[:] = [s for s in shield_powerups if move_item(s)]

        # Check collisions with meteorites
        rover_rect = pygame.Rect(rover_x, rover_y, 60, 60)

        if not is_invincible:
            for m in meteorites:
                meteorite_rect = pygame.Rect(m[0], m[1], 40, 40)
                if check_collision(rover_rect, meteorite_rect):
                    lives -= 1
                    meteorites.remove(m)
                    if lives <= 0:
                        return game_over_screen()
                    break  # avoid detecting multiple hits at once

        # Check if player collected a shield
        for s in shield_powerups:
            shield_rect = pygame.Rect(s[0], s[1], 40, 40)
            if check_collision(rover_rect, shield_rect):
                is_invincible = True
                invincible_start_time = time.time()
                shield_powerups.remove(s)
                break

        draw_game()

# Run the game if player starts it
if start_screen():
    while main_game():
        pass

# Exit the game
pygame.quit()