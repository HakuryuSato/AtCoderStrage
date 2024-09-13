import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__


# 長さNの0と1からなる文字列Sがある、S[1]=0,S[N]=1を満たす
# 質問を20回まで行える
# 1<=p<=N-1かつ、S[p]!=S[p+1]を満たす整数pを1個出力　(つまり、Sの連続するインデックスで、値が異なる部分を見つける)
# 2<=N<=2*10^5

# N=int(input()) # 2~2*10^5

# # 質問の形式 "? i" を標準出力 ここで20回ループか？
# print("? 2")

# # S[i]の応答が返ってくる
# input() # 0 または 1

# # 正解が分かったら解答
# print("! 2")

# # プログラムを終了
# exit()


def query(pos):
    print(f"? {pos}\n")
    sys.stdout.flush()  
    response = input().strip()
    return int(response)

def find_position(N):
    left, right = 1, N

    while left < right:
        mid = (left + right) // 2
        s_mid = query(mid)

        if s_mid == 0:
            left = mid + 1
        else:
            right = mid

    print(f"! {left}\n")
    sys.stdout.flush()

N = int(input())
find_position(N)

exit()