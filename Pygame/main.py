import pygame

print (pygame.ver)

# Iniciar
pygame.init()
window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("SoccerGame")
closedGame = True

# Assets
footballField = pygame.image.load("assets/field.png")

score1 = 0
score1Img = pygame.image.load("assets/score/0.png")
score2 = 0
score2Img = pygame.image.load("assets/score/0.png")

# Jogador 1
player1 = pygame.image.load("assets/player1.png")
player1X = 50
player1Y = 290
player1MoveUp = False
player1MoveDown = False

# Jogador 2
player2 = pygame.image.load("assets/player2.png")
player2X = 1152
player2Y = 290
player2DirY = -5

# ball
ball = pygame.image.load("assets/ball.png")
ballX = 617
ballY = 337
ballDirX = -5
ballDirY = -8

# Mover o Player 1
def movePlayer1():
    global player1X
    global player1Y

    if player1MoveUp:
        player1Y -= 5
    else:
        player1Y += 0

    if player1MoveDown:
        player1Y += 5
    else:
        player1Y += 0

def movePlayer2():
    global player2X
    global player2Y
    global player2DirY

    player2Y += player2DirY

    if player2Y <= 0:
        player2DirY *= -1

    elif player2Y >= 570:
        player2DirY *= -1

# Mover a bola
def MoveBall():
    global ballX
    global ballY
    global ballDirX
    global ballDirY
    global score1
    global score2

    ballX += ballDirX
    ballY += ballDirY

    # Colisão player 1
    if ballX < 120:
        if player1Y < ballY + 23:
            if player1Y + 146 > ballY:
                ballDirX *= -1
    
    # Colisão player 2
    if ballX > 1100:
        if player2Y < ballY + 23:
            if player2Y + 146 > ballY:
                ballDirX *= -1

    # Colisao Parede
    if ballY <= 0:
        ballDirY *= -1
    elif ballY > 674:
        ballDirY *= -1

    # Bola Reseta
    if ballX <= -300:
        ballX = 600
        ballY = 300
        ballDirX *= -1
        score2 += 1

    if ballX >= 1420:
        ballX = 600
        ballY = 300
        ballDirX *= -1
        score1 += 1

# Desenhar todos os objetos
def draw():
    window.blit(footballField,(0,0))
    window.blit(player1, (player1X,player1Y))
    window.blit(player2, (player2X,player2Y))
    window.blit(ball, (ballX,ballY))
    window.blit(score1Img, (500, 10))
    window.blit(score2Img, (700, 10))

# Manter tela
while closedGame:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            closedGame = False

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1MoveUp = True
            if events.key == pygame.K_s:
                player1MoveDown = True

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1MoveUp = False
            if events.key == pygame.K_s:
                player1MoveDown = False
   
    MoveBall()
    movePlayer1()
    movePlayer2()
    draw()
    pygame.display.update()