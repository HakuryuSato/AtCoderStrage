import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N=int(input())
l=[0]*N

for i in range(N):
    text=list(input().split())
    l[i]=[int(text[0]),text[1]]


left_keys = [pos for pos, hand in l if hand == 'L']
right_keys = [pos for pos, hand in l if hand == 'R']

if len(left_keys) > 1:
    result_left = sum(abs(left_keys[i] - left_keys[i - 1]) for i in range(1, len(left_keys)))
else:
    result_left = 0 
if len(right_keys) > 1:
    result_right = sum(abs(right_keys[i] - right_keys[i - 1]) for i in range(1, len(right_keys)))
else:
    result_right = 0  

result = result_left + result_right 
print(result)