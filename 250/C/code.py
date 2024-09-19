import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

N, Q = map(int, input().split())  # Nボール数, Q 操作回数 どちらも最大2*10^5


balls = [i for i in range(1, N + 1)]
pos = {balls[i]: i for i in range(N)}


for _ in range(Q):
    x = int(input())
    idx = pos[x]

    if idx == N - 1:
        swap_idx = idx - 1
    else:
        swap_idx = idx + 1

    balls[idx], balls[swap_idx] = balls[swap_idx], balls[idx]
    pos[balls[idx]], pos[balls[swap_idx]] = idx, swap_idx

print(*balls)
