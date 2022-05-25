import UtilLib
from Common.Status import Status
from Common.ConstVar import *
import Lib.UtilLib
import configparser
import requests


class MainController:
    def __init__(self):
        """initalize Monitoring object."""
        self.config = configparser.ConfigParser()
        self.run_type = None
        self.base_url = None
        self.token = None

    def running(self, run_type=None):
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
        self._read_config(run_type)

        header = {
            # Token값 변수로 받기
            'Content-Type' : 'application/json',
            'Authorization': f'Token {self.token}'
        }

        params = {
            # 변수로 받기
            'account_alias' : '20220517030650032658',
        }

        # response = requests.get(self.base_url+'/accounts/amounts', params=params, headers=header)
        response = requests.get(self.base_url+'/accounts/33911840901/assets')
        if response.status_code is not 200:
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



    def _read_config(self, run_type) -> bool:
        """
        * config.ini 파일을 읽어서 변수에 할당 합니다.
        @returns
            On Succuess - true
                         @descriptions
                            - 프로젝트 최상위 경로에서 config.ini 파일을 읽어서 변수에 저장합니다
            On Failure - false
                        @descriptions
                            - config.ini이 없거나, config.ini 파일 내 해당 변수가 없을 시 에러 발생
        """
        try:
            self.config.read(CONFIG_PATH, encoding='utf-8')
            self.base_url = self.config['URL_CONF'][run_type]
            self.token = self.config['Header']['token']

        except IOError:
            return Status.FAIL

        return Status.SUCCESS

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
