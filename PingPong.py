from pygame import *
from random import randint

window = display.set_mode((1280,720))
display.set_caption('У всех есть проблемы, но не все с ними борятся')
background = transform.scale(image.load('Пинг-Понг стол.png'), (1280,720))
raketka1 = transform.scale(image.load('551-5514736_ping-pong-racket-png-image-blue-ping-pong.png'), (640,360))
raketka2 = transform.scale(image.load('Raketka1.jpg'), (640,360))

mixer.init()
mixer.music.load('Hoyo-Mix and Yu-Peng Chen - Hanachirusato (dizer.net).mp3')
mixer.music.play()
propysheno = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100,150))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 1275:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 1275:
            self.rect.y += self.speed


class Babel(GameSprite):
    def update(self):
        global lost
        self.rect.x += self.speed
        if self.rect.x == 1280:
            self.rect.x = 0
            propysheno += 1



raketka1 = Player1('551-5514736_ping-pong-racket-png-image-blue-ping-pong.png',1170,520,50)
raketka2 = Player2('Raketka1.jpg',5,520,50)
babel = Babel("Sharik.jpg",640,360,20)
font.init()
font1 = font.Font(None,36)
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        clock = time.Clock()
        FPS = 60
        clock.tick(FPS)
        window.blit(background,(0,0))
        raketka1.update()
        raketka1.reset()
        raketka2.update()
        raketka2.reset()
        babel.update()
        babel.reset()
        if propysheno >= 1:
            text_lose1 = font1.render("wasted",1,(255,255,255))
            window.blit(text_lose1, (250,250))
            finish = True
        display.update()
    time.delay(50)