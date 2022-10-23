from pygame import *
from random import randint

from cards import cards_list
mixer.init()
font.init()
init()

WIDTH = 900
HEIGHT = 600
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Zenterost")

place_card_e = {
    "one_card" : (100,50),
    "two_card" : (150,50),
    "three_card" : (200,50)
}

place_card_p = {
    "one_card" : (100,150),
    "two_card" : (150,150),
    "three_card" : (200,150)
}





class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(image_name),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.width = width
        self.height = height
    
    def draw(self):
        window.blit(self.image, self.rect)



class Player:
    def __init__(self):
        self.hp = 500
        self.ballets = sprite.Group()
        self.cards = []
        self.cometery_cards = []



class Enemy():
    def __init__(self):
        self.hp = 500
        self.cards = []
        self.cometery_cards = []



class Card(GameSprite):
    def __init__(self, name, card_img, defend, atk):
        super().__init__('reverse.jpg', x, y, width, height)
        self.name = name
        self.card_img = card_img
        self.DEF = 0
        self.ATK = 0
            
    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y



bg_image = transform.scale(image.load("cards/Pole.png"),(WIDTH, HEIGHT))

player = Player()
clock = time.Clock()
player.cards = []
for card in cards_list:
    new_card = Card(card, cards_list[card]['img'],cards_list[card]['def'],cards_list[card]['atk'])
    player.cards.append(new_card)

enemy = Enemy()
enemy.cards = []
for card in cards_list:
    new_card = Card(card, cards_list[card]['img'],cards_list[card]['def'],cards_list[card]['atk'])
    enemy.cards.append(new_card)

r_card = 0
rt = 0
n_e_c = 18

FPS = 60
run = True
finish = False

while run:
    window.blit(bg_image, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:

        if  len(enemy.cards) > 0:
            if rt == True:
                enemy.cards[r_card].move(place_card_e[one_card])
                r_card += 1
                window.blit(enemy.cards[r_card], (place_card_e[two_card]))
                r_card += 1
                window.blit(enemy.cards[r_card], (place_card_e[three_card]))
                r_card += 1
                rt == False
            else:
                pass
        else:
            pass




    else:
        window.blit(result, (200, 200))
    enemy.cards.draw(window)
    display.update()
    clock.tick(FPS)