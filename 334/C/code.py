import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

a,m,l,r = map(int,input().split())

start_flag = max(l, a + ((l - a + m - 1) // m) * m)
end_flag = min(r, a + ((r - a) // m) * m)

if start_flag > end_flag:
    print(0)
else:
    count = (end_flag - start_flag) // m + 1
    print(count)






'''
a,l,r =-10^18~10^18
M=1~10^9

数直線がある、座標Aを基準にして、Lと<=Rの間にMmおきに何本旗を立てられるか？
'''