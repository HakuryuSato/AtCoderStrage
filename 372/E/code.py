import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

input = sys.stdin.read
data = input().split()

N = int(data[0])
Q = int(data[1])
ptr = 2

parent = [i for i in range(N+1)]
size = [1]*(N+1)
top_k = [[i] for i in range(N+1)]

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

for _ in range(Q):
    query_type = data[ptr]
    if query_type == '1':
        u = int(data[ptr+1])
        v = int(data[ptr+2])
        ptr += 3
        pu = find(u)
        pv = find(v)
        if pu != pv:
            if size[pu] < size[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            size[pu] += size[pv]
            merged = sorted(top_k[pu] + top_k[pv], reverse=True)
            top_k[pu] = merged[:10]
    elif query_type == '2':
        v = int(data[ptr+1])
        k = int(data[ptr+2])
        ptr += 3
        pv = find(v)
        if len(top_k[pv]) >= k:
            print(top_k[pv][k-1])
        else:
            print(-1)

