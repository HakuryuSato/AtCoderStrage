import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())
A = list(map(int,input().split()))


first_occurrence = {}
result = []


for i, a in enumerate(A):
    if a in first_occurrence:
        if first_occurrence[a] == -1:
            continue  
        result.append([a, i])
        first_occurrence[a] = -1  # 
    else:
        first_occurrence[a] = i 

sorted_result = sorted(result, key=lambda x: x[1])
print(*[row[0] for row in sorted_result])