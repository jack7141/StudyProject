"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// Hash import
const CryptoJS = require("crypto-js");
class Block {
    // 생성자 
    constructor(
    // 인자
    index, hash, previousHash, data, timestamp) {
        this.index = index;
        this.hash = hash;
        this.previousHash = previousHash;
        this.data = data;
        this.timestamp = timestamp;
    }
}
// return값 string으로 명시!
// 값을 해쉬값으로 변환
Block.calculateBlockHash = (index, previousHash, timestamp, data) => CryptoJS.SHA256(index + previousHash + timestamp + data).toString();
// 블록 조건 충족여부 체크
Block.valiableStrcture = (thisBlock) => typeof thisBlock.index === "number" &&
    typeof thisBlock.hash === "string" &&
    typeof thisBlock.previousHash === "string" &&
    typeof thisBlock.timestamp === "number" &&
    typeof thisBlock.data === "string";
// FirstBlock은 Block속성만 받을 수 있게 명시!
const FirstBlock = new Block(0, "2020202020202", "", "Hello", 123456);
// 설정값 : Block 클래스, value: Block values(blockchain 변수에는 Block 클래스만 들어갈 수 있다.)
// 예시
// [
//     Block {
//       index: 0,
//       hash: 'asdjfiasdf', 
//       previousHash: '',   
//       data: 'flasidf',    
//       timestamp: 123231312
//     }
// ]
let blockchain = [FirstBlock];
// 블록체인값
const getBlockchain = () => blockchain;
// 체인의 맨 마지막 블록 객체 
const getLastesBlock = () => blockchain[blockchain.length - 1];
const getNewTimeStamp = () => Math.round(new Date().getTime() / 1000);
// 블록생성 함수!
const createNewBlock = (data) => {
    // 이전 블록 객체!
    const previousBlock = getLastesBlock();
    // 새로운 인덱스
    const newIndex = previousBlock.index + 1;
    // 새로운 타임
    const newTimeStamp = getNewTimeStamp();
    // 새로운 Hash값
    const newHash = Block.calculateBlockHash(newIndex, previousBlock.hash, newTimeStamp, data);
    const newBlock = new Block(newIndex, newHash, previousBlock.hash, data, newTimeStamp);
    addBlocktoChain(newBlock);
    return newBlock;
};
// 들어온 Block의 Hash값을 Return
const getBlockHash = (whatIsThisBlockHash) => 
/**
 * params : Hash값을 얻고자하는 Block
 */
Block.calculateBlockHash(whatIsThisBlockHash.index, whatIsThisBlockHash.previousHash, whatIsThisBlockHash.timestamp, whatIsThisBlockHash.data);
// 블록 검증(구조)
const isBlockValid = (currentBlock, previousBlock) => {
    /**
     * params : 현재 블록 객체, 이전 블록 객체
     * return : Boolean
     */
    if (!Block.valiableStrcture(currentBlock)) {
        return true;
    }
    else if (previousBlock.index + 1 !== currentBlock.index) {
        // 이전 블록과 현재 블록의 인덱스가 1개 차이가 아니면 False
        return false;
    }
    else if (previousBlock.hash !== currentBlock.previousHash) {
        // 이전 블록의 해쉬값과 현재 블록의 '이전해쉬값' 변수의 값이 다르면 False 
        return false;
    }
    else if (getBlockHash(currentBlock) !== currentBlock.hash) {
        // 현재 들어온 블록의 해쉬값이 서로 다르면 False
        return false;
    }
    else {
        return true;
    }
};
const addBlocktoChain = (currentBlock) => {
    if (isBlockValid(currentBlock, getLastesBlock())) {
        blockchain.push(currentBlock);
    }
};
createNewBlock("1");
createNewBlock("2");
createNewBlock("3");
createNewBlock("4");
console.log(blockchain);
//# sourceMappingURL=index.js.map