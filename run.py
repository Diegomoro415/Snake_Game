# import libraries
import random
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


# Define the function to start the game loop
def game_loop():
    """
    The main game loop that handles game logic and updates the display.
    """
    # Initialize the snake's position and movement
    lead_x = round(screen_width / 2 / 10.0) * 10.0
    lead_y = round(screen_height / 2 / 10.0) * 10.0
    lead_x_change = 0
    lead_y_change = 0
    snake_list = []
    snake_length = 1
    # Initialize the food's position
    food_x = round(random.randrange(0, screen_width - block_size) / 10) * 10
    food_y = round(random.randrange(0, screen_height - block_size) / 10) * 10

    
    # Start the game loop
    game_over = False
    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
        # Move the snake's head
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Fill the background
        screen.fill((0, 40, 0))
        # Check for collision with the walls
        if lead_x < 0 or lead_x >= screen_width or lead_y < 0 or lead_y >= screen_height:
            game_over = True
        # Draw the food
        pygame.draw.rect(screen, (255, 0, 0), [food_x, food_y, block_size,
                                        block_size])
        # Update the snake's body
        snake_head = [lead_x, lead_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        # Check for collision with the snake's body
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True
        # Draw the snake
        draw_snake(snake_list)

        # Update the snake's length and food's position if there's a collision
        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0,
                        screen_width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0,
                        screen_height - block_size) / 10.0) * 10.0
            snake_length += 1

        # Update the display
        pygame.display.update()
        # Set the game's frame rate
        clock.tick(15)

# Wait for user to press a key
wait_key = True
while wait_key:
    for event_press in pygame.event.get():
        if event_press.type == pygame.QUIT:
            pygame.quit()
        if event_press.type == pygame.KEYDOWN:
            wait_key = False
            game_loop()
    # Clean the screen
    screen.fill((255, 255, 255))
