# BlockChain 
* 타입스크립트란?
=> 기존의 자바스크립트는 너무 유연하기 때문에 버그를 잡아내기 어려움. 이러한 문제를 해결하기 위해서, 좀더 엄격한 문법구조가 필요했음. 그래서 나온게 타입스크립트.

타입스크립트 설치
1. npm install -g typescript
(tsconfig파일 설정해준후, tsc로 구동하면 ts -> js로 변환된다.)
*   "scripts": {
    "start": "node index.js",
    "prestart": "tsc"
  } tsconfig에 설정을 넣어주면 node 명령어 npm으로도 구동이 된다. 다만 node가 읽을수 있는 구문이 아니면, ERROR가 난다. ex) alert

*   "scripts": {
    // 해당방식으로 node에서 tsc-watch가 성공하면, index.js를 콜하는 설정추가,
    "start": "./node_modules/.bin/tsc-watch --onSuccess \"node dist/index.js\""
  } tsc-watch 연동 방식

2. npm install tsc-watch --save-dev
* watch 모드로 돌리게 되면 변동이 생길때마다 자동으로 변화시켜줌




