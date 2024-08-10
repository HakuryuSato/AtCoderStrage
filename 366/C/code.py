import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

Q = int(input())

query=Q*[0]
for i in range(Q):
    query[i]=list(map(int,input().split()))

sack = {}
unique_count = 0

for q in query:
    if q[0] == 1:
        if q[1] in sack:
            sack[q[1]] += 1
        else:
            sack[q[1]] = 1
            unique_count += 1
    elif q[0] == 2:
        if q[1] in sack:
            sack[q[1]] -= 1
            if sack[q[1]] == 0:
                del sack[q[1]]
                unique_count -= 1
    else:
        print(unique_count)

