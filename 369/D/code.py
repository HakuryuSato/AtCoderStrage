import sys

# ローカル用
file_number = 1
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
# sys.stdin = sys.__stdin__

N=int(input()) 
A=list(map(int,input().split())) 





dp_odd = 0 
dp_even = 0 

for i in range(N):
    new_dp_odd = max(dp_odd, dp_even + A[i])  
    new_dp_even = max(dp_even, dp_odd + A[i] * 2)  
    dp_odd, dp_even = new_dp_odd, new_dp_even 

print(max(dp_odd, dp_even))
