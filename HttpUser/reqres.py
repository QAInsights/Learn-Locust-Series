from locust import HttpUser, constant, task


class MyReqRes(HttpUser):

    wait_time = constant(1)
    host = "http://example.com"

    @task
    def get_users(self):
        res = self.client.get("/")
        print(res.status_code)
