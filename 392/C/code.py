import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

N=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))

Q_dict={}
P_dict={}
zekken={}
for i in range(1,N+1):
    Q_dict[Q[i-1]]=P[i-1]
    zekken[i]=Q[i-1]
    P_dict[i]=P[i-1]

result=[]
for i in range(1,N+1):
    miteru = Q_dict[i]
    kiteru = zekken[miteru]
    result.append(kiteru)


print(*result)