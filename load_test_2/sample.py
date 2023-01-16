from locust import HttpUser, task, between, TaskSet
# https://wookkl.tistory.com/67
# https://velog.io/@ehddnr/locust%EB%A1%9C-%EB%B6%80%ED%95%98%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%95%98%EA%B8%B0
class AccountBehavior(TaskSet):
    @task
    def get_account_number_detail(self):
        account_number = 123445152
        self.client.get(f'/asset/{account_number}')

    @task
    def home(self):
        self.client.get('/')

    def on_start(self):
        print("START LOCUST")

    def on_stop(self):
        print("STOP LOCUST")


class LocustUser(HttpUser):
    host = "https://locust.load-test.com"
    tasks = [AccountBehavior]
    wait_time = between(1, 4)