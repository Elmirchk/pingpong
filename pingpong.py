from pygame import *

font.init()
font1 = font.Font(None, 80)
win1 = font1.render('Player-1 WIN!', True, (255, 255, 255))
lose1 = font1.render('Player-1 LOSE!', True, (180, 0, 0))
win2 = font1.render('Player-2 WIN!', True, (255, 255, 255))
lose2 = font1.render('Player-2 LOSE!', True, (180, 0, 0))

font2 = font.Font(None, 36)

back = 'фон.jpg'
ballpng = 'мяч.png'
rocketki = 'ракетка.png'

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y :
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y :
            self.rect.y += self.speed


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-понг")
background = transform.scale(image.load(back), (700, 500))
player1 = Player(rocketki, win_width - 600, 90, 50, 300, 4)
player2 = Player(rocketki, win_width - 150, 90, 50, 300, 4)
ball = GameSprite(ballpng, 350, 0, 50, 50, 2)


finish = False
run = True
FPS = 60
clock = time.Clock()

dx = 2
dy = 2

score1 = 0
score2 = 0
goal = 10

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background, (0,0))

        player1.update2()
        player2.update()

        player1.reset()
        player2.reset()
        ball.reset()

        if sprite.collide_rect(ball, player1):
            score1 += 1
        if sprite.collide_rect(ball, player2):
            score2 += 1

        if score1 == goal:
            finish == True
            window.blit(win1, (150, 200))
        if score2 == goal:
            finish == True
            window.blit(win2, (150, 200))

        text = font2.render("1 Счет: " + str(score1), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        text = font2.render("2 Счет: " + str(score2), 1, (255, 255, 255))
        window.blit(text, (590, 20))

        if ball.rect.x < win_width - 700:
            finish = True
            window.blit(lose1, (150, 200))
        if ball.rect.x > win_width - 100:
            finish = True
            window.blit(lose2, (150, 200))
        
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            dy += -1

        ball.rect.x += dx
        ball.rect.y += dy

        if sprite.collide_rect(ball, player1):
            dx *= -1
        if sprite.collide_rect(ball, player2):
            dx *= -1

        display.update()
        clock.tick(FPS)