# pygame-example-shmup.py
# Shoot 'em up

import random

import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 720
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)

MISSILE = pg.image.load("./Images/missile.svg")
MISSILE = pg.transform.scale(MISSILE, (MISSILE.get_width() // 100, MISSILE.get_height() // 100))
MISSILE = pg.transform.rotate(MISSILE, -90)

NUM_ENEMIES = 1



# TODO: Player class
#      - Limit player position to the bottom
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/f15.webp")
        self.image = pg.transform.scale(self.image, (self.image.get_width() // 10, self.image.get_height() // 10))
        self.image = pg.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect()

    def update(self):
        """Follow the mouse"""
        self.rect.center = pg.mouse.get_pos()
        print(pg.mouse.get_pos())
        print(self.rect.center)

        # Keep it at the bottom of the screen
        if self.rect.top < HEIGHT - 200:
            self.rect.top = HEIGHT - 200


# TODO: Bullets/lasers
#      - Image - picture or pygame surface?
#      - Spawn at the Player
#      - Vertical velocity

class Bullet(pg.sprite.Sprite):
    def __init__(self, player_loc: list):
        """

        Params:
            player_loc: x,y coords of centerx and top """
        
        super().__init__()

        self.image = MISSILE

        self.rect = self.image.get_rect()


        self.rect.centerx = player_loc[0]

        self.rect.bottom = player_loc[1]

        self.vel = -2

    def update(self):
        self.rect.y += self.vel

        if self.rect.bottom < 0:
            self.kill()


        



# TODO: Enemies
#      - Move left to right to left

class Enemy(pg.sprite.Sprite):
    def __init__(self, centerx: int, centery: int):
        """
        Params:
            centerx: center x spawn of the enemy
            centery: center y spawn of the enemy
        """
        super().__init__()

        self.image = pg.image.load("./Images/su27.png")
        self.image = pg.transform.scale(self.image, (self.image.get_width() // 5, self.image.get_height() // 5))
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = centerx, centery

        self.vel_x = 4
        self.vel_y = 2

    def update(self):
        # Movement
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Bounce in the x-axis
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.vel_x *= -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel_x *= -1

def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    bullet_sprites = pg.sprite.Group()
    enemy_sprites = pg.sprite.Group()

    # Create the Player sprite object
    player = Player()

    all_sprites.add(player)

    # Create and spawn all enemies randomly in y
    for _ in range(NUM_ENEMIES):
        enemy = Enemy(
            random.randrange(20, WIDTH - 20), random.randrange(20, HEIGHT - 400)
        )
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)

    pg.display.set_caption("Shoot 'Em Up")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                bullet = Bullet((player.rect.centerx, player.rect.top))
                all_sprites.add(bullet)
                bullet_sprites.add(bullet)

        # --- Update the world state
        all_sprites.update()

        # Collision between bullets and enemies
        for bullet in bullet_sprites:
            enemies_hit = pg.sprite.spritecollide(bullet, enemy_sprites, False)

            for enemy in enemies_hit:
                enemy.kill()
                bullet.kill()

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps

    pg.quit()


def main():
    start()


if __name__ == "__main__":
    main()