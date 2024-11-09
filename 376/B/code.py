import sys

# ローカル用
# file_number = 1 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

# 
def calculate_steps(total_parts, start, end, restricted):
    if start > end:
        start, end = end, start
    if start < restricted < end:
        return total_parts + start - end
    else:
        return end - start
    
# N パーツ数、Q クエリ数
n, q = map(int, input().split())
left_position, right_position = 1, 2
operation_count = 0

for _ in range(q):
    direction, target_position = input().split()
    target_position = int(target_position)
    if direction == 'L':
        operation_count += calculate_steps(n, left_position, target_position, right_position)
        left_position = target_position
    else:
        operation_count += calculate_steps(n, right_position, target_position, left_position)
        right_position = target_position

print(operation_count)