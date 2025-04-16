import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


N = int(input())

is_loggedin = False
ans=0

for _ in range(N):
    S = input()
    if S == "login":
        is_loggedin = True
    elif S == "logout":
        is_loggedin = False
    elif S == "private" and not is_loggedin:
        ans+=1

print(ans)