
# Banging_Splash
# Banging Splash

# ゲーム のタイトル
Banging Splash


## 実行環境の必要条件
* python >= 3.10
* pygame >= 2.1

## ゲームの概要

プレイヤーは画面下部に配置されています。プレイヤーは左右に移動し、スペースキーを押すことで弾を発射できます。
敵は画面上部からランダムに出現し、左右に移動します。プレイヤーが弾を当てると、新しい敵がランダムな位置に再出現します。
ゲームの目標は、できるだけ多くの敵を倒してスコアを稼ぐことです。

## ゲームの実装


自機キャラを操り、敵機を打ち倒すシューティングゲーム。

## ゲームの実装
### 共通基本機能
* YouTubeより拝借したインベーダーゲームコード
### 担当追加機能
* C0A22045「特殊技:散弾」:RSHIFTを押すことで、現在溜まっているゲージ数×1つの散弾が発射される
### ToDo
- multishotは未完成どころか最初の状態からほぼ進んでないと言っても過言ではないので次回までに完成させてくる
### メモ
* 

プレイヤーは画面下部に配置されています。プレイヤーは左右に移動し、スペースキーを押すことで弾を発射できます。
敵は画面上部からランダムに出現し、左右に移動します。プレイヤーが弾を当てると、新しい敵がランダムな位置に再出現します。
ゲームの目標は、できるだけ多くの敵を倒してスコアを稼ぐことです。

## ゲームの実装

***操作方法***:
左矢印キー: プレイヤーを左に移動
右矢印キー: プレイヤーを右に移動
スペースキー: 弾を発射
左シフトキー: スコアを消費してバリアを生成
右シフトキー: スコアを消費して散弾銃モード

***要素***:4


操作方法:
左矢印キー: プレイヤーを左に移動
右矢印キー: プレイヤーを右に移動
スペースキー: 弾を発射
左シフトキー: スコアを消費してバリアを生成
右シフトキー: スコアを消費して散弾銃モード

要素:4

プレイヤー（playerImg）: 左右に移動できる宇宙船。
敵（enemyImg）: 画面上部から左右に移動する敵宇宙船。
弾（bulletImg）: プレイヤーと敵が発射する弾。
バリア（shield）: プレイヤーが生成するバリア



得点:
敵宇宙船を倒すごとに、得点が加算されます。得点は画面左上に表示されます。

注意点:
敵宇宙船が放つ弾がプレイヤーに当たると、ゲームが終了します。

コードの構造:

***得点***:
敵宇宙船を倒すごとに、得点が加算されます。得点は画面左上に表示されます。

***注意点***:
敵宇宙船が放つ弾がプレイヤーに当たると、ゲームが終了します。

***コードの構造***:

得点:
敵宇宙船を倒すごとに、得点が加算されます。得点は画面左上に表示されます。

注意点:
敵宇宙船が放つ弾がプレイヤーに当たると、ゲームが終了します。

コードの構造:


Pygameライブラリを使用してウィンドウを作成し、ゲームのメインループを実装しています。
イベントハンドリングを使用して、キーボードの入力に応じてプレイヤーの動きや弾の発射を制御しています。
isCollision 関数は、弾と敵の衝突を検出しています。
スコアは画面左上に表示され、敵を倒すと増加します。


クリア条件:
敵が放つ弾に当たらずプレイヤーは敵を打ち落とし最高点を目指す

参考サイト:
https://www.youtube.com/watch?v=fAJ_BjLd3Ro
### 共通基本機能
* 主人公キャラクターに関するクラス
方向キーで左右に移動
スペースキーで弾の放出
* 敵に関するクラス
ランダムのスピードで左右に移動一定の時間ごとに弾の放出

### 担当追加機能
* 中西
敵の動きをランダム性（速度）のある横移動にする
### ToDo
- [ ] 敵横移動機能
- [ ] 散弾機能
- [ ] バリア機能
- [ ] ゲージ機能
- [ ] 敵の攻撃機能

### メモ
Banging Splashゲームは、プレイヤーが左右に移動可能な宇宙船で画面上部から出現する敵宇宙船を撃破し、
得点を稼ぐシンプルな2Dゲームです。プレイヤーは左右矢印キーで移動し、スペースキーで弾を発射します。
敵を倒すと得点が加算され、敵が画面下部に到達するとゲーム終了。
***クリア条件***:
敵が放つ弾に当たらずプレイヤーは敵を打ち落とし最高点を目指す

***参考サイト***:

クリア条件:
敵が放つ弾に当たらずプレイヤーは敵を打ち落とし最高点を目指す

参考サイト:

https://www.youtube.com/watch?v=fAJ_BjLd3Ro

###共通基本機能
* 主人公キャラクターに関するクラス
方向キーで左右に移動
スペースキーで弾の放出
* 敵に関するクラス
ランダムのスピードで左右に移動一定の時間ごとに弾の放出

### 担当追加機能

* 中西
敵の動きをランダム性（速度）のある横移動にする
* 金子
出るビームをあるポイント量を消費することによって出る散弾ビーム機能の追加
* 浅岡
敵を倒すと溜まるゲージの生成（マックス10）
* 南部
プレイヤーに敵が放出した弾に当たったらゲームオーバーになる機能
* 宮崎
敵が弾を一定の間隔で弾を放出する機能を追加。
enemybulletについて→座標とステータスを定義した。
fire_enemy_bulletで座標を更新する形にした。
isCollision、isPlayerHitで当たり判定に関する事を定義した。
背景を追加。
* 伊藤
ゲージをある量使用して発生させるバリア生成機能
### ToDo
- [ ] 敵横移動機能
- [ ] 散弾機能
- [ ] バリア機能
- [ ] ゲージ機能
- [ ] 敵の攻撃機能

### メモ
Banging Splashゲームは、プレイヤーが左右に移動可能な宇宙船で画面上部から出現する敵宇宙船を撃破し、
得点を稼ぐシンプルな2Dゲームです。プレイヤーは左右矢印キーで移動し、スペースキーで弾を発射します。
敵を倒すと得点が加算され、敵が画面下部に到達するとゲーム終了。
効果音やシンプルなグラフィックを使用し、改善点としてアニメーションやレベルごとの難易度変更が挙げられます。
PythonとPygameが必要な動作環境です。


* 中西
敵の動きをランダム性（速度）のある横移動にする
* 金子
出るビームをあるポイント量を消費することによって出る散弾ビーム機能の追加
* アサオカ（担当コマンド）
敵を倒すと溜まるゲージの生成（マックス10）
ゲージの元となる図形を描画して敵に充てるたびにゲージが少しずつ増えていく仕組みにした。
* 南部
プレイヤーに敵が放出した弾に当たったらゲームオーバーになる機能
* 宮崎
敵が弾を一定の間隔で弾を放出する機能
* 伊藤
ゲージをある量使用して発生させるバリア生成機能
### ToDo

-  ゲージ機能（担当機能）
- 1.敵に当たるとゲージ増加
- 2.スキルを使うとゲージ減少





