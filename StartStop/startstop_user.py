from locust import User, task, constant


class MyTest(User):
    wait_time = constant(1)

    def on_start(self):
        print("Starting")

    @task
    def task_1(self):
        print("My tasks")

    def on_stop(self):
        print("Stopping")
