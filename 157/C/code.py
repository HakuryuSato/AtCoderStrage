import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N, M = map(int, input().split())  # M = 3, N = 3
l = []


for i in range(M):
    l.append(list(map(int, input().split())))

# l = [[1, 7], [3, 2], [1, 7]]



def check(l):
    if M == 0:
        if N == 1:
            return 0
        elif N == 2:
            return 10
        elif N == 3:
            return 100

    if isinstance(l[0], int):
        l = [l]

    for i in range(1000):
        i_str = str(i)

        if len(i_str) != N:
            continue

        try:
            if all(i_str[digit - 1] == str(number) for digit, number in l):
                return i
        except IndexError:
            continue

    return -1


print(check(l))
