import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__


def differ_by_one(s1, s2):
    count = 0
    for a, b in zip(s1, s2):
        if a != b:
            count += 1
    return count == 1

def generate_permutations(arr, l, r):
    if l == r:
        yield arr[:]
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]
            yield from generate_permutations(arr, l + 1, r)
            arr[l], arr[i] = arr[i], arr[l]

N, M = map(int, input().split())
l = [input().strip() for _ in range(N)]

found = False

for perm in generate_permutations(l, 0, N - 1):
    is_valid = True
    for i in range(N - 1):
        if not differ_by_one(perm[i], perm[i + 1]):
            is_valid = False
            break
    if is_valid:
        found = True
        break

if found:
    print("Yes")
else:
    print("No")