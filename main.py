import os
import sys
import pygame

from map import board_coordinates, draw_map
from player import Player
from yellow_enemy import YellowEnemy


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((720, 720))
    pygame.display.set_caption("Pacman")

    # Initialisierung von Player und YellowEnemy (Gegner)
    player = Player('assets/player_images/rechts.png', 'assets/player_images/1.png',
                    'assets/player_images/hoch.png', 'assets/player_images/runter.png',
                    'assets/player_images/2.png',
                    (30, 30), 1, screen)

    yellow_enemy = YellowEnemy('assets/player_images/orange.png', (278, 278),
                               screen, board_coordinates)

    running = True
    while running:
        clock.tick(80)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                pygame.quit()
                os.execv(sys.executable, ['python'] + sys.argv)

        # Spiellogik-Update und Rendering
        if player.check_collision(yellow_enemy):
            print("Game Over")
            break

        screen.fill((0, 0, 0))  # Bildschirm leeren

        draw_map(screen)  # Spielfeld zeichnen

        player.draw_player()  # Spieler zeichnen
        player.move(board_coordinates)  # Siedlerbewegung aktualisieren
        player.collect_point(board_coordinates)  # Punkte einsammeln

        yellow_enemy.player_pos = player.get_position()  # Aktualisiere die Position des Spielers
        yellow_enemy.find_shortest_path()  # Berechne den kürzesten Pfad zum Spieler
        yellow_enemy.move()
        yellow_enemy.draw_enemy()

        pygame.display.flip()  # Bildschirm aktualisieren

    pygame.quit()


if __name__ == "__main__":
    main()
