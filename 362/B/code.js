// テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const file_number= 3
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
points =[]
rl.on("line", (line) => {
    points.push(line.split(" ").map(Number));



    lineCount++;
}).on("close", () => {
    main();
});


function isRightTriangle(points) {
    function distanceSquared(x1, y1, x2, y2) {
        return (x1 - x2) ** 2 + (y1 - y2) ** 2;
    }

    const [x1, y1] = points[0];
    const [x2, y2] = points[1];
    const [x3, y3] = points[2];

    const dAB = distanceSquared(x1, y1, x2, y2);
    const dBC = distanceSquared(x2, y2, x3, y3);
    const dCA = distanceSquared(x3, y3, x1, y1);

    const sides = [dAB, dBC, dCA].sort((a, b) => a - b);

    if(sides[0] + sides[1] === sides[2]){
        return "Yes"
    }else{
        return "No"
    }
}



function main() {
    // console.log(points)
    
    console.log(isRightTriangle(points))
}
