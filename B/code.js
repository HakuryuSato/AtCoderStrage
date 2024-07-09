// テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const file_number= 0
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
lines=[];
rl.on("line", (line) => {
    S=line



    lineCount++;
}).on("close", () => {
    main();
});


function countChar(text, char) {
    return text.split(char).length - 1;
}

function checkOccurrences(obj) {
    const counts = {};
    for (let key in obj) {
        counts[obj[key]] = (counts[obj[key]] || 0) + 1;
    }

    for (let count of Object.values(counts)) {
        if (count !== 0 && count !== 2) {
            return false;
        }
    }
    return true;
}

function main() {
    // console.log(S)
    wordList = new Set(...S.split(" "))

    duplicationCount = 0
    resultDict = {}
    for (const word of wordList) {
        resultDict[word] = countChar(S, word)        
      }

    //   console.log(resultDict)
    //   console.log(checkOccurrences(resultDict));

      if(checkOccurrences(resultDict)) {
        console.log("Yes")
      } else {
        console.log("No")
      }

}
