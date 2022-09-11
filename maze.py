from pygame import *
# import pugame_menu

mixer.init()
font.init()
init()

#створи вікно гри
WIDTH = 1000
HEIGHT = 800
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Moze")


mixer.music.load("rok.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(loops = -1)        


win_sound = mixer.Sound("money.ogg")
kick_sound = mixer.Sound("kick.ogg")



font1 = font.SysFont("Impact",50)
font2 = font.SysFont("Impact",50)

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height):
        super().__init__()
        self.img = transform.scale(image.load(image_name),(width,height))
        self.rect = self.img.get_rect()
        self.rect.x = x 
        self.rect.y = y 
    
    def draw(self):
        window.blit(self.img, self.rect)

class Wall(sprite.Sprite):
    def __init__(self,x, y, width, height, color = (255, 113, 33)):
        super().__init__()
        self.img = Surface((width, height))
        self.rect = self.img.get_rect()
        self.img.fill(color)
        self.rect.x = x 
        self.rect.y = y 
        self.width = width
        self.height = height
    def draw(self):
        window.blit(self.img, self.rect)

class Treasure(GameSprite):
    def __init__(self):
        super().__init__("treasure.png" , WIDTH-120, HEIGHT-100, 50, 50)

bg_image = transform.scale(image.load("background.jpg"),(WIDTH, HEIGHT))

player = GameSprite("hero.png" , 0, 80, 60, 60)
treasure = GameSprite("treasure.png" , 880, 720, 80, 80)

cyborg = GameSprite("cyborg.png" , 930, 300, 60, 60)
cyborg1 = GameSprite("cyborg.png" , 930, 600, 60, 60)
cyborg2 = GameSprite("cyborg.png" , 810, 130, 60, 60)
cyborg3 = GameSprite("cyborg.png" , 800, 450, 60, 60)


wall1 = Wall(0,50,100,10)
wall2 = Wall(0,150,100,10)
wall3 = Wall(100,0,700,10)
wall4 = Wall(100,790,700,10)
wall5 = Wall(100,150,10,650)
wall6 = Wall(100,0,10,60)
wall7 = Wall(800,0,10,50) 
wall8 = Wall(800,150,10,570)
wall9 = Wall(200,0,10,700)
wall10 = Wall(200,700,200,10)
wall11 = Wall(300,550,10,150)
wall12 = Wall(200,350,150,10)
wall13 = Wall(300,200,150,10)
wall14 = Wall(300,450,150,10) 
wall15 = Wall(450,200,10,350)
wall16 = Wall(600,600,10,200)
wall17 = Wall(600,600,100,10)
wall18 = Wall(700,500,10,200)
wall19 = Wall(450,350,350,10)
wall20 = Wall(600,350,10,150)
wall21 = Wall(600,0,10,200) 
wall22 = Wall(600,200,100,10) 
wall23 = Wall(800,700,10,100) 
walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20, wall21, wall22]

bot = True
bot1 = True
bot2 = True
bot3 = True
clock = time.Clock()
FPS = 60
speed = 4
speed_2 = 3
roz = 250,310
hard = 0
res = False
result_ = 380,200
run = True

finish = False
# def start_game():
#     global ran
#     ran = True
#     menu.disable()


# menu = pygame_menu.Menu("Лабіринт",400,300, theme = pugame_menu.themeі.THEME_BLUE)
# menu.add.button("Грати", start_game)
# menu.add.button("Вихід",pugame_menu,events) 

# menu.minloop(window)

