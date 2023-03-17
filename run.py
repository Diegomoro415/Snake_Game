# pylint: disable=E1101
# import libraries
import random
import pygame
from login import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope of the API access and credentials for authentication
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'service_account.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('snakegame_ws').sheet1

class Game():
    """
    A class for configuring the Snake game using Pygame.

    Attributes:
    -----------
    None

    Methods:
    --------
    run_game():
        Configures the game window, loads an image for the initial screen
        of the game, and displays the image on the screen.

    """
    #Initial the snake game in pygame
    def game_init(self):
        """
        Configures the Snake game using Pygame.

        Initializes Pygame, creates the game window, loads an image for the
        initial screen of the game, and displays the image on the screen.
        """
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
        # Create a font object for displaying the score
        display_font = pygame.font.SysFont(None, 30)

        # Create the Pygame screen and clock
        clock = pygame.time.Clock()

        # Load the image for the initial screen
        image = pygame.image.load('image/init_screen.png')

        # Set the position of the image on the screen
        image_rect = image.get_rect()
        image_rect.centerx = screen.get_rect().centerx
        image_rect.centery = screen.get_rect().centery

        # Draw the image on the screen
        screen.blit(image, image_rect)

        # Update the screen to show the image
        pygame.display.flip()

        # Define the function to display the game over screen
        def game_over_screen():
            """
            Displays the game over for few seconds
            """
            game_over_image = pygame.image.load('image/gameover2.png')
            # Set the position of the GIF image on the screen
            game_over_image_rect = image.get_rect()
            game_over_image_rect.centerx = screen.get_rect().centerx
            game_over_image_rect.centery = screen.get_rect().centery
            screen.blit(game_over_image, game_over_image_rect)
            pygame.display.update()
            pygame.time.delay(500)

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
            food_x = round(random.randrange(0,
                           screen_width - block_size) / 10) * 10
            food_y = round(random.randrange(0,
                           screen_height - block_size) / 10) * 10
            # Initialize the game over flag
            score = 0
            record_cell = wks.cell(2, 4)
            record = int(record_cell.value) if record_cell.value else 0
            current_score = wks.cell(2, 3)
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
                # Render the score on the screen
                score_text = display_font.render(f"Score: {score}", True, (255,
                                                                        255, 255))
                score_rect = score_text.get_rect()
                score_rect.topleft = (500 - 125, 15)
                screen.blit(score_text, score_rect)
                #Render the Record on the Screen
                record_text = display_font.render(f"Record: {record}", True, (255,
                                                                        255, 255))
                record_rect = record_text.get_rect()
                record_rect.topright = (120, 15)
                screen.blit(record_text, record_rect)
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
                    # Initializing variables for score
                    score += 1
                    current_score.value = score
                    wks.update_cell(current_score.row, current_score.col, current_score.value)
                    if score >= record:
                        record = score
                        wks.update_cell(2, 4, record)
                # Update the display
                pygame.display.update()
                # Set the game's frame rate
                clock.tick(15)
            # Display the game over screen and wait for a few seconds
            while True:
                for event in pygame.event.get(game_over_screen()):
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_n:
                            pygame.quit()
                        if event.key == pygame.K_y:
                            game_loop()

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

if __name__ == "__main__":
    root = tk.Tk()
    login_window = Login(root)
    login_window.mainloop()