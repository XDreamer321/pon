from pygame import *
from time import sleep

GREEN = (0, 255, 128)


window = display.set_mode((700,500))
display.set_caption('Птички летят')
back = transform.scale(image.load('bs.jpg'), (700,500))
win = transform.scale(image.load('win.png'), (700,500))
lose = transform.scale(image.load('lose.jpg'), (700,500))
win_width = 700
run = True
class Card (sprite.Sprite):
    def __init__(self, width,height,x,y,color):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
    def draw(self):
        draw.rect(window, self.fill_color, self.rect)
    

class Sp(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Pon(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Sp):
    def __init__(self,picture,w,h,x,y,x_speed,y_speed):
        super().__init__(picture,w,h,x,y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        
        platforms_touched = sprite.spritecollide(self,barriers, False)

        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.right = max(self.rect.left, p.rect.right)

        self.rect.y += self.y_speed
        
        platforms_touched = sprite.spritecollide(self,barriers, False)
        
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet = Bullet('puli.png', 20, 8 , self.rect.right,self.rect.centery, 15)
        bullets.add(bullet                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  )            
class Enemy(Sp):
    def __init__(self,picture,w,h,x,y,speed):
        super().__init__(picture,w,h,x,y)                
        self.speed = speed
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Bullet(Sp):
    def __init__(self,picture,w,h,x,y,speed):
        super().__init__(picture,w,h,x,y)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width + 10:
            self.kill()    





player1 = Card(80,80,100,150,GREEN)
player2 = Enemy('dis.png',60,60,445,150, 3)
player3 = Enemy('dis.png',60,60,445,400, 3)
player = Player('dimon.png', 120,130,130, 300, 0,0)
wall1 = Pon('wall1.png', 300,60, 150, 150)
wall2 = Pon('wall2.png', 60,300, 390, 210)
final = Sp('final.png', 80, 80, 530, 400 )
stena1 = Pon('wall2.png', 1,500, 0, 0)
stena2 = Pon('wall2.png', 1,500, 700, 0)
stena3 = Pon('wall1.png', 700,1, 0, 0)
stena4 = Pon('wall1.png', 700,1, 0, 500)

barriers = sprite.Group()
barriers.add(wall1)
barriers.add(wall2)
barriers.add(stena1)
barriers.add(stena2)
barriers.add(stena3)
barriers.add(stena4)
bullets = sprite.Group()
enemys = sprite.Group()
enemys.add(player2)
enemys.add(player3)

pobeda = True
pomer = False        
while run:
    time.delay(50)

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                player.y_speed = -7 
            if e.key == K_DOWN:
                player.y_speed = 7 
            if e.key == K_LEFT:
                player.x_speed = -7
            if e.key == K_RIGHT:
                player.x_speed = 7
            if e.key == K_w:
                player.y_speed = -7
            if e.key == K_s:
                player.y_speed = 7
            if e.key == K_a:
                player.x_speed = -7 
            if e.key == K_d:
                player.x_speed = 7 
            elif e.key == K_SPACE:
                player.fire()          



            
        elif e.type == KEYUP:
            if e.key == K_UP:
                player.y_speed = 0
            if e.key == K_DOWN:
                player.y_speed = 0 
            if e.key == K_LEFT:
                player.x_speed = 0
            if e.key == K_RIGHT:
                player.x_speed = 0
            if e.key == K_w:
                player.y_speed = 0 
            if e.key == K_s:
                player.y_speed = 0 
            if e.key == K_a:
                player.x_speed = 0 
            if e.key == K_d:
                player.x_speed = 0   
            
    
    if pobeda != False:
          

        window.blit(back, (0,0))
        
        enemys.draw(window)
        enemys.update()
        player.reset()
        player.update()
        barriers.draw(window)
        final.reset()
        bullets.draw(window)
        bullets.update()




        sprite.groupcollide(bullets, barriers, True, False)
        sprite.groupcollide(bullets, enemys, True, True)
        if sprite.collide_rect(player, final ):
            pobeda = False
            window.blit(win,(0,0))
        if sprite.spritecollide(player, enemys, False ):
            
            pobeda = True
            window.blit(lose,(0,0))

    display.update() 