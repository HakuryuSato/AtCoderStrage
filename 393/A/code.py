import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())


Takahashi,Aoki = input().split()

if Takahashi == 'sick' and Aoki == 'sick':
    print(1)

if Takahashi == 'sick' and Aoki == 'fine':
    print(2)

if Takahashi == 'fine' and Aoki == 'sick':
    print(3)

if Takahashi == 'fine' and Aoki == 'fine':
    print(4)