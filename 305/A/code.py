import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N = int(input())

if(N%5<=2):
    print(N-N%5)
    
else:
    print(N+(5-N%5))