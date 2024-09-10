import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

H,W=map(int,input().split())

A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

for s in range(H):
    for t in range(W):
        ok = True
        for i in range(H):
            for j in range(W):
                if A[(i - s + H) % H][(j - t + W) % W] != B[i][j]:
                    ok = False
        if ok:
            print("Yes")
            exit()
print("No")


# 各行に対して、#の個数がBより多ければYes?
# 縦方向のシフトはどう処理する？.のみの列があれば#の個数だけで良いが、
# 

# a_count=0
# b_count=0

# for i in range(H):
#     a_count+=input().count('#')

# for i in range(H):
#     b_count+=input().count('#')

# if a_count>=b_count:
#     print('Yes')
# else:
#     print('No')

