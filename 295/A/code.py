import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__
N=int(input())
W=list(input().split())
text = ['and', 'not', 'that', 'the', 'you']
print('Yes' if any(word in text for word in W) else 'No')