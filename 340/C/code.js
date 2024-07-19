const fs = require("fs");
const path = require("path");
const file_number = 2;

function ceilBigInt(x, y) { // 切り上げ
    let remainder = x % y;
    if (remainder === 0n) {
        return x / y;
    } else if (x > 0n) {
        return (x - remainder + y) / y;
    } else {
        return (x - remainder) / y;
    }
}

function floorBigInt(x, y) { //切り捨て
    let remainder = x % y;
    if (remainder === 0n) {
        return x / y;
    } else if (x > 0n) {
        return (x - remainder) / y;
    } else {
        return (x - remainder - y) / y;
    }
}


function sumUsingGauss(n) {
    let sum = BigInt(0);
    for (let k = BigInt(1); k <= n; k++) {
        let halfK = k / BigInt(2);
        if (halfK >= BigInt(2)) {
            sum += halfK;
        }
    }
    return sum;
}


function Main(input) {
    input = input.split("\n");
    const N = BigInt(input[0]);
    result = (N * (N + 1n)) / 2n;

    sum=0n;

    // while (N >= 2n) {
    //     let half1 = ceilBigInt(N,2n)
    //     let half2 = floorBigInt(N,2n)

    //     if (half1 >= 2n) sum += half1;
    //     if (half2 >= 2n) sum += half2;

    //     N = half1; // 次のループのためにnを更新
    // }


    console.log(sumUsingGauss(BigInt(N)).toString());
}



Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
