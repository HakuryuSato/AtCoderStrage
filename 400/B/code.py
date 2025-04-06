import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())


N,M = read_values()

ans =0

for i in range(M+1):
    ans += N**i

print(ans if ans <= 10**9 else 'inf')