from locust import User, task, constant, between, constant_pacing, SequentialTaskSet
import time


class ConstantPacing(User):
    wait_time = constant_pacing(3)

    @task
    def launch(self):
        time.sleep(2)
        print("Constant Pacing Demo")


class Constant(User):
    wait_time = constant(3)

    @task
    def launch(self):
        print("Constant Demo")


class Between(User):
    wait_time = between(3, 5)

    @task
    def launch(self):
        print("Between Demo")
