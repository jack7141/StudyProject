import { useState, useEffect } from "react";

// CleanUp을 통해서 True, False로 H1 태그를 만들고 없앤다.
// 다만 생성됬을때 말고도 삭제됬을때도 return을 받으려고 아래와 같이 처리한다.
function Hello() {
  useEffect(function () {
    console.log("hi :)");
    return function () {
      console.log("bye :(");
    };
  }, []);
  useEffect(() => {
    console.log("hi :)");
    return () => console.log("bye :(");
  }, []);
  return <h1>Hello</h1>;
}

function CleanUp() {
  const [showing, setShowing] = useState(false);
  const onClick = () => setShowing((prev) => !prev);
  return (
    <div>
      {showing ? <Hello /> : null}
      <button onClick={onClick}>{showing ? "Hide" : "Show"}</button>
    </div>
  );
}

export default CleanUp;