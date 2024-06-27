const readline = require('readline');
const fs = require('fs');
const rl = readline.createInterface({
    input: fs.createReadStream('input1.txt'),
    output: process.stdout
});



// // 本番用*************************************************************************
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin, 
//     output: process.stdout
// }); 
// // 本番用*************************************************************************



let lineCount = 0;
let lines = []
rl.on('line', (line) => {
    N = Number(line)


    lineCount++;
}).on('close', () => {
    main();
});

function isNZero(N) {
    return N === 0
}

function createCarpet() {
    return ["###", "#.#", "###"]
}

function outPutCarpet(carpet) {
    for (let subCarpet of carpet) {
        for (let row of subCarpet) {
            console.log(row);
        }
    }
}



function main() {
    // console.log(N)
    if (isNZero(N)) { // レベル0なら1x1マス
        console.log('#')
    } else {
        allCarpet = []


        loop = 3 ** N // ループ数
        centerNumber = Math.floor(loop / 2) // 中央
        for (i = 1; i <= loop; i++) { //　カーペットレベル分ループ


            if (i % 3 === 0) { // もし3の倍数なら
                // 次の配列に入れる
                outPutCarpet(allCarpet)
            } else {

            }
            // console.log(i)




        }




    }


}