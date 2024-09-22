import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__


data = sys.stdin.read().split()
N = int(data[0])
Q = int(data[1])
S = list(data[2])

queries = data[3:]

def count_abc_in_range(s, start, end):
    count = 0
    for i in range(start, min(end, N - 2)):
        if s[i] == 'A' and s[i + 1] == 'B' and s[i + 2] == 'C':
            count += 1
    return count

total = count_abc_in_range(S, 0, N)

for q in range(Q):
    X = int(queries[2 * q]) - 1
    C = queries[2 * q + 1]

    start = max(0, X - 2)
    end = min(N, X + 3)

    total -= count_abc_in_range(S, start, end)

    S[X] = C

    total += count_abc_in_range(S, start, end)
    print(total)


"""
メモ
毎回ABCをカウントすると間に合わないので、
最初にトータルをカウントし、
変更があったら変更文字の前後6文字を抽出してABCがあるかチェック、
変更を適用する前後でtotalを計算する。
計算量はO(Q)？

"""