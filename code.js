// const readline = require('readline');
// const fs = require('fs');
// const rl = readline.createInterface({
//     input: fs.createReadStream('input0.txt'),
//     output: process.stdout
// });



// 本番用*************************************************************************
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin, 
    output: process.stdout
}); 
// 本番用*************************************************************************



let lineCount = 0;
let lines = []
rl.on('line', (line) => {
    // console.log(line)
    if (lineCount === 0) {
        [N, M] = line.split(' ').map(Number)
    } else {
        lines.push(line.split(""))
    }



    lineCount++;
}).on('close', () => {
    main();
});




function createAllTypes(M) {
    const allTypes = new Array(M).fill('x');
    return allTypes;
}


// 全ての組み合わせを生成する再帰的関数
function getCombinations(array) {
    const result = [];
    const generateCombinations = (prefix, array) => {
        for (let i = 0; i < array.length; i++) {
            result.push([...prefix, array[i]]);
            generateCombinations([...prefix, array[i]], array.slice(i + 1));
        }
    }
    generateCombinations([], array);
    return result;
}


function checkAllO(array) {
    // 'x'が存在しないことを確認する
    return !array.includes('x');
}


// 最小回数で全てのポップコーンを集められる組み合わせ
function minPopCount(array, allTypesTemp) {

    maxMinCount = Infinity



    array.map((combi) => { // 組み合わせでループ

        // console.log(allTypes)

        allTypes = [...allTypesTemp] // ポップコーン種類初期化


        count = 0 // 購入回数


        combi.map((type) => {
            type.map((t, index) => {
                // console.log(allTypes[index])
                // console.log(allTypes[index],t)
                // console.log(allTypes[index] === 'x' && t === 'o')
                if (allTypes[index] === 'x' && t === 'o') { // もし現在の種類が未購入で店にあるなら

                    allTypes[index] = 'o' // 購入として扱う
                } // 既にoなら何もしない
            })



        })

        // combi.map((val) => console.log(val))

        // console.log(checkAllO(allTypes), combi.length < maxMinCount, combi.length)
        // console.log(allTypes)
        // 購入が終わった時点で全てoかチェックして、
        if (checkAllO(allTypes)) { // もし全てoで

            if (combi.length < maxMinCount) { // そのcombiのほうが小さければ
                maxMinCount = combi.length //conbi配列の長さを最小回数とする
            }

        }


    })

    return maxMinCount
}




function main() {
    // console.log(N,M,lines)
    combinations = getCombinations(lines)
    allTypes = createAllTypes(M)
    min = minPopCount(combinations, allTypes)
    console.log(min)

}