while run:
    
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                menu.enable()
                menu.mainloop(window)

    if finish == True:
        keys = key.get_pressed()
        restart = font2.render("Для рестарту натисніть R", True, (255,5,5))
        if keys[K_r]:
            player = GameSprite("hero.png" , 0, 80, 60, 60)
            treasure = GameSprite("treasure.png" , 880, 720, 80, 80)
            cyborg = GameSprite("cyborg.png" , 850, 300, 60, 60)
            cyborg1 = GameSprite("cyborg.png" , 900, 600, 60, 60)
            cyborg2 = GameSprite("cyborg.png" , 810, 130, 60, 60)
            cyborg3 = GameSprite("cyborg.png" , 870, 450, 60, 60)
            finish = False
        elif res == True and MOUSEBUTTONDOWN:
            player = GameSprite("hero.png" , 0, 80, 60, 60)
            treasure = GameSprite("treasure.png" , 880, 720, 80, 80)
            cyborg = GameSprite("cyborg.png" , 850, 300, 60, 60)
            cyborg1 = GameSprite("cyborg.png" , 900, 600, 60, 60)
            cyborg2 = GameSprite("cyborg.png" , 810, 130, 60, 60)
            cyborg3 = GameSprite("cyborg.png" , 870, 450, 60, 60)
            finish = False
            


    if not finish:

        keys = key.get_pressed()
        if keys[K_UP] and player.rect.y>0:
            player.rect.y -= speed
        if keys[K_DOWN] and player.rect.y<740:
            player.rect.y += speed
        if keys[K_LEFT] and player.rect.x>0:
            player.rect.x -= speed
        if keys[K_RIGHT] and player.rect.x<940:
            player.rect.x += speed
        
        if sprite.collide_rect(player, treasure):
            result = font1.render("Ти Виграв!", True, (255,0,0))
            finish = True
            hard = hard + 1
            win_sound.play()




        keys = key.get_pressed()
        if bot == True and cyborg.rect.x>800:
            cyborg.rect.x -= speed_2 
        else:
            bot = False
        if bot == False and cyborg.rect.x<940:
            cyborg.rect.x += speed_2 
        else:
            bot = True

        if sprite.collide_rect(player, cyborg):
            result = font1.render("Ти програв!", True, (255,0,0))
            finish = True

            kick_sound.play()




        keys = key.get_pressed()
        if bot1 == True and cyborg1.rect.x>800:
            cyborg1.rect.x -= speed_2
        else:
            bot1 = False
        if bot1 == False and cyborg1.rect.x<940:
            cyborg1.rect.x += speed_2 
        else:
            bot1 = True

        if sprite.collide_rect(player, cyborg1):
            result = font1.render("Ти програв!", True, (255,0,0))
            finish = True

            kick_sound.play()




        keys = key.get_pressed()
        if bot2 == True and cyborg2.rect.y>0:
            cyborg2.rect.y -= speed_2 
        else:
            bot2 = False
        if bot2 == False and cyborg2.rect.y<200:
            cyborg2.rect.y += speed_2 
        else:
            bot2 = True

        if sprite.collide_rect(player, cyborg2):
            result = font1.render("Ти програв!", True, (255,0,0))
            finish = True
            kick_sound.play()








        window.blit(bg_image, (0,0))

        for w in walls:
            w.draw()
            if sprite.collide_rect(player, w):
                result = font1.render("Ти програв!", True, (255,0,0))
                finish = True
                kick_sound.play()

        if hard >= 1:
            result = font1.render("Level 1", True, (255,0,0))
            restsrt = font1.render("щоб продовжити натисніть R", True, (255,0,0))
            speed_2 = 3.6
        if hard >= 2:
            result = font1.render("Level 2", True, (255,0,0))
            keys = key.get_pressed()
            if bot3 == True and cyborg3.rect.x>800:
                cyborg3.rect.x -= speed_2
            else:
                bot3 = False
            if bot3 == False and cyborg3.rect.x<940:
                cyborg3.rect.x += speed_2 
            else:
                bot3 = True
    
            if sprite.collide_rect(player, cyborg3):
                result = font1.render("Ти програв!", True, (255,0,0))
                finish = True
                kick_sound.play()
            cyborg3.draw()
        if hard >= 3:
            result = font1.render("Level 3", True, (255,0,0))
            speed_2 = 4.2
        if hard >= 4:
            result = font1.render("Level 4", True, (255,0,0))
            speed_2 = 4.8
        if hard == 5:
            result = font1.render("Level 5", True, (255,0,0))
            speed_2 = 5.4
            speed = 4.6
        if hard == 6:
            result = font1.render("BOSS", True, (255,0,0))
            speed_2 = 5.5
            speed = 5.2
        if hard == 7:
            result = font1.render("Вітаю ти пройшов ", True, (255,0,0))
            result = font1.render("Щоб почати заново натисни R", True, (255,0,0))
            hard = 0
            speed_2 = 3
            speed = 4

        


        treasure.draw()
        player.draw()
        cyborg.draw()
        cyborg1.draw()
        cyborg2.draw()
        wall23.draw()
    else:
        window.blit(restart, (roz))
        window.blit(result, (380, 200))
    display.update()
    clock.tick(FPS)