from Common import Status
from Common.ConstVar import *

import configparser

class IO:
    def __init__(self, run_type, base_api):
        """initalize Monitoring object."""
        self.config = configparser.ConfigParser()
        self.run_type = run_type
        self.base_api = base_api

    @property
    def read_config(self) -> dict:
        """
        * config.ini 파일을 읽어서 변수에 할당 합니다.

        @returns
            On Succuess - @return
                            -  dicti { base_url, }

                          @descriptions
                            - 프로젝트 최상위 경로에서 config.ini 파일을 읽어서 변수에 저장합니다

            On Failure - false
                        @descriptions
                            - config.ini이 없거나, config.ini 파일 내 해당 변수가 없을 시 에러 발생
        """
        try:
            self.config.read(CONFIG_PATH, encoding='utf-8')

            kwrags = {
                'base_url':self.config['URL_CONF'][self.run_type],
                'base_api':self.config['API_BASE'][self.base_api],
            }

        except IOError:
            return Status.FAIL

        return kwrags
