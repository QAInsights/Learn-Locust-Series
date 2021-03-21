from locust import User, task, constant


class MyFirstTest(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print("Launching the URL")

    @task
    def search(self):
        print("Searching")


class MySecondTest(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch2(self):
        print("Second Test")

    @task
    def search2(self):
        print("Second Search Test")
