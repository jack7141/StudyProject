import argparse
import os
import sys
import argparse
# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------
# 모듈 사용을 위하여 상위 폴더의 경로를 sys.path 에 추가 함
# 라이브러리 폴더가 추가 될시 이부분도 추가 해야함
BASE_DIR = os.path.dirname(os.path.abspath(os.getcwd()))
SRC_DIR_NAME_Common = "Common"
SRC_DIR_NAME_Lib = "Lib"
SRC_DIR_NAME_Main = "Main"

Common = os.path.join(BASE_DIR, SRC_DIR_NAME_Common)
Lib = os.path.join(BASE_DIR, SRC_DIR_NAME_Lib)
Main = os.path.join(BASE_DIR, SRC_DIR_NAME_Main)

AppPathList = [BASE_DIR, Common, Lib, Main]

add_path = [sys.path.append(p) for p in AppPathList]


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

from Lib import UtilLib
from Common import (ConstVar, )
from Main.MainController import MainController as mc


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def arguments_entryPoint():
    # [Command Parameter 설정]
    # arguments 설정
    modeList = [ConstVar.run_type_local, ConstVar.run_type_dev, ConstVar.run_type_opr, ConstVar.run_type_kb]
    title = 'Account'

    parser = argparse.ArgumentParser(prog="FOUNT API Monitor",
                                     description=f"* [Fount API 모니터링] {title}")

    # Argument(parameter) optional 인자로 설정
    # 실행 모드 설정
    parser.add_argument("-s",
                        "--settings",
                        type=str,
                        help="'{local}' (로컬 URL 모드) | '{dev}' (개발계 URL 모드) | '{opr}' (운영계 URL 모드) | '{kb}' (운영계 URL 모드)".format(
                            local = ConstVar.run_type_local,
                            dev = ConstVar.run_type_dev,
                            opr = ConstVar.run_type_opr,
                            kb = ConstVar.run_type_kb
                        ),
                        required=True,
                        choices=modeList,
                        metavar='',
                        dest="mode")

    mode = UtilLib.removeSideBlank(parser.parse_args().mode)

    return mode

if __name__ == "__main__":
    # [FOUNT Monitor Entry Point]
    print("#"*50)
    print("#{:>49}".format("#"))
    print("#\t  Start FOUNT API Monitor{:>17}".format("#"))
    print("#{:>49}".format("#"))
    print("#" * 50)
    # ------------------------------------------------------------------------------------------------------------------

    # params, Token을 여기서 받고싶은데..
    mode = arguments_entryPoint()
    mc_object = mc()
    if mode == ConstVar.run_type_local:
        mc_object.running(run_type=ConstVar.run_type_local)

    elif mode == ConstVar.run_type_dev:
        mc_object.running(run_type=ConstVar.run_type_dev)

    elif mode == ConstVar.run_type_opr:
        mc_object.running(run_type=ConstVar.run_type_opr)

    else:
        mc_object.running(run_type=ConstVar.run_type_kb)

    # ------------------------------------------------------------------------------------------------------------------
    print("#" * 50)
    print("#{:>49}".format("#"))
    print("#\t  End FOUNT API Monitor{:>19}".format("#"))
    print("#{:>49}".format("#"))
    print("#" * 50)