from pygame import * 

win_width = 600
win_height = 500
win = display.set_mode((win_width, win_height))
background = (200, 255, 255)
win.fill(background)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

platform1 = Player('racket.png', 30, 200, 4, 50, 150)
platform2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

clock = time.Clock()
game = True
fps = 60
finish = False
speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        win.fill(background)
        platform1.update_l()
        platform2.update_r()

        platform1.reset()
        platform2.reset()
        ball.reset()

    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(platform1, ball) or sprite.collide_rect(platform2, ball):
        speed_x *= -1    

    if ball.rect.x < 0:
        finish = True
        win.blit(lose1, (200, 200))

    if ball.rect.x > win_width:
        finish = True
        win.blit(lose2, (200, 200))

    display.update()
    clock.tick(fps)
