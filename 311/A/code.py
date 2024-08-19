import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())
S = input()

d=set()

for i in range(N):
    d.add(S[i])
    if(len(d)>=3):
        print(i+1)
        break
