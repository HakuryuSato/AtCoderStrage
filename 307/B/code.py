import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__


def check(text):
    return text == text[::-1]

N = int(input())
S = [input() for _ in range(N)]

is_in_palindrome = False
for i in range(len(S)-1):
    for j in range(i+1,len(S)):
        if(check(S[i]+S[j]) or check(S[j]+S[i])):
            is_in_palindrome = True


print('Yes' if is_in_palindrome else 'No')