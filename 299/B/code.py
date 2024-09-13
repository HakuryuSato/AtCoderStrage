import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N,T=map(int,input().split()) #　4 2
C=list(map(int,input().split())) # 色 1 2 1 2
R=list(map(int,input().split())) # 値 6 3 4 5


# 勝者となるプレイヤーの番号を出力
# 色がTであるカードが1枚以上場に出された場合、値が最大の物を出したプレイヤーが勝者
# 色がTであるカードが場に1枚も出されなかった場合、プレイヤー1が出したカードと同じ色のカードのうち、値が最大の物を出したプレイヤーが勝利


# 色と値を結合したリストを作成
cards = [(C[i], R[i], i + 1) for i in range(N)]  # (色, 値, プレイヤー番号)

# 色Tのカードで最大値を持つプレイヤーを探す
filtered_T = [card for card in cards if card[0] == T]

if filtered_T:
    # 色Tのカードがある場合、値でソートして最大のプレイヤー番号を取得
    winner = max(filtered_T, key=lambda x: x[1])[2]
else:
    # 色Tのカードがない場合、プレイヤー1の色のカードで最大のプレイヤー番号を取得
    player1_color = C[0]
    filtered_C1 = [card for card in cards if card[0] == player1_color]
    winner = max(filtered_C1, key=lambda x: x[1])[2]

print(winner)