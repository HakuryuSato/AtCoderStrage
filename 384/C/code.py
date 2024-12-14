import sys
from itertools import combinations

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__


input_list = list(map(int, input().split()))
l = list(zip(["A", "B", "C", "D", "E"], input_list))
all_combinations = [list(combinations(l, i)) for i in range(1, 6)]

result = []
for combination in all_combinations:
    for comb in combination:
        questions_text = ""
        score = 0
        for c in comb:
            questions_text += str(c[0])
            score += c[1]

        result.append((questions_text, score))

soreted_result = sorted(result,key=lambda x:(-x[1],x[0]))

for item in soreted_result:
    print(item[0])
