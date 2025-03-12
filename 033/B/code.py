import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())


n=int(input())
l=[]
sum_count=0

for _ in range(n):
    name,count = input().split()
    count = int(count)
    l.append([name,count])
    sum_count += count

ans = 'atcoder'
for name,count in l:
    if count > (sum_count/2):
        ans = name

print(ans)