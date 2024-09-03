import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

num_dict = {}

N = int(input())

for i in range(N):
    num = int(input())
    num_dict[num] = num_dict.get(num, 0) + 1


count=0
for i in num_dict:
    if(num_dict[i]%2 == 1):
        count+=1

print(count)