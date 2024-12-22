import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

import sys
data = sys.stdin.read().split()
N = int(data[0])
H = list(map(int, data[1:]))

# 答え (少なくとも1棟は飾れる)
max_val = 1

# step(=K) を 1 から N まで
for step in range(1, N + 1):
    # offset(=r) を 0 から step-1 まで
    for offset in range(step):
        # 同じ高さがどれだけ続いているかをカウントする変数
        count = 1
        last_height = H[offset]
        
        # step ごとに進むループは while 文を使って range 呼び出しを避ける
        i = offset + step
        while i < N:
            if H[i] == last_height:
                count += 1
            else:
                # 今までの連続長を max_val と比較
                if count > max_val:
                    max_val = count
                count = 1
            last_height = H[i]
            i += step
        
        # グループ末尾の連続長をチェック
        if count > max_val:
            max_val = count

print(max_val)
