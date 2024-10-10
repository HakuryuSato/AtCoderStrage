import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

S=input()

count_0 = S.count('0')
count_1 = S.count('1')

max_pairs = min(count_0, count_1)

print(max_pairs * 2)



'''
S=0と1からなる長さ1~10^5のデータ
01または10の場合、その二つを取り除く(除外データ+2)
最大で何個のデータを取り除けるか？

'''