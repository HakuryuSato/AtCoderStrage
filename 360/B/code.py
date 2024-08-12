import sys

# ローカル用
file_number = 1
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
# sys.stdin = sys.__stdin__

S,T = input().split()

def check(S, T):
    s_len = len(S)
    t_len = len(T)

    for w in range(1, s_len):
        for c in range(w):
            now = ""
            for i in range(c, s_len, w):
                now += S[i]
            if now == T:
                return "Yes"
    return "No"


print(check(S,T))