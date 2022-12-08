import sys
import threading
import time

from collections import defaultdict
from locust import HttpUser, task, between

global is_done
is_done = False

class Order:
    def __init__(self, account_alias):
        self.account_alias = account_alias

    def make_order(self, client):
        print(f"REQUEST create order account_alias: {self.account_alias}")

        response = client.post(
            url="/api/v1/hanaw/accounts/global/fractional/order",
            json={
                "account_alias": self.account_alias[:-3],
                "account_type": self.account_alias[-3:],
                "code": "MSFT",
                "amount": "1000"
            }
        )

        if response.ok:
            order_no = response.json().get('order_no')            
            print(f"SUCCEEDED create order_no: {order_no}")
            return order_no
        else:
            print(f"FAILED create order, account_alias : {self.account_alias}, error: {response.text}")
            return None
                


class HanawOrderTest(HttpUser):
    lock = threading.Lock()
    results = defaultdict(list)
    # accounts = [
    #     'A25033952010',
    #     'A31309604010',
    #     'A98081538010',
    #     'A35740157010',
    #     'A57639682010',
    #     'A09834287010',
    #     'A03596514010',
    #     'A28721921010',
    #     'A20926582010',
    #     'A86640858010',
    # ]

    accounts = [
        'A56543189010',
        'A73320062010',
    ]

    @task(weight=1)
    def account_0(self):        
        account_alias = self.accounts[0]

        order = Order(account_alias=account_alias)
        order_no = order.make_order(client=self.client)

        if order_no:
            self.results[account_alias].append(order_no)
                
    @task(weight=1)
    def account_1(self):
        account_alias = self.accounts[1]

        order = Order(account_alias=account_alias)
        order_no = order.make_order(client=self.client)

        if order_no:
            self.results[account_alias].append(order_no)            
            

    # @task(weight=1)
    # def account_2(self):
    #     account_alias = self.accounts[2]

    #     order = Order(account_alias=account_alias)
    #     order_no = order.make_order(client=self.client)

    #     if order_no:
    #         self.results[account_alias].append(order_no)  

    # @task(weight=1)
    # def account_3(self):
    #     account_alias = self.accounts[3]

    #     order = Order(account_alias=account_alias)
    #     order_no = order.make_order(client=self.client)

    #     if order_no:
    #         self.results[account_alias].append(order_no)  

    # @task(weight=1)
    # def account_4(self):
    #     account_alias = self.accounts[4]

    #     order = Order(account_alias=account_alias)
    #     order_no = order.make_order(client=self.client)

    #     if order_no:
    #         self.results[account_alias].append(order_no)  

    # @task(weight=1)
    # def account_5(self):
    #     account_alias = self.accounts[5]

    #     order = Order(account_alias=account_alias)
    #     order_no = order.make_order(client=self.client)

    #     if order_no:
    #         self.results[account_alias].append(order_no)  

    # @task(weight=1)
    # def account_6(self):
    #     account_alias = self.accounts[6]

    #     order = Order(account_alias=account_alias)
    #     order_no = order.make_order(client=self.client)

    #     if order_no:
    #         self.results[account_alias].append(order_no)                                                              

    # @task(weight=1)
    # def account_7(self):
    #     account_alias = self.accounts[7]

    #     order = Order(account_alias=account_alias)
    #     order_no = order.make_order(client=self.client)

    #     if order_no:
    #         self.results[account_alias].append(order_no)  

    # @task(weight=1)
    # def account_8(self):
    #     account_alias = self.accounts[8]

    #     order = Order(account_alias=account_alias)
    #     order_no = order.make_order(client=self.client)

    #     if order_no:
    #         self.results[account_alias].append(order_no)  

    # @task(weight=1)
    # def account_9(self):
    #     account_alias = self.accounts[9]

    #     order = Order(account_alias=account_alias)
    #     order_no = order.make_order(client=self.client)

    #     if order_no:
    #         self.results[account_alias].append(order_no)     


    # 테스트 종료시 요청했던 주문을 모두 취소한다.
    def on_stop(self):
        global is_done

        self.lock.acquire()
        if is_done:
            return 

        for account_alias in self.results.keys():

            print(f'start to cancel order, account_alias : {account_alias}')

            for order_no in self.results.get(account_alias, []):
                print(f"REQUEST cancel order_no : {order_no}")

                response = self.client.post(
                    url="/api/v1/hanaw/accounts/global/fractional/order/cancel",
                    json={
                        "account_alias": account_alias[:-3],
                        "account_type": account_alias[-3:],
                        "order_no": order_no
                    }
                )

                if response.ok:
                    print(f"SUCCEEDED cancel order no : {order_no}")
                else:
                    print(f"FAILED cancel order_no : {order_no}, error: {response.text}")
                    return             

            is_done = True
                            
        self.lock.release()
