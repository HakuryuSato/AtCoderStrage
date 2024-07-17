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





lineCount = 0;
lines=[];
rl.on("line", (line) => {
    if(line===0){
        return lines
    }else{
        lines.push(Number(line));
    }




    lineCount++;
}).on("close", () => {
    main();
});



function main() {
    // console.log(lines)
    lines.reverse()
    // console.log(lines)
    for(i=0;i<lines.length;i++){
        console.log(lines[i])
    }
 
}
