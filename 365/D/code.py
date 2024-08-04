import sys

# ローカル用
file_number = 3
sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
# sys.stdin = sys.__stdin__


N = int(input())
S = list(input())

count=0
takahashi = {'R':True, 'S':True, 'P':True}
previous_move = 'P' if S[0] == 'R' else ('R' if S[0] == 'S' else 'S')

for s in S:
    # 高橋の現在の動きを決定
    if s == 'R' and takahashi['P']:
        current_move = 'P'
    elif s == 'R' and takahashi['R']:
        current_move = 'R'
    elif s == 'S' and takahashi['R']:
        current_move = 'R'
    elif s == 'S' and takahashi['S']:
        current_move = 'S'
    elif s == 'P' and takahashi['S']:
        current_move = 'S'
    elif s == 'P' and takahashi['P']:
        current_move = 'P'
    else:
        continue
    
    count += 1 if (s == 'R' and current_move == 'P') or (s == 'S' and current_move == 'R') or (s == 'P' and current_move == 'S') else 0

    takahashi[previous_move] = True
    takahashi[current_move] = False
    previous_move = current_move

print(count)