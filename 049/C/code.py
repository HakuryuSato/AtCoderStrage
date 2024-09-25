import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

# 実行時間2秒 メモリ1GB

S=input()
add_strings=['dream', 'dreamer' ,'erase' ,'eraser']

# Tの文字列に、add_stringsのいずれかを追加することで、S=Tとすることができるか？
# 判定し、YES or NO を出力
# ただしS=1~10^5

# 考察
# Sの文字列が、全てadd_stringsの部分文字列で表現されているかを調べる？
# たかだか10^5なので、前からループしていって、1~7文字を抽出して、add_stringsの中の値と一致するか、もしいずれにも一致しなければ、ループ中断してNO？
# 不足：手前からだとdreamerがdreamの時点で終了してしまう、逆順に判定する必要がある


S = S[::-1]
add_strings = [s[::-1] for s in add_strings]

i = 0
while i < len(S):
    matched = False
    for add in add_strings:
        if S[i:i+len(add)] == add:
            i += len(add) 
            matched = True
            break
    if not matched:
        print("NO")
        break
else:
    print("YES")


