# https://velog.io/@ehddnr/locust%EB%A1%9C-%EB%B6%80%ED%95%98%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%95%98%EA%B8%B0
# 서비스 TPS 측정 툴

from locust import HttpUser, task

order_num = []

class Order(HttpUser):
    @task
    def make_order(self):
        r = self.client.post("/api/v1/order",
                             json={
                                    "account_alias": "AAA123",
                                    "account_type": "010",
                                    "code": "MSFT",
                                    "amount": "1000"
                             })
        if r.ok:
            if r.json().get('order_no', None):
                print("================================================================")
                print(f"order_no: {r.json()['order_no']}")
                order_num.append(r.json()['order_no'])

    def on_stop(self):
        for i in order_num:
            print("================================================================")
            print(f"ON STOP --> order_no: {i}")
            self.client.post("/api/v1/order/cancel",
                             json={
                                 "account_alias": "AAA123",
                                 "account_type": "010",
                                 "order_no": i
                             })