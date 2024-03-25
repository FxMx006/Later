import pygame
import heapq

from player import Player


class YellowEnemy:
    def __init__(self, image_path, start_pos, screen, board_coordinates):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = start_pos
        self.start_pos = self.pixel_to_matrix(start_pos)
        self.player_pos = (0, 0)
        self.screen = screen
        self.board_coordinates = board_coordinates.copy()
        self.vel = 1  # Geschwindigkeit des Gegners reduziert
        self.player = Player('assets/player_images/rechts.png', 'assets/player_images/1.png',
                             'assets/player_images/hoch.png', 'assets/player_images/runter.png',
                             'assets/player_images/2.png',
                             (30, 30), 1, screen)
        self.path = self.find_shortest_path()  # Pfad, den der Gegner entlang laufen wird
        self.current_step = 0  # Aktueller Schritt im Pfad

    def draw_enemy(self):
        self.screen.blit(self.image, (round(self.rect.x), round(self.rect.y)))

    def find_shortest_path(self):
        player_pos = self.player.get_position()

        start = self.get_nearest_accessible(self.start_pos)
        target = self.get_nearest_accessible(player_pos)
        open_list = []
        heapq.heappush(open_list, (0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}
        while open_list:
            _, current = heapq.heappop(open_list)
            if current == target:
                break
            for next in self.get_neighbors(current):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(target, next)
                    heapq.heappush(open_list, (priority, next))
                    came_from[next] = current
        if target in came_from:
            return self.reconstruct_path(came_from, target)
        else:
            return []

    def get_neighbors(self, pos):
        x, y = pos
        directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        neighbors = [point for point in directions if
                     0 <= point[0] < len(self.board_coordinates[0]) and 0 <= point[1] < len(self.board_coordinates) and
                     self.board_coordinates[point[1]][point[0]] in {0, 11, 12}]
        return neighbors

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def reconstruct_path(self, came_from, target):
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

    def pixel_to_matrix(self, pos):
        return pos[0] // 30, pos[1] // 30

    def matrix_to_pixel(self, pos):
        return pos[0] * 30, pos[1] * 30

    def get_nearest_accessible(self, pos):
        if self.board_coordinates[pos[1]][pos[0]] in {0, 11, 12}:
            return pos
        for d in range(1, max(len(self.board_coordinates), len(self.board_coordinates[0]))):
            for i in range(-d, d + 1):
                for j in range(-d, d + 1):
                    x, y = pos[0] + i, pos[1] + j
                    if 0 <= x < len(self.board_coordinates[0]) and 0 <= y < len(self.board_coordinates) and \
                            self.board_coordinates[y][x] in {0, 11, 12}:
                        return x, y
        return

    def move(self):
        if self.current_step < len(self.path):
            next_step = self.path[self.current_step]
            next_x, next_y = self.matrix_to_pixel(next_step)
            if self.rect.x < next_x:
                self.rect.x += self.vel
            elif self.rect.x > next_x:
                self.rect.x -= self.vel
            if self.rect.y < next_y:
                self.rect.y += self.vel
            elif self.rect.y > next_y:
                self.rect.y -= self.vel
            if round(self.rect.x) == next_x and round(self.rect.y) == next_y:
                self.current_step += 1
