import pygame
from pygame import mixer
import random
import math

pygame.init()

mixer.init()

screen = pygame.display.set_mode((800, 600))
# screen.fill((150, 150, 150))
pygame.display.set_caption('ex05/Invaders Game')

# Player
playerImg = pygame.image.load('ex05/player.png')
playerX, playerY = 370, 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('ex05/enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change, enemyY_change = 4, 40

# Bullet
bulletImg = pygame.image.load('ex05/bullet.png')
bulletX, bulletY = 0, 480
bulletX_change, bulletY_change = 0, 3
bullet_state = 'ready'

# Score
score_value = 0
#クリア条件
font_1 = pygame.font.SysFont(None, 32) # フォントの作成
clear_font = pygame.font.SysFont(None, 64) # **ゲームクリアメッセージ用のフォントを作成**


def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False
    
# gaugeの値設定
gauge_value = 0
gauge_max = 5

"""
gaugeの描画設定
ゲージの増加を表すゲージを緑に設定
ゲージが満たされていない事を表す色を赤に設定
スコアの下あたり表示させる
"""

def gauge():
    pygame.draw.rect(screen, (255, 0, 0), [20, 80, gauge_max * 20, 20])  #　赤のゲージ
    pygame.draw.rect(screen, (0, 255, 0), [20, 80, gauge_value * 20, 20])  # 緑のゲージ

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

            #capslockを押すとゲージが一増える
            if event.key == pygame.K_CAPSLOCK and gauge_value >= 2:
                gauge_value  -= 2
                gauge_max += 1
                if gauge_max >= 15:
                    gauge_max -=1
                    gauge_value += 2
            #なくてもいい        
            elif event.key == pygame.K_CAPSLOCK and gauge_value < 2:
                event_text = clear_font.render("It's not the time yet...", True, (255,255,0)) # クリアメッセージを作成
                screen.blit(event_text, (200,250)) # 画面中央に表示
                pygame.display.update()
                pygame.time.wait(500) # 5秒間待つ

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
        enemyX_change = 1#4
        enemyY += enemyY_change
    elif enemyX >=736: #右端に来たら
        enemyX_change = -1#-4
        enemyY += enemyY_change

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1

        # ゲージの描画を、当たり判定でする。
        if gauge_value<gauge_max:
            gauge_value += 1 # ゲージの値を1増加する。
        if gauge_value >= gauge_max:
            gauge_value=gauge_max

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

    # ゲームクリア
    """
    if score_value >= 3:
        clear_text = clear_font.render("congratulations!", True, (255,255,255)) # **クリアメッセージを作成**
        screen.blit(clear_text, (200,250)) # 画面中央に表示
        pygame.display.update()
        pygame.time.wait(5000) # 5秒間待つ
        break
"""
    # ゲームクリア
    if score_value >= 30:
        clear_text_1 = clear_font.render("congratulations...", True, (255,255,0)) # クリアメッセージを作成

        text_height = clear_text_1.get_height()
        start_y = 600  # テキストが画面下から始まるように設定
        speed = 8  # テキストが移動する速度

        while start_y + text_height > 0:  # テキストが画面上に完全に消えるまでループ
            screen.fill((0, 0, 0))  # 画面を黒で塗りつぶす
            screen.blit(clear_text_1, (200, start_y))  # テキストを新しい位置に描画
            pygame.display.update()  # 画面を更新
            start_y -= speed  # テキストのy座標を減らす（上に移動）
            pygame.time.wait(20)  # 一定時間待つ（テキストの移動速度を制御）

        
        break

    # guageの描画
    gauge()

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
