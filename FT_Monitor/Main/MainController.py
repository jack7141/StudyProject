import UtilLib
from Common.Status import Status
from Common.ConstVar import *
from IO.IO import IO
import Lib.UtilLib
import configparser
import requests


class MainController:
    def __init__(self, run_type=None, base_api=None):
        """initalize Monitoring object."""
        self.config = configparser.ConfigParser()
        self.run_type = run_type
        self.base_api = base_api

    def running(self):
        """ Monitoring Process 시작 """
        # KB_TR인 경우 토큰 필요 없고 바로 GET요청을 통해서 데이터 읽어올 수 있음

        """
        BASE_URL - stage-kb-tr.fount.co/api/v1/kb 
            - /accounts/{계좌번호}/assets - 자산평가
            - /accounts/{계좌번호}/balances - balances
            - /accounts/{계좌번호}/execution - 해외 체결내역 조회
            - /accounts/{계좌번호}/trades - 해외 거래내역
        """
        # config 파일 read
        io = IO(run_type=self.run_type, base_api=self.base_api)
        BASE_URL = io.read_config.get('base_url')
        API_URL = io.read_config.get('base_api')
        # run_type으로 클래스 분기

        # header = {
        #     # Token값 변수로 받기
        #     'Content-Type' : 'application/json',
        #     'Authorization': f'Token {self.token}'
        # }
        #
        # params = {
        #     # 변수로 받기
        #     'account_alias' : '20220517030650032658',
        # }

        # response = requests.get(self.base_url+'/accounts/amounts', params=params, headers=header)
        response = requests.get(BASE_URL+API_URL+'/33911840901/assets')
        if response.status_code != 200:
            print("#{:>49}".format("#"))
            print(f'#\t   {response.status_code} response 응답 에러'"{:>17}".format("#"))
            print("#{:>49}".format("#"))
            return False

        #
        #
        """
        json 저장
        현재폴더 기준
            오늘날짜 ---
                    |- API 호출 요청한 시간 --- 
                    |                    |- trades, execution, balance, assets json 데이터 생성
                    |
                    |- API 호출 요청한 시간 ---
                                         |- trades, execution, balance, assets json 데이터 생성
        """
        print(UtilLib.get_json_pretty(response))





    def _config_generator(self):

        self.config["Header"] = {}
        # config 파일에서 Token 있으면 pass
        # 없으면, 생성하고 저장
        # 유저 토큰은 발급받아야함
        # self.config["Header"]["Token"] =

        with open(CONFIG_PATH, 'w+', encoding='utf-8') as configfile:
            self.config.write(configfile)

    def _save_response(self):
        """
        * API response를 받은 데이터를 LOCAL에 json 파일로 저장합니다
        @params
        @return
            - On Success : true
                        @descriptions
                            - 지정한 경로에 response 데이터를 json 파일로 저장합니다.
            - On Failure : false
                        @descriptions
                            - 지정한 경로에 response 데이터를 json 저장할 수 없습니다.

        """
        pass
