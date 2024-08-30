import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__

N=int(input())
S=input()

aoki=S.count('A')
takagi=S.count('T')

if(aoki > takagi):
    print('A')
elif(takagi>aoki):
    print('T')
else:
    aoki_count=0    
    takagi_count=0
    for s in S:
        if(s=='A'):
            aoki_count+=1
        else:
            takagi_count+=1
        
        if(aoki_count==aoki):
            print("A")
            break
        elif(takagi_count==takagi):
            print("T")
            break



