import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400


score = 0
game_over = False

nicki = Actor("nicki")
nicki.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
  screen.fill("pink")
  nicki.draw()
  coin.draw()
  screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

if game_over:
 screen.fill("pink")
 screen.draw.text("Final score: " + str(score), topleft=(10, 10), fontsize=60)

def place_coin():
    coin.x = randint(20, WIDTH - 20)
    coin.y = randint(20, HEIGHT - 20)

def time_up():
    global game_over
    game_over = True

def update():
    global score
    
    if keyboard.left:
        nicki.x = nicki.x - 2
    elif keyboard.right:
        nicki.x = nicki.x +2
    elif keyboard.up:
        nicki.y = nicki.y - 2
    elif keyboard.down:
        nicki.y = nicki.y + 2

    coin_collected = nicki.colliderect(coin)
    
    if coin_collected:
           score = score + 10
           place_coin()

clock.schedule(time_up, 19.0)

pgzrun.go()


