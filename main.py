import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    pygame.display.set_caption("Asteroids Game")
    pygame.mouse.set_visible(False)
    pygame.font.init()
    # Load a font for displaying the score
    font = pygame.font.SysFont("comicsans", 30, True)

    # Main game loop

    while True:

        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        # Draw the score on the screen
        score_text = font.render(f"Score: {player.score}", True, "white")
        live_test = font.render(f"Lives: {player.lives}", True, "white")
        screen.blit(live_test, (10, 40))
        screen.blit(score_text, (10, 10))

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over")
                sys.exit()
    
            for bullet in shots:
                if bullet.check_collision(asteroid):
                    asteroid.kill()
                    player.score += 1
                    player.shoot_fired += 1
                    asteroid.split()
                    bullet.kill()                

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()