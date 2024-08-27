"""
12-6. Sideways Shooter: Write a game that places a ship on the left side of the
screen and allows the player to move the ship up and down. Make the ship fire
a bullet that travels right across the screen when the player presses the spacebar. 
Make sure bullets are deleted once they disappear off the screen.
"""

import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sideways Shooter")

# Set colors
bg_color = (30, 30, 30)  # Dark background color
bullet_color = (255, 255, 0)  # Yellow bullets

# Load ship image
# Replace with your image path
ship_image = pygame.image.load(
    "Python_Crash_Course_files\Chapter12_MakingShipThatFires\Task_12_2_GameCharacter\ship.bmp")
ship_rect = ship_image.get_rect()
ship_rect.left = 20  # Position the ship on the left side of the screen
ship_rect.centery = screen_height // 2

# Bullet settings
bullets = []
bullet_speed = 10

# Ship movement
ship_speed = 5
moving_up = False
moving_down = False

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
            elif event.key == pygame.K_SPACE:
                # Create a bullet and add it to the list
                bullet_rect = pygame.Rect(0, 0, 10, 4)
                bullet_rect.midleft = ship_rect.midright
                bullets.append(bullet_rect)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False

    # Move the ship
    if moving_up and ship_rect.top > 0:
        ship_rect.y -= ship_speed
    if moving_down and ship_rect.bottom < screen_height:
        ship_rect.y += ship_speed

    # Move bullets
    for bullet in bullets:
        bullet.x += bullet_speed

    # Remove bullets that are off the screen
    bullets = [bullet for bullet in bullets if bullet.right < screen_width]

    # Draw everything
    screen.fill(bg_color)
    screen.blit(ship_image, ship_rect)
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, bullet)

    # Update the screen
    pygame.display.flip()
    clock.tick(60)  # Maintain 60 FPS
