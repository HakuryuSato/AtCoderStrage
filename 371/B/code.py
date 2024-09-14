import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N,M = map(int,input().split())
l=[True]*N

for i in range(M):
    fam,gender = input().split()
    fam = int(fam)
    if l[fam-1] and gender=="M":
        print("Yes")
        l[fam-1]=False
    else:
        print("No")




