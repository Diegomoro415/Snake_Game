# import libraries
import pygame 

# Initialize Pygame
pygame.init()

# Define the width and height of the game window
screen_width = 500
screen_height = 500
# Define the size of each block in the game
block_size = 10

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SnakeGame")

# Create the Pygame screen and clock
clock = pygame.time.Clock()
# Update the screen to show the image
pygame.display.flip()

# Define the function to draw the snake
def draw_snake(snake_list):
    """
    Draw the snake on the screen.
    Args:
        snake_list (list):
        A list of tuples representing the coordinates of segment of the snake.
    """
    for x, y in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), [x, y, block_size, block_size])

# Wait for user to press a key
wait_key = True
while wait_key:
    for event_press in pygame.event.get():
        if event_press.type == pygame.QUIT:
            pygame.quit()
        if event_press.type == pygame.KEYDOWN:
            wait_key = False
    # Clean the screen
    screen.fill((255, 255, 255))
