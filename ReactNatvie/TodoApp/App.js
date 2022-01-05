import { StatusBar } from 'expo-status-bar';
import { useEffect, useState } from 'react';
import { theme } from "./color";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { Fontisto } from "@expo/vector-icons";
import tw from 'tailwind-react-native-classnames';
import {
  StyleSheet,
  Text,
  View,
  // 눌렀을때 투명도로 눌린거를 확인하게해줌
  TouchableOpacity,
  TouchableHighlight,
  // 눌러도 아무런 반응 없음
  TouchableWithoutFeedback,
  // 버튼 주변을 클릭해도 클릭이 가능하게끔
  Pressable,
  // Textinput 태그
  TextInput,
  ScrollView,
  Alert,
  // 현재 무슨 Platform인지 확인
  Platform,
} from "react-native";


const STORAGE_KEY = "@toDos";

export default function App() {

  const [working, setWorking] = useState(true);
  const [text, setText] = useState("");
  const [toDos, setToDos] = useState({});
  
  // 함수 콜해서 return을 받는 변수
  const travel = () => setWorking(false);

  // 함수 콜해서 return을 받는 변수
  const work = () => setWorking(true);
  const onChangeText = (inputText) => setText(inputText);

  useEffect(() => {
    loadToDos();
  }, []);


  // 스토리지를 저장할때는 String으로만 가능하고, Object를 저장하려해도 String으로 수정해서 처리해야함
  const saveToDos = async (toSave) => {
    // object to String
    const ObjectToString = JSON.stringify(toSave)
    // 스토리지에 save
    await AsyncStorage.setItem(STORAGE_KEY, ObjectToString);
  };

  const loadToDos = async () => {
    const getCovertedString = await AsyncStorage.getItem(STORAGE_KEY);
    // StiringToObject
    console.log(getCovertedString)
    // 스토리지에 null값이 있다면 parse가 불가능하기 때문에
    if (getCovertedString) {
      setToDos(JSON.parse(getCovertedString));
    }
  };

  const addToDo = async () => {
    if (text === "") {
      return;
    }
    const newToDos = {
      // 기존의 TODO의 object내용을 모두 가지고온다
      ...toDos,
      // 숫자id : object{내용: wortking값 (기본값 True)} 를 다시 저장
      [Date.now()]: { text, working },
    };
    console.log(newToDos)
    // setToDos에 저장
    // 예시
    // Object {
    //   "1639885042607": Object {
    //     "text": "어누유",
    //     "work": true,
    //   },
    //   "1639885126770": Object {
    //     "text": "ㅍㅊ 유유류류류류류",
    //     "work": true,
    //   },
    // }

    setToDos(newToDos);
    // object를 saveToDos로 Send
    await saveToDos(newToDos);
    setText("");
  };

  const deleteToDo = async (key) => {
    // 기존의 데이터를 모두 들고온 후 데이터들 중에서 key값에 맞는 값만 삭제하고 다시 setToDos에 담아주고 save
    const newToDos = {...toDos};
    if(Platform.OS === "web"){
        const ok = confirm(`${newToDos[key].text}삭제하시겠습니까?`)
        if (ok) {
          delete newToDos[key]
          setToDos(newToDos);
          saveToDos(newToDos);
        }
    } else {
      Alert.alert(
        `${newToDos[key].text}`, "삭제하시겠습니까?", [
        { text: "취소"}, 
        { text: "확인" , 
        // 기다리는게 싫다면, async와 await을 지워도 상관없음
          onPress: () => {
            delete newToDos[key]
            setToDos(newToDos);
            saveToDos(newToDos);
        }},
      ]);
    }
    return;
  };


  return (
    <View style={styles.container}>
      <StatusBar style="auto" />
      {/* header */}
      <View style={styles.header}>
        <TouchableOpacity onPress={work}>
          <Text style={{...styles.btnText, color: working ? "white": theme.grey}}>Work</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={travel}>
          <Text style={{...styles.btnText, color: !working ? "white": theme.grey}}>Travel</Text>
        </TouchableOpacity>
      </View>
        <TextInput        

        // 타자를 입력할 시 입력창을 바꿔줌
        // keyboardType='email-address'

        // 타자에서 enter key의 라벨이름을 바꿔줌
        // returnKeyType='search'

        onChangeText={onChangeText}

        // 함수콜!
        onSubmitEditing={addToDo}
        value={text}
        placeholder={working ? "Add a To Do" : "Where do you want to go?"}
        style={styles.input}>
        </TextInput>

      <ScrollView>
        {Object.keys(toDos).map((key) =>
        // work항목과 Travel항목을 True, False로 구별
          toDos[key].working === working ? (
            <View style={styles.toDo} key={key}>
              <Text style={styles.toDoText}>{toDos[key].text}</Text>
              <TouchableOpacity onPress={() => deleteToDo(key)}>
              <Fontisto name="trash" size={18} color={theme.grey} />
              </TouchableOpacity>
            </View>
          ) : null
        )}
      </ScrollView>

      
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: theme.bg,
    paddingHorizontal: 20,
  },
  header: {
    justifyContent: "space-between",
    flexDirection: "row",
    marginTop: 100,
  },
  btnText: {
    fontSize: 38,
    fontWeight: "600",
  },
  input: {
    backgroundColor: "white",
    paddingVertical: 15,
    paddingHorizontal: 20,
    borderRadius: 30,
    marginVertical: 20,
    fontSize: 18,
  },
  toDo: {
    backgroundColor: theme.toDoBg,
    marginBottom: 10,
    paddingVertical: 20,
    paddingHorizontal: 20,
    borderRadius: 15,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
  },
  toDoText: {
    color: "white",
    fontSize: 16,
    fontWeight: "600",
  },
});