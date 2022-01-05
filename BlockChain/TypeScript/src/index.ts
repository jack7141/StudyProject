// Hash import
import * as CryptoJS from 'crypto-js';

class Block{
    
    // return값 string으로 명시!
    // 값을 해쉬값으로 변환
    static calculateBlockHash = (
        index:number, 
        previousHash:string, 
        timestamp:number, 
        data:string
        ): string => 
        CryptoJS.SHA256(index + previousHash + timestamp + data).toString();
        
    // 블록 조건 충족여부 체크
    static valiableStrcture = (thisBlock: Block): boolean => 
        typeof thisBlock.index === "number" &&
        typeof thisBlock.hash === "string" &&
        typeof thisBlock.previousHash === "string" &&
        typeof thisBlock.timestamp === "number" &&
        typeof thisBlock.data === "string";

    // 변수지정
    public index: number;
    public hash: string;
    public previousHash: string;
    public data: string;
    public timestamp: number;
        
    // 생성자 
    constructor(
        // 인자
        index: number,
        hash: string,
        previousHash: string,
        data: string,
        timestamp: number
    ){
        this.index = index;
        this.hash = hash;
        this.previousHash = previousHash;
        this.data = data;
        this.timestamp = timestamp;
    }
}

// FirstBlock은 Block속성만 받을 수 있게 명시!
const FirstBlock:Block =  new Block(0, "2020202020202", "", "Hello", 123456);
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

let blockchain: Block[] = [FirstBlock];

// 블록체인값
const getBlockchain = (): Block[] => blockchain;

// 체인의 맨 마지막 블록 객체 
const getLastesBlock = (): Block => blockchain[blockchain.length - 1];
const getNewTimeStamp = (): number => Math.round(new Date().getTime() / 1000);

// 블록생성 함수!
const createNewBlock = (data: string): Block => {
    // 이전 블록 객체!
    const previousBlock: Block = getLastesBlock();

    // 새로운 인덱스
    const newIndex: number = previousBlock.index + 1;

    // 새로운 타임
    const newTimeStamp: number = getNewTimeStamp();

    // 새로운 Hash값
    const newHash: string = Block.calculateBlockHash(
        newIndex,
        previousBlock.hash,
        newTimeStamp,
        data
    );

    const newBlock: Block = new Block(
        newIndex,
        newHash,
        previousBlock.hash,
        data,
        newTimeStamp
    );
    addBlocktoChain(newBlock);
    return newBlock
}

// 들어온 Block의 Hash값을 Return
const getBlockHash = (whatIsThisBlockHash: Block): string =>
    /**
     * params : Hash값을 얻고자하는 Block
     */
    Block.calculateBlockHash(
        whatIsThisBlockHash.index,
        whatIsThisBlockHash.previousHash,
        whatIsThisBlockHash.timestamp,
        whatIsThisBlockHash.data
    );

// 블록 검증(구조)
const isBlockValid = (currentBlock: Block, previousBlock: Block): boolean => {
    /**
     * params : 현재 블록 객체, 이전 블록 객체
     * return : Boolean
     */
    if(!Block.valiableStrcture(currentBlock)){
        return true;
    } else if(previousBlock.index + 1 !== currentBlock.index) {
        // 이전 블록과 현재 블록의 인덱스가 1개 차이가 아니면 False
        return false;
    } else if(previousBlock.hash !== currentBlock.previousHash) {
        // 이전 블록의 해쉬값과 현재 블록의 '이전해쉬값' 변수의 값이 다르면 False 
        return false;
    } else if(getBlockHash(currentBlock) !== currentBlock.hash) {
        // 현재 들어온 블록의 해쉬값이 서로 다르면 False
        return false;
    } else {
        return true
    }
};

const addBlocktoChain = (currentBlock: Block): void => {
    if(isBlockValid(currentBlock, getLastesBlock())){
        blockchain.push(currentBlock);
    }
}
createNewBlock("1");
createNewBlock("2");
createNewBlock("3");
createNewBlock("4");


console.log(blockchain);

export {};