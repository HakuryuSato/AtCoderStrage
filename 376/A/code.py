import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N,C=map(int,input().split())
T=list(map(int,input().split()))

reward_count = 1  
last_reward_time = T[0]

for i in range(1, N):
    if T[i] - last_reward_time >= C:
        reward_count += 1 
        last_reward_time = T[i] 

print(reward_count)




'''
実行時間2秒 メモリ1GB
[問題文]
N ボタン押下数
C クールダウン
T ボタンを押して報酬をもらおうとした時間

何個の報酬を受け取ることができたか出力

[私の考え]

'''