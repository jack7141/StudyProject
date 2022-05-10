import json
import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent.parent

secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    """ secrets.json의 key, value를 통해 기본 세팅을 진행합니다.

    @params
        setting - secrets.json의 키 값
        secrets - BASE_URL을 통해서 secrets.json 파일을 읽어옵니다

    @returns
        On succuess - Django Secret key, Database, etc.. 설정 완료
        On failure - json 파일에 key를 확인하고 key가 없으면 KeyError를 출력합니다.
                     message: "Set the {0} enviroment variable".format(setting)
    """
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} enviroment variable".format(setting)
        raise ImproperlyConfigured(error_msg)