import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__


M = int(input())
powers_of_3 = [3**i for i in range(11)]

A = []
remaining = M

for i in reversed(range(11)):
    while remaining >= powers_of_3[i]:
        A.append(i)
        remaining -= powers_of_3[i]

print(len(A))
print(*A)


# M = int(input())
# N = 20
# l = [3**i for i in range(11)] 
# found = False
# def check(A):
#     return sum(l[A_i] for A_i in A) == M
# for n in range(1, N+1):
#     max_value = 11 ** n
#     for i in range(max_value):
#         A = [(i // (11 ** j)) % 11 for j in range(n)]
#         if check(A):
#             print(n)
#             print(*A)
#             found = True
#             break
#     if found:
#         break
# 間に合わない、逆にMから逆算？
