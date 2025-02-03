import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

data = sys.stdin.read().splitlines()

n, q = map(int, data[0].split())
queries = data[1:]

pigions = {i: i for i in range(1, n + 1)}
holes = {i: 1 for i in range(n + 1)}
count = 0

for query in queries:
    if query.split()[0] == "1":
        _, pigion_no, hole_no = map(int,(query.split()))
        prev_hole_no = pigions[pigion_no]

        if holes[prev_hole_no]==2:
            count-=1
        holes[prev_hole_no]-=1

        if holes[hole_no]==1:
            count+=1
        
        holes[hole_no]+=1

        pigions[pigion_no]=hole_no

    else:
        print(count)
