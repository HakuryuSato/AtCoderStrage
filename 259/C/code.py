import sys

# ローカル用
# file_number = 1
# sys.stdin = open(f'input{file_number}.txt', 'r')

# # 本番用
sys.stdin = sys.__stdin__


S=input() #abbaac や xyzz
T=input() #abbbbaaac や xyyzz
 
# Sに対して、2以上の連続する部分文字列には、同じ文字を追加することができる
# SとTを同じにすることは可能かどうかYesまたはNoで出力せよ

# ランレングス圧縮
def rle_encode(s):
    encoded = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append((s[i - 1], count))
            count = 1
    encoded.append((s[-1], count))
    return encoded

encoded_S = rle_encode(S)
encoded_T = rle_encode(T)

# 全要素比較後、各要素比較
if len(encoded_S) != len(encoded_T):
    print("No")
else:
    for (char_S, count_S), (char_T, count_T) in zip(encoded_S, encoded_T):
        if char_S != char_T or count_S > count_T or (count_S < count_T and count_S < 2):
            print("No")
            break
    else:
        print("Yes")
