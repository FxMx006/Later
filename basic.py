import pygame
import random


class Ghost:
    def __init__(self, image_path, start_pos, velocity, screen):
        self.image = pygame.image.load(image_path)
        self.start_pos = start_pos
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.rect = pygame.Rect(self.x, self.y, 22, 22)
        self.screen = screen
        self.vel = velocity
        self.directions = ['left', 'right', 'up', 'down']
        self.direction = random.choice(self.directions)

    def collision(self, board_coordinates):
        corners = [(self.x // 30, self.y // 30),
                   ((self.x + self.rect.width) // 30, self.y // 30),
                   (self.x // 30, (self.y + self.rect.height) // 30),
                   ((self.x + self.rect.width) // 30, (self.y + self.rect.height) // 30)]
        for corner in corners:
            if board_coordinates[int(corner[1])][int(corner[0])] not in [0, 11, 12]:
                return True
        return False

    def move(self, player, board_coordinates):
        old_x, old_y = self.x, self.y

        best_direction = None
        best_distance = float('inf')

        for direction in self.directions:
            # Versuchen Sie, in diese Richtung zu bewegen
            if direction == 'left':
                self.x -= self.vel
            elif direction == 'right':
                self.x += self.vel
            elif direction == 'up':
                self.y -= self.vel
            elif direction == 'down':
                self.y += self.vel

            # Überprüfen Sie, ob dieser Zug den Geist näher an den Spieler bringt und keinen Zusammenstoß verursacht
            dx, dy = self.x - player.x, self.y - player.y
            new_distance = dx ** 2 + dy ** 2
            if new_distance < best_distance and not self.collision(board_coordinates):
                best_direction = direction
                best_distance = new_distance

            # Rückgängig machen des Zuges
            self.x, self.y = old_x, old_y

        # Wenn wir einen guten Zug gefunden haben, machen wir ihn
        if best_direction is not None:
            self.direction = best_direction
            if self.direction == 'left':
                self.x -= self.vel
            elif self.direction == 'right':
                self.x += self.vel
            elif self.direction == 'up':
                self.y -= self.vel
            elif self.direction == 'down':
                self.y += self.vel

        self.rect.x, self.rect.y = int(self.x), int(self.y)

    def draw_ghost(self):
        ghost_pos = (self.rect.x - self.image.get_width() // 2 + self.rect.width // 2,
                     self.rect.y - self.image.get_height() // 2 + self.rect.height // 2)
        self.screen.blit(self.image, ghost_pos)
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 2)