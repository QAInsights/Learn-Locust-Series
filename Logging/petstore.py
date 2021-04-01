from locust import HttpUser, SequentialTaskSet, task, constant
import logging


class PetStore(SequentialTaskSet):

    @task
    def home_page(self):
        with self.client.get("/", catch_response=True, name="T00_HomePage") as response:
            if "Welcome to JPetStore 6" in response.text and response.elapsed.total_seconds() < 2.0:
                response.success()
                logging.info("Home Page load success")
            else:
                response.failure("Home page took too long to load and/or text check has failed.")
                logging.error("Home page didn't load successfully.")


class LoadTest(HttpUser):
    host = "https://petstore.octoperf.com"
    wait_time = constant(1)
    tasks = [PetStore]
