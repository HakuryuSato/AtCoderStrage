import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N=int(input()) # 3
l = list(map(int,input().split())) # [3, 4, 6]

# def calc(m,l):
#     sum=0
#     for num in l:
#         sum+= m % num

#     return sum


# max_num = max(l)
# max_m = 0


# for m in range(max_num+1):
#     current = calc(m,l)
#     max_m = max(current,max_m)

print(sum(num-1 for num in l))

