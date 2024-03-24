import os
import sys
import pygame

from map import board_coordinates
from map import draw_map
from player import Player
from yellow_enemy import Ghost


def main():
    pygame.init()
    screen = pygame.display.set_mode((720, 720))
    pygame.display.set_caption("Pacman")

    player = Player('assets/player_images/rechts.png', 'assets/player_images/1.png',
                    'assets/player_images/hoch.png', 'assets/player_images/runter.png',
                    'assets/player_images/2.png',
                    (30, 30), 0.3, screen)

    yellow_enemy = Ghost('assets/player_images/orange.png', (278, 278), 0.2, screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                pygame.quit()
                os.execv(sys.executable, ['python'] + sys.argv)

        if player.check_collision(yellow_enemy):
            print("Game Over")
            break
        screen.fill((0, 0, 0))
        draw_map(screen)

        player.draw_player()
        player.move(board_coordinates)
        player.collect_point(board_coordinates)
        yellow_enemy.move(player, board_coordinates)  # Pass both the player object and board_coordinates
        yellow_enemy.draw_ghost()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
