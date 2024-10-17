import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 本番用
sys.stdin = sys.__stdin__


N = int(input())
H = list(map(int, input().split()))
T = 0

for h in H:
    num = h // 5
    T += num * 3
    h -= num * 5

    while h > 0:
        T += 1
        if T % 3 == 0:
            h -= 3
        else:
            h -= 1

print(T)

"""
[問題文]
実行時間制限: 2 sec / メモリ制限: 1024 MB

N人の敵が並んでおり、前からi番目の敵の体力はHi
0で初期化された変数Tを使い、全ての敵の体力が0以下になるまで以下を繰り返す
Tを1増やす、その後体力が1異常である最も前の敵を攻撃、
このときTが3の倍数ならばその敵の体力は3減り、そうでないなら1減る

全ての敵の体力が0以下になった時のTの値を求めよ
N=1~2*10^5
H=1~10^9

[私の考え]
そのままループしたら間に合わないので、5?などで割ったあまりなどから答えを計算する

"""
