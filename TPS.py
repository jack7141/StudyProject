# import os
# import time
# from multiprocessing import Process, Pool
# import requests as req
#
# import requests
# from concurrent.futures import ThreadPoolExecutor, as_completed
# from time import time
#
# localhost = "http://0.0.0.0/"
# endpoint = "api/v1/hanaw/accounts/global/fractional/order"
# cancel_enpoint = "api/v1/hanaw/accounts/global/fractional/order/cancel"
# test = []
# test2 = []
#
# url_list = [
#     "https://www.google.com/api/",
#     "https://www.google.com/api/",
#     "https://www.google.com/api/",
#     "https://www.google.com/api/",
#     "https://www.google.com/api/",
#     "https://www.google.com/api/",
#     "https://www.google.com/api/",
#     "https://www.google.com/api/",
#     "https://www.google.com/api/",
# ]
#
# def download_file(xxxx):
#
#     payload = {
#       "account_alias": "A08202414",
#       "account_type": "010",
#       "password": "3651",
#       "code": "MSFT",
#       "amount": "1000"
#     }
#
#     resp = req.post(url=f'{localhost}{endpoint}', json=payload)
#     print(resp.json())
#     if resp.json()['order_no']:
#         cancel_payload = {
#               "account_alias": "A08202414",
#               "account_type": "010",
#               "password": "3651",
#               "order_no": resp.json()['order_no']
#         }
#         cancel = req.post(url=f'{localhost}{cancel_enpoint}', json=cancel_payload)
#
#         # 취소 접수 endpoint로 처리
#         # 모든 과정 끝나면, list 담기
#         print(cancel.json())
#         test2.append(resp.json())
#     return resp.json()
#
# """
# 1분, 프로세스 100개, 요청 갯수, 응답갯수 확인
#
# 계좌 2700, 종목 5, 2700 x 5 ==> 13500
# * 10초 -> 보내고, 응답, 요청값 갯수 확인 => 갯수 / 10 => 1초당 100개
#
# 주문처리로 요청이 되야하는 이유
# - 주문 접수로 확인
# - 운영계
# """
# if __name__ == "__main__":
#     start = time()
#
#     processes = []
#     with ThreadPoolExecutor(max_workers=25) as executor:
#         for url in url_list:
#             processes.append(executor.submit(download_file, url))
#
#     for task in as_completed(processes):
#         print(task.result())
#
#     print(f'Time taken: {time() - start}')
#
#
#
#
#
import os
import threading
import time
from threading import Thread
import requests


localhost = "http://0.0.0.0/"
endpoint = "api/v1/hanaw/accounts/global/fractional/order"
cancel_enpoint = "api/v1/hanaw/accounts/global/fractional/order/cancel"
test = []
test2 = []

def callback():
    for i in ['A56543189', 'A73320062']:
        for _ in range(20):
            try:
                payload = {
                  "account_alias": i,
                  "account_type": "010",
                  "code": "MSFT",
                  "amount": "1000"
                }
                r = requests.post(url=f'{localhost}{endpoint}', json=payload)
                # time.sleep(1)
                if r.ok:
                    if r.json().get('order_no', None):
                        cancel_payload = {
                              "account_alias": i,
                              "account_type": "010",
                              "order_no": r.json()['order_no']
                        }
                    cancel = requests.post(url=f'{localhost}{cancel_enpoint}', json=cancel_payload)
                    print(f"Account: {payload['account_alias']}, REQUSET : {r.json()}, RESPONSE: {cancel.json()}")
                else:
                    print("ERRORORRROROROROR!")
            except KeyboardInterrupt:
                return

THREAD_COUNT = 20
if __name__ == '__main__':
    threads = []
    for i in range(THREAD_COUNT):
        t = Thread(target=callback)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()