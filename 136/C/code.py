import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

n=int(input())
H=list(map(int,input().split()))

if len(H) == 1:
    print('Yes')
    exit()

for i in range(n - 2, -1, -1):
    if H[i] > H[i + 1] + 1:
        print("No")
        exit()
    elif H[i] == H[i + 1] + 1:
        H[i] -= 1
print('Yes')