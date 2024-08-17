import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__

N, K = map(int, input().split())
R = list(map(int, input().split()))

#辞書順条件
#1.総和が同じ
#2.重複しない？

#全探索前提？
#Rが最大値、1からRまで
#総和%K == 0 がtrue

#再帰関数か？
def generate_sequences(sequence, index, total_sum):
    #基底ケース
    if index == N: 
        #総和%K == 0の数列のみ
        if total_sum % K == 0:
            print(" ".join(map(str, sequence)))
        return
    
    #1からRまで
    for i in range(1, R[index] + 1):
        sequence[index] = i
        generate_sequences(sequence, index + 1, total_sum + i)

sequence = [0] * N
generate_sequences(sequence, 0, 0)