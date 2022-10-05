# Importar librerías
import pygame

# Initialize pygame
pygame.init()

# Colors
background_color = (0, 72, 139)
players_color = (255, 255, 255)
ball_color = (201, 209, 255)


# Window size
screen_width = 800
screen_height = 600

# Size variable
size = (screen_width, screen_height)

# Display the window
screen = pygame.display.set_mode(size)

# Players size
player_width = 15
player_height = 90

# Player 1 coordinates
player1_x = 64
player1_y = 32

# Player 2 coordinates
player2_x = screen_width - 64
player2_y = 32

# Ball coordinates
ball_x = 250
ball_y = 300
ball_radius = 16

# Title
pygame.display.set_caption("Python Pong")

# Icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with color
    screen.fill(background_color)

    # Drawing area

    # Define the player 1 - left
    player1 = pygame.draw.rect(screen, players_color, (player1_x, player1_y, player_width, player_height))

    # Define the player 2 - right
    player2 = pygame.draw.rect(screen, players_color, (player2_x, player2_y, player_width, player_height))

    # Define the ball
    ball = pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Refresh the window
    pygame.display.flip()