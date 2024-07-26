const fs = require("fs");
const path = require("path");
const file_number = 2;

function Main(input) {
    input = input.split("\n");
    let [k, g, m] = input[0].split(" ").map(Number);

    let gml = 0;
    let mml = 0;
    for (i = 0; i < k; i++) {
        if (gml === g) {
            gml = 0;
        } else if (mml === 0) {
            mml = m;
        } else {
            if (mml + gml >= g) {
                mml -=  (g - gml);
                gml += (g - gml);
            } else {
                gml += mml;
                mml = 0;
            }
        }
    }

    console.log(gml,mml)
}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
