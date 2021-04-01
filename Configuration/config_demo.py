from locust import HttpUser, task, constant


class LoadTest(HttpUser):
    wait_time = constant(1)

    def __init__(self, parent):
        super().__init__(parent)
        self.hostname = self.host

    @task
    def home_page(self):
        res = self.client.get("/", name=self.hostname)
        print(res.text)

