// Button 클래스에서 export 가져옴
import Button from "./Button";
import styles from "./App.module.css";
import { useEffect, useState } from "react";

function App() {

  const [counter, setValue] = useState(0);
  const [keyword, setKeyword] = useState("");
  const ClickFunction = () => setValue((prev) => prev + 1);

  const onChange = (event) => setKeyword(event.target.value);

  console.log('run all time');

  const RunOnlyOnce = () => {
    console.log('i run only once');
  }
  // useEffect를 사용하면 처음에 Render할때만 작동된다.
  // useEffect(RunOnlyOnce, []);
  useEffect(() => {
      console.log('익명의 함수로 생성');
  }, []);

  useEffect(() => {
    console.log('[]의 의미!');
    // [] 안에 state를 넣어주면 내가 넣은 값의 변동에 따라서 useEffect가 다시 동작한다.
    // 그래서 빈 값으로 넣어주면 실행과 동시에 한번만 실행되는 이유!
    // 보통 검색할때 많이 쓰는듯
}, [keyword]);
  return (
    <div>
      <input onChange={onChange} value={keyword}></input>
      <h1 className={styles.title}>Hello</h1>
      <button onClick={ClickFunction}>click</button>
    </div>
  );
}

export default App;
