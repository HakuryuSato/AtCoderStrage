

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

import sys
data = sys.stdin.read().split()
N = int(data[0])
Q = int(data[1])
S = list(data[2])

queries = data[3:]
total = 0

for i in range(N - 2):
    if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
        total += 1

for q in range(Q):
    X = int(queries[2 * q])
    C = queries[2 * q + 1]
    pos = X - 1
    affected = [pos - 2, pos - 1, pos]
    for i in affected:
        if 0 <= i <= N - 3:
            if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
                total -= 1
    S[pos] = C
    for i in affected:
        if 0 <= i <= N - 3:
            if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
                total += 1
    print(total)
