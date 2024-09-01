# Main folder name input
read -p "ディレクトリ名を入力: " mainfolder

# Create the main directory
mkdir -p "$mainfolder"

# Subdirectories to be created inside the main folder
directories=("A" "B" "C" "D" "E")

# Create each subdirectory inside the main folder and copy template contents
# for dir in "${directories[@]}"; do
#     mkdir -p "$mainfolder/$dir"
#     cp -r ./template/* "$mainfolder/$dir/"
# done

for dir in "${directories[@]}"; do
    # 各サブディレクトリを作成
    mkdir -p "$mainfolder/$dir"
    for file in ./template/*; do
        # コピー先のファイルパスを設定
        target_file="$mainfolder/$dir/$(basename "$file")"
        # ファイルが存在しない場合のみコピー
        if [ ! -e "$target_file" ]; then
            cp "$file" "$target_file"
        fi
    done
done

# Declare associative array for storing times
declare -A times

while true; do
  echo "アルファベットA~Hを入力してストップウォッチを開始します (終了するにはend):"
  read input

  if [ "$input" == "end" ]; then
    break
  fi

  if [[ "$input" =~ ^[A-H]$ ]]; then
    start_time=$(date +%s)
    echo "Enterを押して時間計測を終了します..."
    read
    end_time=$(date +%s)
    elapsed_time=$(( (end_time - start_time) / 60 ))
    times[$input]=$elapsed_time
    echo "$input: $elapsed_time 分"
  else
    echo "無効な入力です。A~Hの範囲で入力してください。"
  fi
done

output="AtCoderABC${mainfolder}(Py"
for key in A B C D E F G H; do
  if [[ -n "${times[$key]}" ]]; then
    output+=" $key:${times[$key]}分"
  fi
done
output+=")"

echo "$output" >  "${mainfolder}/time.txt"
echo "結果が time.txt に保存されました。"
read -p "終了するにはEnterキーを押してください..."