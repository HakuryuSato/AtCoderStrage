import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

L,R=map(int,input().split())

if L==1 and R==0:
    print("Yes")
elif L==0 and R==1:
    print("No")
else:
    print("Invalid")



