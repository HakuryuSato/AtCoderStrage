import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

# 実行時間2秒 メモリ1GB



S = input()

x = [0] * 26

# アルファベットの座標を格納
for i in range(26):
    x[ord(S[i]) - ord("A")] = i

ans = 0
for i in range(25):
    ans += abs(x[i] - x[i + 1])
print(ans)



# キーボードが固定ではなく、与えられたSがキーボードだった
# keyboard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# current_position = 0
# total_distance = 0

# S=input()

# for char in S:
#     next_position = keyboard.index(char)
#     total_distance += abs(next_position - current_position)
#     current_position = next_position

# # 最小移動距離の出力
# print(total_distance)

