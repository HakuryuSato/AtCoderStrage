import sys

# ローカル用
# file_number = 3
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

def read_values(): return map(int, input().split())
def read_list(): return list(read_values())

N=int(input())
TASKS = [read_list() for _ in range(N)] # 10^5

sorted_TASKS = sorted(TASKS,key=lambda x:x[1]) # 10^5


current_time=0

for task in sorted_TASKS: # 10^5
    time=task[0]
    limit=task[1]

    current_time += time
    
    if current_time > limit:
        print('No')
        exit()


    
    
print('Yes')