const fs = require("fs");
const path = require("path");
const file_number = 3;

function initialize(H, W) {
    list = [];
    for (i = 0; i < H; i++) {
        line = [];
        for (j = 0; j < W; j++) {
            line.push(".");
        }
        list.push(line);
    }

    return list;
}

function checkColor(grid) {
    if (grid === ".") {
        return ["#", 1];
    } else {
        return [".", -1];
    }
}

function getNewPosition(x, y, direction) {
    switch (direction) {
        case 0: // 上
            return [x - 1, y];
        case 1: // 右
            return [x, y + 1];
        case 2: // 下
            return [x + 1, y];
        case 3: // 左
            return [x, y - 1];
        default:
            return [x, y];
    }
}

function getNewDirection(currentDirection, step) {
    return (currentDirection + step + 4) % 4;
}

function editTable(N, field) {
    if (N === 0) {
        return field;
    }

    // 1回目の処理
    // field[0][0] = "#";
    let currentGrid = [0, 0];
    let direction = 0;

    for (i = 0; i < N; i++) {
        // 現在のマスチェック 色適用
        let currentValue = field[currentGrid[0]][currentGrid[1]];
        let [newColor, step] = checkColor(currentValue);

        field[currentGrid[0]][currentGrid[1]] = newColor;
        direction = getNewDirection(direction, step);

        [currentGrid[0], currentGrid[1]] = getNewPosition(
            currentGrid[0],
            currentGrid[1],
            direction,
        );
    }

    return field;
}

function Main(input) {
    input = input.split("\n");
    [H, W, N] = input[0].split(" ");
    let field = initialize(H, W);
    console.log(field);

    console.log(editTable(N, field));
}

Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
