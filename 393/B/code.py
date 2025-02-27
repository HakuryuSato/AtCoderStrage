import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())


S=list(input())
N = len(S)
ans=0



for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      if j - i == k - j and S[i] == 'A' and S[j] == 'B' and S[k] == 'C':
        ans += 1
print(ans)


# 以下のコードでは、0,2,4などは試せても1,3,5などが抜ける
# for step in range(1,101):
#     before=''
#     for i in range(0,len(S),step):
#         print(S[i])
#         if S[i]=='A':
#             before='A'
#         elif S[i]=='B' and before == 'A':
#             before='B'
#         elif S[i]=='C' and before =='B':
#             before=''
#             ans +=1
#         else:
#             before=''