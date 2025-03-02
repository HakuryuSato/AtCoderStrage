import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())

N=int(input())

G=[['?']*N for _ in range(N)]

for i in range(N):
    for j in range(N):

        if min(i,j,N-i-1,N-j-1)%2==0:
            G[i][j]="#"
                
        else:
            G[i][j]="."

    
for g in G:
    print("".join(g))