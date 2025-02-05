import sys

# ローカル用
# file_number = 2
# sys.stdin = open(f"input{file_number}.txt", "r")

# # 提出用
sys.stdin = sys.__stdin__

dict = {
    "N": "S",
    "E": "W",
    "S": "N",
    "W": "E",
    "NE": "SW",
    "NW": "SE",
    "SE": "NW",
    "SW": "NE",
}

D=input()

print(dict[D])