# Importar librerías
import pygame
import math
import random as rd

# Initialize pygame
pygame.init()

# Colors
background_color = (0, 72, 139)
players_color = (255, 255, 255)
ball_color = (201, 209, 255)
line_color = (0, 17, 106)

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
player1_y_speed = 0

# Player 2 coordinates
player2_x = screen_width - 64
player2_y = 250
player2_y_speed = 0

# Ball coordinates
ball_x = 400
ball_y = 300
ball_radius = 16
ball_speed_x = 0.15
ball_speed_y = 0.15

# Scores
player1_score = 0
player2_score = 0

# Score font
score_font = pygame.font.Font("font.otf", 32)

# Won font
won_font = pygame.font.Font("font.otf", 64)

# Won text position
won_x = 200
won_y = 250

# Score position - Player 1
player1_score_x = 10
player1_score_y = 10

# Score position - Player 2
player2_score_x = screen_width - 190
player2_score_y = 10

# Player 1 score funtion
def show_score1(x, y):
    score1 = score_font.render("Player 1: " + str(player1_score), True, (0, 0, 0))
    screen.blit(score1, (x, y))

# Player 2 score funtion
def show_score2(x, y):
    score2 = score_font.render("Player 2: " + str(player2_score), True, (0, 0, 0))
    screen.blit(score2, (x, y))

# Line size
line_width = 8
line_height = 600

# Line position
line_x = 396
line_y = 0

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
        
        # Players Key controls
        if event.type == pygame.KEYDOWN:

            # Player 1
            if event.key == pygame.K_w:
                player1_y_speed = -0.4
            
            if event.key == pygame.K_s:
                player1_y_speed = 0.4
            
            # Player 2
            if event.key == pygame.K_UP:
                player2_y_speed = -0.4
            
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0.4

        if event.type == pygame.KEYUP:

            # Player 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            
            if event.key == pygame.K_s:
                player1_y_speed = 0
        
            # Player 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0

            if event.key == pygame.K_DOWN:
                player2_y_speed = 0
            
    # Players movement
    player1_y += player1_y_speed
    player2_y += player2_y_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Players collisions
    
    # Player 1
    if player1_y <= 0:
        player1_y = 0
    
    if player1_y >= screen_height - player_height:
        player1_y = screen_height - player_height
    
    # Player 2
    if player2_y <= 0:
        player2_y = 0
    
    if player2_y >= screen_height - player_height:
        player2_y = screen_height - player_height

    # Fill the screen with color
    screen.fill(background_color)

    # Drawing area

    # Define the line
    line = pygame.draw.rect(screen, line_color, (line_x, line_y, line_width, line_height))

    # Define the player 1 - left
    player1 = pygame.draw.rect(screen, players_color, (player1_x, player1_y, player_width, player_height))

    # Define the player 2 - right
    player2 = pygame.draw.rect(screen, players_color, (player2_x, player2_y, player_width, player_height))

    # Define the ball
    ball = pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Ball collision
    if ball_y > (screen_height - ball_radius) or ball_y < ball_radius:
        ball_speed_y *= -1
    
    # Ball collision and score update
    if ball_x > screen_width:
        ball_x = screen_width/2
        ball_y = screen_height/2
        ball_speed_x = rd.choice((-0.15, 0.15))
        player1_score += 1
    elif ball_x < 0:
        ball_x = screen_width/2
        ball_y = screen_height/2
        ball_speed_x = rd.choice((-0.15, 0.15))
        player2_score += 1
    
    # Colitions
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
    
    # Show won text
    if player1_score >= 3:
        won_text = won_font.render("Player 1 won", True, (0, 0, 0))
        screen.blit(won_text, (won_x, won_y))
        ball_speed_x = 0
        ball_speed_y = 0
        player1_y_speed = 0
        player2_y_speed = 0
    elif player2_score >= 3:
        won_text = won_font.render("Player 2 won", True, (0, 0, 0))
        screen.blit(won_text, (won_x, won_y))
        ball_speed_x = 0
        ball_speed_x = 0
        player1_y_speed = 0
        player2_y_speed = 0       

    # Call score funtions
    show_score1(player1_score_x, player1_score_y)
    show_score2(player2_score_x, player2_score_y)
    
    # Refresh the window
    pygame.display.flip()