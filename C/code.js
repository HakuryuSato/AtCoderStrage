// テスト用 ---------------------------------------------------------------------------------------------------
const readline = require("readline");
const fs = require("fs");
const path = require("path");

const file_number = 0;
const file = `input${file_number}.txt`;

const rl = readline.createInterface({
    input: fs.createReadStream(path.join(__dirname, file)),
    output: process.stdout,
});

// テスト用 ---------------------------------------------------------------------------------------------------

// // 本番用 ---------------------------------------------------------------------------------------------------
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });
// // 本番用 ---------------------------------------------------------------------------------------------------

lineCount = 0;
lines = [];
rl.on("line", (line) => {
    if (lineCount === 0) {
        N = Number(line);
    } else {
        num = line.split(" ").map(Number);
    }

    lineCount++;
}).on("close", () => {
    main();
});

function calcPow(exponents) {
    return exponents.map((n) => Math.pow(2, n));
}

function calcLog(values) {
    return values.map((n) => Math.log2(n));
}

function main() {
    // console.log(N, num);
    // num = num.map((n) => Math.pow(2, n));
    // console.log(num);

    ball_lines = [];

    for (i = 0; i < N; i++) {
        let ballSize = 2 ** num[i];
        ball_lines.push(ballSize);
        
        if (num.length <= 1) { //1つ以下なら終了
            break;
        } else { // 2つ以上なら
            const last_ball = ball_lines[ball_lines.length - 1];
            const second_last_ball = ball_lines[ball_lines.length - 2];
            console.log(last_ball, second_last_ball);

            if (last_ball === second_last_ball) { //等しいならば
                ball_lines.pop();
                ball_lines.pop();
                ball_lines.push(last_ball + second_last_ball);
            } else { //異なるならば
                console.log("異なる");
                break;
            }
        }

               
    }

    // numの場合  -------------------------------------------------

    // console.log(ball_lines.reduce((a, b) => a + b));

    // console.log(N, num);
    // num = num.map((n) => Math.pow(2, n));
    // console.log(num);

    // for (let i = 0; i < N; i++) {
    //     console.log(num)
    //     if (num.length <= 1) break; //1つ以下なら終了

    //     const last_ball = num[num.length - 1];
    //     const second_last_ball = num[num.length - 2];
    //     console.log(last_ball, second_last_ball);

    //     if (last_ball === second_last_ball) {
    //         num.pop();
    //         num.pop();
    //         num.push(last_ball + second_last_ball);
    //     } else {
    //         console.log("異なる");
    //         break;
    //     }
    // }
}
