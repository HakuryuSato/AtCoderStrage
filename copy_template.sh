# Main folder name input
read -p "Enter the main folder name: " mainfolder

# Create the main directory
mkdir -p "$mainfolder"

# Subdirectories to be created inside the main folder
directories=("A" "B" "C" "D" "E")

# Create each subdirectory inside the main folder and copy template contents
for dir in "${directories[@]}"; do
    mkdir -p "$mainfolder/$dir"
    cp -r ./template/* "$mainfolder/$dir/"
done
