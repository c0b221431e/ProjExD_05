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
multishot = False  # 散弾が放たれている状態か否か

# Score
score_value = 0

gage = 5  # ゲージの溜まり具合 ※conflict時、この変数(以下のプログラムで使われているものを含む)は、ゲージ担当のものに合わせてください

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    screen.blit(bulletImg, (x + 16, y + 10)) 
    bullet_state = 'fire'

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
    def __init__(self, playerX, playerY, power: int):
        """
        引数
        playerX, playerY:自機のX座標とY座標
        power:ゲージの溜まり具合、散弾で出る弾の数
        """
        self.playerX, self.playerY = playerX, playerY
        self.power = power
        self.image = pygame.image.load('bullet.png')
        self.bullets_locate = [[self.playerX, self.playerY]]*power   # 弾の現在地のリスト
        self.bullet_speed = bulletY_change  # 弾の進むスピード
        self.is_arrive = [False] * power  # 弾が存在するか否かのリスト

    def summon_bullets(self):
        """
        散弾を生成するための関数
        """
        self.lst = []  # 角度の違う弾丸のリスト
        self.angles = []  # 角度のリスト
        cnt = 0
        try:
            for i in range(-400, 410, 800//(self.power-1)):  # ゲージが2以上の場合、散弾発動
                self.lst.append(pygame.transform.rotozoom(self.image, i/10, 1.0))
                self.angles.append(i/10)
                self.is_arrive[cnt] = True
                cnt += 1
        except ZeroDivisionError:  # ゲージが1の場合、正面に飛ぶようにする
            self.lst.append(pygame.transform.rotozoom(self.image, 0, 1.0))
            self.angles.append(0)
            self.is_arrive[cnt] = True
        
    def move_bullets(self):
        """
        散弾を動かすための関数
        """
        for n, img in enumerate(self.lst):  # 存在するすべての弾に対して
            if self.is_arrive[n]:
                locx, locy = self.bullets_locate[n]
                screen.blit(img, (self.bullets_locate[n]))  # 弾の描画
                locx += math.cos(math.radians(self.angles[n]+90)) *self.bullet_speed  # 弾の移動
                locy -= math.sin(math.radians(self.angles[n]+90)) *self.bullet_speed
                self.bullets_locate[n] = [locx, locy]

    def kill_bullets(self):
        """
        散弾を消去するための関数
        """
        global enemyX, enemyY, score_value
        enemy = "arrive"  # 敵が生存しているか否か(複数弾同時ヒットを避けるため)
        for n, b in enumerate(self.bullets_locate):  # 全ての弾に対して
            if enemy == "arrive":  # 敵が生存しているなら
                collision = isCollision(enemyX, enemyY, b[0], b[1])
                if collision:  # 敵と衝突したなら、スコアを+1して、弾と敵をリセットする
                    score_value += 1
                    enemyX = random.randint(0, 736)
                    enemyY = random.randint(50, 150)
                    self.is_arrive[n] = False
                    enemy = "dead"  # 敵を生存していない状態にする
            if b[1] < 0:  # 画面外に出たら弾消失
                self.is_arrive[n] = False
                

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
            if event.key == pygame.K_RSHIFT and gage >= 1 and not multishot:  # ゲージが1以上溜まっている時にRSHIFTが押されたなら
                mshot = Multishot(playerX, playerY, gage)  # Multishotインスタンス生成
                mshot.summon_bullets()
                multishot = True  # 散弾状態へ移行
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
    
    # Multishot
    if multishot:  # 散弾についての処理
        mshot.move_bullets()
        mshot.kill_bullets()
        if True not in mshot.is_arrive:  # 存在する弾がなくなったら、multishot状態から抜ける
            multishot = False

    # Score
    font = pygame.font.SysFont(None, 32) # フォントの作成　Noneはデフォルトのfreesansbold.ttf
    score = font.render(f"Score : {str(score_value)}", True, (255,255,255)) # テキストを描画したSurfaceの作成
    screen.blit(score, (20,50))

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
