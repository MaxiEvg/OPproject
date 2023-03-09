import pgzrun
from typing import Tuple                    
from random import randint


WIDTH = 1280
HEIGHT = 800


player = Actor("gg")           # 
player_position = WIDTH // 2, HEIGHT // 2     # Установка параметров игрока
player.center = player_position               #

COIN_COUNT = 9                                # Кол-во максимальных монет
coin_list = list()                            # Массив учета монет
spike_list = list()                           # Массив учета спайков

coin_countdown = 2                            # Задаем частоту появления монет (в сек)
coin_interval = 0.15                           # Ускорение появления монет (в сек)

spike_countdown = 2                           # Задаем частоту появления спайков
spike_interval = 0.25                         # Ускорение появления спайков (в сек)

score = 0
health1 = list()
health = 5
limit = 0.5

xxx = randint(1, 20)
if xxx == 20:
    music.play('oops')
    music.set_volume(0.3)
else:
    music.play('level3')
    music.set_volume(0.4)

def add_spike():
    
    global spike_countdown
    
    new_spike = Actor("spike1", (randint(10, WIDTH - 10), randint(10, HEIGHT - 10)))

    spike_list.append(new_spike)
    
    if len(spike_list) < 5:
        spike_countdown -= spike_interval
    if spike_countdown < 1:
       spike_countdown = 5
       
    clock.schedule(add_spike, spike_countdown)  # Частота появления спайков

def add_coin():
   
    global coin_countdown

    new_coin = Actor("coin_gold1", (randint(10, WIDTH - 10), randint(10, HEIGHT - 10)))

    coin_list.append(new_coin)
    
    if len(coin_list) < 3:
        coin_countdown -= coin_interval

    if coin_countdown < limit:
        coin_countdown = limit

    clock.schedule(add_coin, coin_countdown)     # Частота появления монет

def add_hp():

    hp = Actor("hp", (yyy, 120))
    
    health1.append(hp)



def on_mouse_move(pos: Tuple):                   # pos {Tuple} - текущее положение мыши
    
    global player_position

    player_position = pos

    if player_position[0] < 0:                    #
        player_position[0] = 0                    #
    if player_position[0] > WIDTH:                #
        player_position[0] = WIDTH                #
                                                  # Убедитесь, что игрок не выходит за пределы экрана
    if player_position[1] < 0:                    #
        player_position[1] = 0                    #
    if player_position[1] > HEIGHT:               #
        player_position[1] = HEIGHT               #

color_ = "white"

def update(delta_time: float):                    # delta_time {float} - время с последнего кадра
    
    global score
    global health 
    global color_

    player.center = player_position

    coin_remove_list = []
    spike_remove_list = []

    for coin in coin_list:
        if player.colliderect(coin):
            sounds.coin_pickup.play()  
            coin_remove_list.append(coin)
            score += 10

    for spike in spike_list: 
        if player.colliderect(spike):
            sounds.eep.play()  
            spike_remove_list.append(spike)
            score -= 50
            health -=1
            if health > 3:
                color_ = "white"            #          
            if health == 3:                 #
                color_ = "yellow"           #
            elif health == 2:               # Занести в массив сердца
                color_ = "orange"           #
            elif health == 1:               #
                color_ = "red"              #
        if len(spike_list) > 8:             #
            spike_remove_list.append(spike)      
        
    if (score % 1000 == 0) and (score > 0):
        health += 1
        score += 10        
    if health > 5:
        health = 5

    for coin in coin_remove_list:
        coin_list.remove(coin)
    for spike in spike_remove_list:
        spike_list.remove(spike)

    if len(coin_list) >= COIN_COUNT:
        clock.unschedule(add_coin)  
        clock.unschedule(add_spike)
        print(f"Game over! Final score: {score}")
        exit()
    if health <=0:
        clock.unschedule(add_coin)
        clock.unschedule(add_spike)
        print(f"Game over! Final score: {score}")
        exit()


def draw():

    screen.clear()  

    screen.fill("#040b17")  
    if health == 4:
        screen.blit("bg1", (0, 0))
    elif health == 3:
        screen.blit("bg2", (0, 0))
    elif health == 2:
       screen.blit("bg3", (0, 0))
    elif health == 1:
        screen.blit("bg4", (0, 0))
    elif health == 0:
        screen.blit("bg5", (0, 0))
    
    player.draw()

    for coin in coin_list:           
        coin.draw()                  
    for spike in spike_list:         
        spike.draw()        
    
    global yyy
    yyy = 70
    hp1 = Actor("hp1", (yyy+100,     100))
    hp2 = Actor("hp1", (yyy+150,  100))
    hp3 = Actor("hp1", (yyy+200, 100))
    hp4 = Actor("hp1", (yyy+250, 100))
    hp5 = Actor("hp1", (yyy+300, 100))

    if health == 5:
        hp1.draw(); hp2.draw(); hp3.draw(); hp4.draw(); hp5.draw()
    elif health == 4:
        hp1.draw(); hp2.draw(); hp3.draw(); hp4.draw(); 
    elif health == 3:
        hp1.draw(); hp2.draw(); hp3.draw(); 
    elif health == 2:
        hp1.draw(); hp2.draw()
    elif health == 1:
        hp1.draw()
    
    hptxt = Actor("hp", (yyy+27,     104))
    hptxt.draw()
    scoretxt = Actor("score", (yyy+80, HEIGHT - 50))
    scoretxt.draw()

    screen.draw.text(
        f"{score}",
        (260, HEIGHT - 70),
        fontsize=56, shadow=(2,2), scolor="#202020",
        color="white", 
    )

   
    


clock.schedule(add_coin, coin_countdown)       
clock.schedule(add_spike, spike_countdown)     

pgzrun.go()
