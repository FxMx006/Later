import pygame

board_coordinates = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 8, 0, 9, 8, 0, 9, 1, 5, 0, 9, 1, 8, 0, 4, 1, 8, 0, 9, 1, 8, 0, 9, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 9, 1, 8, 0, 9, 1, 1, 3, 0, 1, 0, 2, 1, 1, 8, 0, 9, 1, 1, 8, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 9, 1, 3, 0, 9, 8, 0, 0, 0, 11, 0, 0, 0, 9, 1, 8, 0, 2, 1, 8, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 2, 3, 0, 2, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 6, 0, 1, 0, 6, 0, 9, 1, 5, 0, 4, 1, 1, 8, 0, 6, 0, 1, 0, 6, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 7, 0, 7, 0, 1, 0, 2, 1, 8, 0, 0, 9, 1, 3, 0, 1, 0, 7, 0, 7, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 9, 1, 8, 0, 7, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 7, 0, 9, 1, 8, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 1, 1, 1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 9, 3, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 3, 0, 2, 8, 0, 1],
    [1, 0, 0, 7, 0, 7, 0, 7, 0, 9, 1, 1, 1, 1, 8, 0, 7, 0, 7, 0, 7, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 1, 8, 0, 6, 0, 6, 0, 0, 0, 0, 0, 0, 6, 0, 6, 0, 2, 1, 3, 0, 1],
    [1, 0, 7, 0, 0, 0, 1, 0, 4, 1, 1, 1, 1, 1, 1, 5, 0, 1, 0, 1, 0, 7, 0, 1],
    [1, 0, 0, 0, 9, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 7, 0, 0, 0, 1],
    [1, 0, 6, 0, 0, 0, 7, 0, 9, 8, 0, 2, 3, 0, 9, 8, 0, 7, 0, 0, 0, 6, 0, 1],
    [1, 0, 4, 1, 8, 0, 0, 0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 0, 0, 9, 1, 5, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 1, 1, 3, 0, 0, 0, 0, 2, 1, 1, 3, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]






def draw_map(screen):
    """
    this function draws the blocks for each number, so we have in the end a
    whole map to play on
    """
    color_walls = (30, 0, 75)
    color_points = (255, 255, 255)
    small_circle_radius = 4.5
    big_circle_radius = 9

    screen_width, screen_height = pygame.display.get_surface().get_size()

    # Set the number of rows and columns to fit 30 pixel blocks
    num_rows = screen_height // 30
    num_cols = screen_width // 30

    rect_width = 30
    rect_height = 30

    rect_radius = min(rect_width, rect_height) // 2

    for row in range(num_rows):
        for col in range(num_cols):
            rect_x = col * rect_width
            rect_y = row * rect_height
            rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

            if board_coordinates[row][col] == 0:
                pygame.draw.circle(screen, color_points,
                                   (col * rect_width + rect_width // 2, row * rect_height + rect_height // 2),
                                   small_circle_radius)

            elif board_coordinates[row][col] == 1:
                pygame.draw.rect(screen, color_walls, rect)

            elif board_coordinates[row][col] == 2:
                pygame.draw.rect(screen, color_walls, rect, border_radius=rect_radius, border_bottom_left_radius=0,
                                 border_bottom_right_radius=0, border_top_right_radius=0)

            elif board_coordinates[row][col] == 3:
                pygame.draw.rect(screen, color_walls, rect, border_radius=rect_radius, border_bottom_left_radius=0,
                                 border_bottom_right_radius=0, border_top_left_radius=0)

            elif board_coordinates[row][col] == 4:
                pygame.draw.rect(screen, color_walls, rect, border_radius=rect_radius, border_top_right_radius=0,
                                 border_bottom_right_radius=0, border_top_left_radius=0)

            elif board_coordinates[row][col] == 5:
                pygame.draw.rect(screen, color_walls, rect, border_radius=rect_radius, border_top_right_radius=0,
                                 border_bottom_left_radius=0, border_top_left_radius=0)

            elif board_coordinates[row][col] == 6:
                pygame.draw.rect(screen, color_walls, rect, border_radius=rect_radius, border_bottom_left_radius=0,
                                 border_bottom_right_radius=0)

            elif board_coordinates[row][col] == 7:
                pygame.draw.rect(screen, color_walls, rect, border_radius=rect_radius, border_top_right_radius=0,
                                 border_top_left_radius=0)

            elif board_coordinates[row][col] == 8:
                pygame.draw.rect(screen, color_walls, rect, border_radius=rect_radius, border_top_left_radius=0,
                                 border_bottom_left_radius=0)

            elif board_coordinates[row][col] == 9:
                pygame.draw.rect(screen, color_walls, rect, border_radius=rect_radius, border_bottom_right_radius=0,
                                 border_top_right_radius=0)

            elif board_coordinates[row][col] == 10:
                pygame.draw.rect(screen, color_walls, rect, border_radius=rect_radius)

            elif board_coordinates[row][col] == 11:
                pygame.draw.circle(screen, color_points,
                                   (col * rect_width + rect_width // 2, row * rect_height + rect_height // 2),
                                   big_circle_radius)

            elif board_coordinates[row][col] == 12:
                pass
