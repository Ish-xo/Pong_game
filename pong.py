import pygame
import random

# Initialize the game
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 10

# Create the window
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Define the paddles and ball
player1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x, ball_speed_y = random.choice((1, -1)) * 5, random.choice((1, -1)) * 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.move_ip(0, -5)
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.move_ip(0, 5)
    if keys[pygame.K_UP] and player2.top > 0:
        player2.move_ip(0, -5)
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.move_ip(0, 5)

    # Move the ball
    ball.move_ip(ball_speed_x, ball_speed_y)

    # Bounce the ball off the top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Bounce the ball off the paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x = -ball_speed_x

    # Reset ball if it goes off screen
    if ball.left <= 0 or ball.right >= WIDTH:
        ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

    # Fill the background
    display.fill(BLACK)

    # Draw the paddles and ball
    pygame.draw.rect(display, WHITE, player1)
    pygame.draw.rect(display, WHITE, player2)
    pygame.draw.ellipse(display, WHITE, ball)

    # Update the display
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()