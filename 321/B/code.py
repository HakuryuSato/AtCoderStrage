import sys

# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')
sys.stdin = sys.__stdin__

N,X = map(int,input().split())
A = list(map(int,input().split()))
A.append(-1)
for last in range(0,101):
    B = A.copy()
    B[N-1] = last
    sum = 0
    ma = 0
    mi = 100
    for p in B:
        sum += p
        ma = max(ma,p)
        mi = min(mi,p)
    score = sum - ma - mi
    if score >= X:
        print(last)
        exit()
    
print("-1")