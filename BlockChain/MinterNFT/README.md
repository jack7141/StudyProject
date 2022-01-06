# 📝 NFT Minter Tutorial Files
* 튜토리얼 - https://docs.alchemy.com/alchemy/tutorials/nft-minter
* 이더리움 tracking? 사이트! 내 지갑 주소치면 활동정보 알수있음.

    1. npm install[command 입력]로 패키지를 모두 설치해준다.

    2. npm start[command 입력]로 서버 Start! 

    3. npm install dotenv => 공통변수 설정을 위해서 설치
    [https://hello-bryan.tistory.com/134]

    4. npm install @alch/alchemy-web3 => alchemy web3을 사용하기 위해서 설치

    5. 정적 사이트 배포 => netlify로 처리

    6. npm run build 로 배포 준비

## ℹ️ 튜토리얼



## 🤔 노트
    [준비물]
* Mint https://www.alchemy.com/ 사이트에 가입해서 계정을 생성해준다.
* MetaMask 지갑과 https://faucet.egorfine.com/ 테스트용 이더리움 거래를 통해서 거래 상태를 확인한다.(사이트에 지갑 주소를 넣어주고 가짜 이더발행! 후 alchemy 사이트, composer에서 네트워크 Ropsten으로 설정, 메소드 eth_getBalance로 설정해주고 주소 적는란에 Faucet에서 발행된 주소로 요청을 보낸다. )

* IPFS : IPFS(아이피에프에스)는 "InterPlanetary File System"의 약자로서, 분산형 파일 시스템에 데이터를 저장하고 인터넷으로 공유하기 위한 프로토콜이다.

* Pinata : NFT 데이터 저장 관리 툴 (Pinata외 Ethernum도 있음 차이는 아직 모르겠음) => 가입해준다.


## 🤔 에러 노트

* Error: Alchemy URL protocol must be one of http, https, ws, or wss. Recieved: undefined React.js
[https://stackoverflow.com/questions/70141376/%C3%97-error-alchemy-url-protocol-must-be-one-of-http-https-ws-or-wss-recieved]

요소들 다 삭제했다가 다시 설치해줬더니 성공함.

    
    npm uninstall react-scripts or yarn remove react-scripts
    and re-install using
    yarn add react-scripts or npm add react-scripts.