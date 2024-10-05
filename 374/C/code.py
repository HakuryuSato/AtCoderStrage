import sys
import bisect

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

n=int(input())
k=list(map(int,input().split()))

N1 = n // 2
N2 = n - N1

k1 = k[:N1]
k2 = k[N1:]

total_sum = sum(k)

def get_all_sums(k_list):
    sums = []
    n = len(k_list)
    for mask in range(1 << n):
        s = 0
        for i in range(n):
            if (mask >> i) & 1:
                s += k_list[i]
        sums.append(s)
    return sums

sums1 = get_all_sums(k1)
sums2 = get_all_sums(k2)
sums2.sort()

min_max = total_sum

for s1 in sums1:
    target = total_sum / 2 - s1
    idx = bisect.bisect_left(sums2, target)
    for i in [idx - 1, idx, idx + 1]:
        if 0 <= i < len(sums2):
            s2 = sums2[i]
            s = s1 + s2
            max_s = max(s, total_sum - s)
            if max_s < min_max:
                min_max = max_s

print(int(min_max))
