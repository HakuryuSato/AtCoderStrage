import sys

# ローカル用
file_number = 1
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

N = int(input())
q = [0] * N
r = [0] * N

for i in range(N):
    q[i], r[i] = map(int, input().split())

Q = int(input())

for _ in range(Q):
    t, d = map(int, input().split())
    t -= 1
    b, c = divmod(d, q[t])
    a = b if c <= r[t] else b + 1
    ans = a * q[t] + r[t]
    print(ans)