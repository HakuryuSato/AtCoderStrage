import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'

N = int(input())

print(pi[:N+2])
