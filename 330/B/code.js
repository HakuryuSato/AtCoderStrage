const fs = require("fs");
const path = require("path");
const file_number = 1;

// function binary_search(l, r, num) {
//     zero = 0n
//     high = r - num;
//     low = l - num;
//     mid = high - low;

//     while (true) {
//         if (mid >= low) { //midがlow以上なら
            
//         }else{ // midがlow以下なら？

//         }
//     }
// }

function Main(input) {
    input = input.split("\n");
    let [n, l, r] = input[0].split(" ").map(BigInt);
    let a = input[1].split(" ").map(BigInt);

    if (l === r) {
        for (i = 0; i < n; i++) {
            console.log(l);
        }
    } else {
        for (i = 0; i < n; i++) {
            num = a[i]
            for(j=l;j<=r;j++){
                if(j-num>=l && j-num<=r){
                    console.log(j-num)
                }
            }
        }
    }
}

Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
