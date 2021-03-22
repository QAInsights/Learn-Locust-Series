from locust import TaskSet, constant, task, HttpUser
import random


class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get Status of 200")


class MyAnotherHTTPCat(TaskSet):

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Get Status of 500")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPCat, MyAnotherHTTPCat]
    wait_time = constant(1)
