import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("crappy clicker")
clock = pygame.time.Clock()

# 1. Define the box (x_pos, y_pos, width, height)
box_rect = pygame.Rect(300, 250, 200, 100)
box_color = (0, 0, 255) # Start blue
count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # 2. Check for the mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left click
                
                # 3. Check if the click position is inside the box
                if box_rect.collidepoint(event.pos):
                    count = count + 5
                    print(f"Box clicked! {count}")
                    box_color = (0, 255, 0) # Change color to green on click

    # Drawing everything
    screen.fill((255, 255, 255)) # White background
    pygame.draw.rect(screen, box_color, box_rect) # Draw the box
    
    pygame.display.flip()
    clock.tick(60)
