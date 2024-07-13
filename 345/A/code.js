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
lines=[];
rl.on("line", (line) => {
    S=line


    lineCount++;
}).on("close", () => {
    main();
});

function checkAllow(S){

    for(let i=0;i<S.length;i++){
        if(i==0){
            if(!(S[i]==='<')){
                return "No"
            }
        }else if(i==S.length-1){
            if(!(S[i]==='>')){
                return "No"
            }
        }else{
            if(!(S[i]==='=')){
                return "No"
            }
        }
    }

    return "Yes"
    

}



function main() {
    console.log(checkAllow(S))
    
}
