const readline = require("readline");
const fs = require("fs");
const path = require("path");
const { maxHeaderSize } = require("http");

// // 本番用 ---------------------------------------------------------------------------------------------------
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });
// // 本番用 ---------------------------------------------------------------------------------------------------

// テスト用 ---------------------------------------------------------------------------------------------------
for (let i = 0; i <= 0; i++) { // ファイルでループ
    const file = `input${i}.txt`;

    const rl = readline.createInterface({
        input: fs.createReadStream(path.join(__dirname, file)),
        output: process.stdout,
    });

    let lineCount = 0;
    lines = [];
    rl.on("line", (line) => {
        if (lineCount === 0) {
            N = Number(line);
        } else {
            lines.push(line.split(" ").map(Number));
        }

        lineCount++;
    }).on("close", () => {
        main();
    });
}
// テスト用 ---------------------------------------------------------------------------------------------------

function main() {
    // console.log(N)
    // 最大の頭の値を取得
    const maxHead = Math.max(...lines.map((gigant) => gigant[1]));

    // 最大の頭の値を持つ行をフィルタリング
    const maxHeadRows = lines.filter((gigant) => gigant[1] === maxHead);

    // 全ての頭が同じか確認
    const allHeadsSame = lines.every((gigant) => gigant[1] === lines[0][1]);

    let result;

    if (allHeadsSame) {
        // 全ての頭が同じ場合、全ての行を足してからhead-shoulderした値を代入
        const totalShoulder = lines.reduce((sum, gigant) => sum + gigant[0], 0);
        const totalHead = lines.reduce((sum, gigant) => sum + gigant[1], 0);
        result = totalHead - totalShoulder;
    } else {
        // 各gigantの肩の合計
        const totalShoulder = lines.reduce((sum, gigant) => sum + gigant[0], 0);

        // 最大の頭を持つgigantの肩の合計
        const maxShoulder = maxHeadRows.reduce(
            (sum, gigant) => sum + gigant[0],
            0,
        );

        // 最大の頭を持つgigantのうち、最後のgigantの肩
        const lastMaxShoulder = maxHeadRows[maxHeadRows.length - 1][0];

        // 結果を計算
        result = maxHead - (totalShoulder - maxShoulder + lastMaxShoulder);
    }

    console.log(result);
}
