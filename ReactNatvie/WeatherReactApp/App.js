import { StatusBar } from 'expo-status-bar';
import React, { useEffect, useState } from "react";
import { StyleSheet, Text, View, ScrollView, Dimensions, ActivityIndicator } from 'react-native';

// expo loaction 라이브러리 설치후 import
import * as Location from "expo-location";

// 아이콘 라이브러리
import { Fontisto } from "@expo/vector-icons";

// 화면의 사이즈를 가지고온다.
const { width: SCREEN_WIDTH } = Dimensions.get("window");

// 날씨 APIKEY 선언
const APIKEY = 'f6551d5a2a90c7cd7fd282637b708ff8';

const icons = {
  Clouds: "cloudy",
  Clear: "day-sunny",
  Atmosphere: "cloudy-gusts",
  Snow: "snow",
  Rain: "rains",
  Drizzle: "rain",
  Thunderstorm: "lightning",
}


export default function App() {
  // 변수 선언 
  const [city, setCity] = useState("Loading...");
  const [ok, setOk] = useState(true);
  const [days, setDays] = useState([]);


  const getWeather = async () => {

    // 모바일 기계상 True, False 위치 요청 
    const { granted } = await Location.requestForegroundPermissionsAsync();

    // 위치 허용 False
    if (!granted) {
      setOk(false);
    }

    const {coords: { latitude, longitude },} = await Location.getCurrentPositionAsync({ accuracy: 5 });// 정확도 5로 설정!

    // 현재 위치를 받아오는 함수를 통해서 가져온 위도, 경도를 reverseFeocode함술르 통해서 도시명을 가져온다.
    const location = await Location.reverseGeocodeAsync({ latitude, longitude },{ useGoogleMaps: false });
    // location info
    // Array [
    //   Object {
    //     "city": "고양시",
    //     "country": "대한민국",
    //     "district": "가좌동",
    //     "isoCountryCode": "KR",
    //     "name": "가좌동 1086",
    //     "postalCode": "10211",
    //     "region": "경기도",
    //     "street": "가좌동",
    //     "subregion": null,
    //     "timezone": "Asia/Seoul",
    //   },
    // ]
    
    console.log(latitude, longitude, APIKEY)

    setCity(location[0].city);

    // API 호출
    const response = await fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${latitude}&lon=${longitude}&exclude=alerts&appid=${APIKEY}&units=metric`);
    const json = await response.json()
    setDays(json.daily);
  };
  
  useEffect(() => {
    // component가 마운트 되면 아래 function 호출
    getWeather();
  }, []);

  return (
    <View style={styles.container}>
      <View style={styles.city}>
        <Text style={styles.cityName}>{city}</Text>
      </View>
      {/* ReactNative상에서는 Scroll이 자동이 아니기 때문에 ScrollView 컴포넌트를 사용해서 스크롤 기능을 넣어준다. */}
      <ScrollView
        // 페이지가 넘어갈때 완전히 페이지가 넘어가야지 넘어가게 해줌
        pagingEnabled
        horizontal
        // 페이지가 넘어갈때 스크롤을 숨겨줌
        showsHorizontalScrollIndicator={false}
        contentContainerStyle={styles.weather}
      >
        {days.length === 0 ? (
          // days의 값이 0이면 로딩화면 표시!
          // 2가지 스타일 합치기
          <View style={{ ...styles.day, alignItems: "center" }}>
            <ActivityIndicator
              color="black"
              style={{ marginTop: 10 }}
              size="large"
            />
          </View>
        ) : (
          days.map((day, index) => (
            <View key={index} style={styles.day}>
            <View
              style={{
                flexDirection: "row",
                alignItems: "center",
                width: "100%",
                justifyContent: "space-between",
              }}
            >
              <Text style={styles.temp}>
                {parseFloat(day.temp.day).toFixed(1)}
              </Text>
              <Fontisto
              // day.weather.main => 날씨 정보(ex. 흐림, 맑음, Cloudy ... )
                name={icons[day.weather[0].main]}
                size={68}
                color="white"
              />
            </View>
              
              <Text style={styles.description}>{day.weather[0].main}</Text>
              <Text style={styles.tinyText}>{day.weather[0].description}</Text>
            </View>
          ))
        )}

      </ScrollView>
      <StatusBar style="true" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "tomato",
  },
  city: {
    flex: 1.2,
    justifyContent: "center",
    alignItems: "center",
  },
  cityName: {
    fontSize: 58,
    fontWeight: "500",
    color: "white",
  },
  weather: {},
  day: {
    width: SCREEN_WIDTH,
    alignItems: "flex-start",
    paddingHorizontal: 20,
  },
  temp: {
    marginTop: 50,
    fontWeight: "600",
    fontSize: 100,
    color: "white",
  },
  description: {
    marginTop: -10,
    fontSize: 30,
    color: "white",
    fontWeight: "500",
  },
  tinyText: {
    marginTop: -5,
    fontSize: 25,
    color: "white",
    fontWeight: "500",
  },
});