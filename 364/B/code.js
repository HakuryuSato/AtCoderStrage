const fs = require("fs");
const path = require("path");
const file_number = 2;

function moveXY(char, x, y) {
    switch (char) {
        case "L":
            x--;
            break;
        case "R":
            x++;
            break;
        case "U":
            y--;
            break;
        case "D":
            y++;
            break;
    }
    return [x, y];
}

function Main(input) {
    input = input.split("\n");
    let [H, W] = input[0].split(" ").map(Number);
    let [Si, Sj] = input[1].split(" ").map(Number);
    let field = input.slice(2, input.length - 2);
    let X = input[input.length - 2];

    let x = Sj-1;
    let y = Si-1;

 

    for (let char of X) {

        let [nextX, nextY]  = moveXY(char,x,y)

        if ((nextX >= 0 && nextX < field[0].length && nextY >= 0 && nextY < field.length) && field[nextY][nextX] == '.') {// 範囲から出ない、かつ'.'なら
            x=nextX
            y=nextY
        }
    }

    console.log(y+1,x+1)
}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
