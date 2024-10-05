import sys
import math
import itertools

# ローカル用
# file_number = 4 
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 提出用
sys.stdin = sys.__stdin__

n,s,t = list(map(int,input().split()))
segments = []
points = [(0.0, 0.0)]

for _ in range(n):
    a, b, c, d = map(float, sys.stdin.readline().split())
    segments.append(((a, b), (c, d)))
    points.append((a, b))
    points.append((c, d))

num_points = len(points)
dist = [[0.0] * num_points for _ in range(num_points)]
for i in range(num_points):
    x1, y1 = points[i]
    for j in range(num_points):
        x2, y2 = points[j]
        dx = x1 - x2
        dy = y1 - y2
        dist[i][j] = math.hypot(dx, dy)

point_indices = {}
for idx, point in enumerate(points):
    point_indices[point] = idx

min_time = float('inf')

for perm in itertools.permutations(range(n)):
    for bitmask in range(1 << n):
        total_time = 0.0
        curr_point = (0.0, 0.0)
        curr_idx = point_indices[curr_point]
        valid = True

        for idx_in_perm in perm:
            segment = segments[idx_in_perm]
            if (bitmask >> idx_in_perm) & 1:
                start_point, end_point = segment[0], segment[1]
            else:
                start_point, end_point = segment[1], segment[0]

            start_idx = point_indices[start_point]
            end_idx = point_indices[end_point]

            move_dist = dist[curr_idx][start_idx]
            time_move = move_dist / s
            total_time += time_move

            print_dist = dist[start_idx][end_idx]
            time_print = print_dist / t
            total_time += time_print
            curr_idx = end_idx

        if total_time < min_time:
            min_time = total_time

print('{0:.10f}'.format(min_time))
