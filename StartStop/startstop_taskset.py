from locust import HttpUser, task, constant, TaskSet


class MyTest(TaskSet):

    def on_start(self):
        self.client.get("/", name=self.on_start.__name__)
        print("Start")

    @task
    def browse_product_1(self):
        self.client.get("/product/OLJCESPC7Z", name=self.browse_product_1.__name__)
        print("Browse Product 1")

    @task
    def browse_product_2(self):
        self.client.get("/product/9SIQT8TOJO", name=self.browse_product_2.__name__)
        print("Browse Product 2")

    @task
    def cart_page(self):
        self.client.get("/cart", name=self.cart_page.__name__)
        print("Cart Page")

    def on_stop(self):
        self.client.get("/", name=self.on_stop.__name__)
        print("Stop")


class LoadTest(HttpUser):
    host = "https://onlineboutique.dev"
    tasks = [MyTest]
    wait_time = constant(1)