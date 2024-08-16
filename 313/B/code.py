import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N, M = map(int,input().split())

# 配列かdictで強さリストを作って可算減算して最後に比較？

s=set(range(1,N+1)) # 最強以外入らないset型
for _ in range(M):
  win,lose=map(int,input().split())
  s.discard(lose) # 負けた番号は排除
print(-1 if len(s)!=1 else s.pop()) # もし長さが1以上(複数人いるなら)-1、そうでなければpopで残った番号を削除しつつ、戻り値をprintする。