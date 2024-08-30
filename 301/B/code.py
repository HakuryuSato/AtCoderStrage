import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())
l = list(map(int, input().split()))

i = 0

while i < len(l) - 1:
    diff = l[i + 1] - l[i]
    if abs(diff) > 1:
        if diff > 0:
            l.insert(i + 1, l[i] + 1)  
        else:
            l.insert(i + 1, l[i] - 1)  
    else:
        i += 1 

print(*l)