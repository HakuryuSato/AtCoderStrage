import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

b = int(input())

if b == 1:
    print(1)
    exit()

for a in range(2, 21):
    temp = b
    count = 0
    while temp % a == 0:
        temp //= a
        count += 1
    if temp == 1 and count == a:
        print(a)
        exit()

print(-1)
