// テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const file_number = 1;
// const file = `input${file_number}.txt`;

// const rl = readline.createInterface({
//     input: fs.createReadStream(path.join(__dirname, file)),
//     output: process.stdout,
// });

// テスト用 ---------------------------------------------------------------------------------------------------

// // 本番用 ---------------------------------------------------------------------------------------------------
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
// // 本番用 ---------------------------------------------------------------------------------------------------

lineCount = 0;
lines = [];
rl.on("line", (line) => {
    if (lineCount === 0) {
        [N, A, B] = line.split(" ").map(Number);
    } else {
        lines = line.split(" ").map(Number);
    }

    lineCount++;
}).on("close", () => {
    main();
});

function isHolidays(day, holidays) {
    return holidays.some((holiday) => day % holiday === 0); // 休日リストで割り切れるか？ => 割り切れるなら休日なのでTrue
}

function main() {
    console.log(N, A, B, lines);
    // 休日:1~A日目
    // 平日:A+1日目~A+B日目
    // 割り切れるかどうか？
    // 平日リスト 休日かどうかだけ判定すればよい
    // weekdays = [];
    // 休日リスト
    holidays = [];

    for (i = 1; i <= A; i++) {
        holidays.push(i);
    }
    // for (i = A + 1; i <= A + B; i++) {
    //     weekdays.push(i);
    // }

    console.log(holidays);

    let result = lines.some((day) => {
        isHolidays(day, holidays);
    });

    if (result) { //休日が含まれるなら
        console.log("No");
    } else {
        console.log("Yes");
    }
}
