import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

# ダンゴ文字列の定義：先頭or末尾に'-'が一つ、他はo 例)ooo- レベル3のダンゴ文字列
# Sの連続する部分文字列であって、レベルXのダンゴ文字列であるものが存在するなら、最大値を出力、存在しないなら-1を出力
# ランレングス圧縮して、最大のoを出力？

N=int(input()) # 10
S=input() # o-oooo---o

max_level = -1
current_o_count = 0
found_dash = False

def max_dango_level(S):
    # 'o'と'-'が両方存在するかチェック
    if 'o' not in S or '-' not in S:
        return -1

    max_level = -1
    current_o_count = 0
    has_dash_before = False

    for i in range(len(S)):
        char = S[i]
        if char == 'o':
            current_o_count += 1
        elif char == '-':
            if current_o_count > 0:
                if has_dash_before or (i > 0 and S[i - 1] == 'o'):
                    max_level = max(max_level, current_o_count)
                current_o_count = 0
            has_dash_before = True

    # 最後のチェック
    if current_o_count > 0 and has_dash_before:
        max_level = max(max_level, current_o_count)
    return max_level

print(max_dango_level(S))