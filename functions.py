# ランレングス圧縮
def run_length_encoding(S):
    r, c = [], 1
    for i in range(1, len(S)):
        if S[i] == S[i-1]: c += 1
        else: r.append((S[i-1], c)); c = 1
    return r + [(S[-1], c)]




# 4方向
directions = [(0,1),(1,0),(-1,0),(0,-1)]