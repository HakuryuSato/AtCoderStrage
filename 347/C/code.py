import sys

# ローカル用
file_number = 3
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
# sys.stdin = sys.__stdin__

N,A,B = map(int,input().split())
D=list(map(int,input().split()))

# 各予定の日付を、1週間の日数で割った余りに変換
D = [d % (A+B) for d in D]

# 予定の日付を昇順にソート
D.sort()

# 隣り合う予定の間隔を計算
diffs = []
for i in range(N-1):
    diffs.append(D[i+1] - D[i])
diffs.append((A+B) - D[-1] + D[0]) # 最後の予定と最初の予定の間隔も考慮する

# 間隔の最大値が平日の日数より大きければYes
if max(diffs) > B:
    print("Yes")
else:
    print("No")