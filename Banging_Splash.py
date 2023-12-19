import pygame
from pygame import mixer
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
# screen.fill((150, 150, 150))
pygame.display.set_caption('Invaders Game')

# Player
playerImg = pygame.image.load('player.png')
playerX, playerY = 370, 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change, enemyY_change = 1, 40

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX, bulletY = 0, 480
bulletX_change, bulletY_change = 0, 3
bullet_state = 'ready'

# Score
score_value = 0

gage = 5  # ゲージの溜まり具合

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    screen.blit(bulletImg, (x + 16, y + 10)) 
    # bullet_state = 'fire' は下の方で行ってます

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False
        

class Multishot:
    """
    特殊技「散弾」のクラス
    """
    def __init__(self, power: int):
        """
        引数
        playerX, playerY:自機のX座標、Y座標
        power:ゲージの溜まり具合、散弾で出る弾の数
        """
        global bullet_state 
        self.power = power
        bullet_state = 'multi'  # bullet_stateに新たな状態'multi'を追加することで散弾を表現

    def shoot_ms(self):
        """
        散弾を動かすための関数
        """
        global bulletY
        for i in range(40, 761, 720//(self.power-1)):  # 全ての散弾に対して
            fire_bullet(i-10, bulletY)
            collision = isCollision(enemyX, enemyY, i-10, bulletY)
            if collision:
                bulletY = 480
                bullet_state = 'ready'
                score_value += 1
                enemyX = random.randint(0, 736)
                enemyY = random.randint(50, 150)
        bulletY -= bulletY_change
        
        

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    bullet_state = 'fire'  # 散弾においてbullet_stateを利用するにあたり、fireへの移行をこっちで行うようにしました
            if event.key == pygame.K_RSHIFT:  # RSHIFTが押されたなら
                mshot = Multishot(gage)
                gage = 0  # ゲージをすべて消費

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # Player
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy
    if enemyY > 440:
        break
    enemyX += enemyX_change
    if enemyX <= 0: #左端に来たら
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >=736: #右端に来たら
        enemyX_change = -1
        enemyY += enemyY_change

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if bullet_state is 'multi':  # 散弾が放たれていたら
        mshot.shoot_ms()
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)

    # Bullet Movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change  
    
    

    # Score
    font = pygame.font.SysFont(None, 32) # フォントの作成　Noneはデフォルトのfreesansbold.ttf
    score = font.render(f"Score : {str(score_value)}", True, (255,255,255)) # テキストを描画したSurfaceの作成
    screen.blit(score, (20,50))

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
