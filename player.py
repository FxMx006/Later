import pygame
import time
import sys


class Player:
    def __init__(self, image_path1, image_path2, image_path3, image_path4, image_path5, start_pos, velocity, screen):
        self.original_image = {
            'up': [pygame.image.load(image_path3), pygame.image.load(image_path2)],
            'down': [pygame.image.load(image_path4), pygame.image.load(image_path2)],
            'left': [pygame.image.load(image_path5), pygame.image.load(image_path2)],
            'right': [pygame.image.load(image_path1), pygame.image.load(image_path2)],
        }
        self.image_index = 0
        self.image = self.original_image['right'][self.image_index]
        self.start_pos = start_pos
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.rect = pygame.Rect(self.x, self.y, 22, 22)
        self.screen = screen
        self.last_valid_move = {'left': False, 'right': False, 'up': False, 'down': False}
        self.vel = velocity
        self.moving = {'left': False, 'right': False, 'up': False, 'down': False}
        self.last_switch_time = time.time()
        self.lives = 3

    def collision(self, board_coordinates):
        corners = [(self.x // 30, self.y // 30),
                   ((self.x + self.rect.width) // 30, self.y // 30),
                   (self.x // 30, (self.y + self.rect.height) // 30),
                   ((self.x + self.rect.width) // 30, (self.y + self.rect.height) // 30)]
        for corner in corners:
            if board_coordinates[int(corner[1])][int(corner[0])] not in [0, 11, 12]:

                return True
        return False

    def check_collision(self, ghost):
        if self.rect.colliderect(ghost.rect):
            self.lives -= 1  # Decrease the number of lives by 1
            self.x, self.y = self.start_pos  # Reset the player's position
            ghost.x, ghost.y = ghost.start_pos  # Reset the ghost's position
            if self.lives == 0:
                self.game_over()  # End the game if the player has no lives left
                return True
        return False

    def game_over(self):
        pygame.quit()
        sys.exit("Spiel vorbei")

    def move(self, board_coordinates):
        old_x, old_y = self.x, self.y
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.moving = {'left': True, 'right': False, 'up': False, 'down': False}
            self.image = self.original_image['left'][self.image_index]
        if keys[pygame.K_RIGHT]:
            self.moving = {'left': False, 'right': True, 'up': False, 'down': False}
            self.image = self.original_image['right'][self.image_index]
        if keys[pygame.K_UP]:
            self.moving = {'left': False, 'right': False, 'up': True, 'down': False}
            self.image = self.original_image['up'][self.image_index]
        if keys[pygame.K_DOWN]:
            self.moving = {'left': False, 'right': False, 'up': False, 'down': True}
            self.image = self.original_image['down'][self.image_index]

        if self.moving['left']:
            self.x -= self.vel
        if self.moving['right']:
            self.x += self.vel
        if self.moving['up']:
            self.y -= self.vel
        if self.moving['down']:
            self.y += self.vel

        if self.collision(board_coordinates):
            self.x, self.y = old_x, old_y
            self.moving = self.last_valid_move
        else:
            self.last_valid_move = self.moving.copy()

        if time.time() - self.last_switch_time > 0.2:
            direction = self.get_direction()
            self.image_index = (self.image_index + 1) % len(self.original_image[direction])
            self.image = self.original_image[direction][self.image_index]
            self.last_switch_time = time.time()

        self.rect.x, self.rect.y = int(self.x), int(self.y)

    def draw_player(self):
        player_pos = (self.rect.x - self.image.get_width() // 2 + self.rect.width // 2,
                      self.rect.y - self.image.get_height() // 2 + self.rect.height // 2)
        self.screen.blit(self.image, player_pos)
        pygame.draw.rect(self.screen, (0, 255, 0), self.rect, 2)

    def get_direction(self):
        for direction, moving in self.moving.items():
            if moving:
                return direction
        return 'right'

    def get_position(self):
        board_x = int((self.x - 30) // 30)
        board_y = int((self.y - 30) // 30)
        return board_x, board_y

    def collect_point(self, board_coordinates):
        board_x, board_y = self.get_position()

        if board_coordinates[board_y][board_x] == 0:
            board_coordinates[board_y][board_x] = -1

    def collect_point(self, board_coordinates):
        board_x, board_y = self.get_position()

        if board_coordinates[board_y+1][board_x+1] == 0:
            board_coordinates[board_y+1][board_x+1] = 12
