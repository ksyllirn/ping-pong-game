from pygame import * 
from button import Button
 
class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
    
    
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
    
 
class Player(GameSprite): 
    def update_r(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < win_height - 80: 
            self.rect.y += self.speed 
    def update_l(self): 
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < win_height - 80: 
            self.rect.y += self.speed 
    
 
back = (60, 67, 252)
win_width = 600 
win_height = 500 
window = display.set_mode((win_width, win_height)) 
window.fill(back) 
 
 
#флаги, отвечающие за состояние игры 
game = True 
finish = False 
clock = time.Clock() 
FPS = 60 
 
 
#создания мяча и ракетки    
racket1 = Player('racket.png', 30, 200, 4, 50, 150)  
racket2 = Player('racket.png', 520, 200, 4, 50, 150) 
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)


font.init() 
font = font.Font(None, 35) 
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0)) 
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0)) 


btn_start = Button(y=150, width=150, height=40, text="начать игру", font_size=24)
btn_credits = Button(y=210, width=150, height=40, text="об авторе", font_size=24)
btn_exit = Button(y=270, width=150, height=40, text="выход", font_size=24)
btn_restart = Button(y=250, width=150, height=40, text="перезапуск", font_size=24) 
btn_continue = Button(y=220, width=150, height=40, text="продолжить", font_size=24)
btn_exit_inpause = Button(y=280, width=150, height=40, text="выйти в меню", font_size=24) 
 
speed_x = 3 
speed_y = 3 

def game_run():
    global speed_x
    global speed_y 
    window.fill(back) 
    racket1.update_l() 
    racket2.update_r() 
    ball.rect.x += speed_x 
    ball.rect.y += speed_y 


    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball): 
        speed_x *= -1 
        speed_y *= 1 
    
    #если мяч достигает границ экрана, меняем направление его движения 
    if ball.rect.y > win_height-50 or ball.rect.y < 0: 
        speed_y *= -1 


    #если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока 
    if ball.rect.x < 0: 
        window.blit(lose1, (200, 200))



    #если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока 
    if ball.rect.x > win_width: 
        window.blit(lose2, (200, 200)) 


    racket1.reset() 
    racket2.reset() 
    ball.reset() 

stage = 'menu'
def menu(events):
    global stage

    window.fill(back)

    btn_start.update(events)
    btn_credits.update(events)
    btn_exit.update(events)

    btn_start.draw(window)
    btn_credits.draw(window)
    btn_exit.draw(window)

    if btn_start.is_clicked(events):
        stage = 'game'
    if btn_exit.is_clicked(events):
        stage = 'off'

def pause(events):
    global stage

    window.fill(back)

    btn_exit_inpause.update(events)
    btn_continue.update(events)

    btn_exit_inpause.draw(window)
    btn_continue.draw(window)

    if btn_exit_inpause.is_clicked(events):
        stage = 'menu'
    if btn_continue.is_clicked(events):
        stage = 'game'
    
while stage != 'off':
    events = event.get() 
    for e in events: 
        if e.type == QUIT: 
            stage = 'off'
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                stage = 'pause'

    if stage == 'menu':
        menu(events)
    if stage == 'game':
        game_run()
    if stage == 'pause':
        pause(events)

    display.update() 
    clock.tick(FPS)
