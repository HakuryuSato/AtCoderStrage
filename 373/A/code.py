import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

# 実行時間2秒 メモリ1GB

sumcount=0
for i in range(12):
    if len(input())==i+1:
        sumcount+=1

print(sumcount)


