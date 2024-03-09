#створи гру "Лабіринт"
from typing import Any
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed


class Matematichka(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x < 470:
            self.direction = "right"
        if self.rect.x > 600:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


w1 = Wall(170, 38, 203, 20, 17, 650, 10)
w2 = Wall(170, 38, 203, 18, 456, 10, 311)
w3 = Wall(170, 38, 203, 18, 456, 650, 10)
w4 = Wall(170, 38, 203, 18, 456, 10, 311)
w5 = Wall(170, 38, 203, 18, 73, 101, 10)
w6 = Wall(170, 38, 203, 23, 136, 134, 10)
w7 = Wall(170, 38, 203, 127, 241, 288, 10)
w8 = Wall(170, 38, 203, 127, 327, 407, 10)
w9 = Wall(170, 38, 203, 305, 80, 10, 311)
w10 = Wall(170, 38, 203, 248, 136, 220, 10)
w11 = Wall(170, 38, 203, 544, 185, 120, 14)
w12 = Wall(170, 38, 203, 658, 466, 10, 450)
w13 = Wall(170, 38, 203, 534, 384, 10, 301)

w14 = Wall(170, 38, 203, 468, 136, 10, 63)
w15 = Wall(170, 38, 203, 23, 136, 134, 10)

window = display.set_mode((700, 500))

background = transform.scale(image.load("jpg.jpg"), (700, 500))
game = True
clock = time.Clock()
FPS = 60

player=Player("pujd.png", 100, 250, 15)
Matematichka=Matematichka("logika.png", 400, 250, 10)
monetochka=GameSprite("almaz.png", 50, 250, 0)


finish = False
font.init()
font = font.Font(None, 70)
win = font.render("You Wenigret", True, (255, 215, 0))
lose = font.render("You Loser", True, (180, 0, 0))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

money = mixer.Sound("pukane-4.ogg")
kick = mixer.Sound("kick.ogg")

while game:
    display.update()
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if finish!=True:
            window.blit(background,(0,0))
            player.reset()
            player.update()
            Matematichka.reset()
            Matematichka.update()
            monetochka.reset()

            w1.draw_wall()
            w2.draw_wall()
            w3.draw_wall()
            w4.draw_wall()
            w5.draw_wall()
            w6.draw_wall()
            w7.draw_wall()
            w8.draw_wall()
            w9.draw_wall()
            w10.draw_wall()
            w11.draw_wall()
            w12.draw_wall()
            w13.draw_wall()
            w14.draw_wall()
            w15.draw_wall()

    if  (sprite.collide_rect(player, w1)
        or sprite.collide_rect(player, w2)
        or sprite.collide_rect(player, w3)
        or sprite.collide_rect(player, w4)
        or sprite.collide_rect(player, w5)
        or sprite.collide_rect(player, w6)
        or sprite.collide_rect(player, w7)
        or sprite.collide_rect(player, w8)):
        player.rect.x=50
        player.rect.y=400


    if sprite.collide_rect(player, Matematichka):
        window.blit(lose, (200, 200))
        player.rect.x=50
        player.rect.y=400
        kick.play()
        finish = True

    if sprite.collide_rect(player, monetochka):
        window.blit(win, (200, 200))
        player.rect.x=50
        player.rect.y=400
        kick.play()
        finish = True