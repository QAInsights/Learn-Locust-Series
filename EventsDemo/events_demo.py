from locust import HttpUser, task, constant, SequentialTaskSet
from locust import events

import logging


@events.spawning_complete.add_listener
def spawn_users(user_count, **kwargs):
    print("Spawned ... ", user_count, " users.")


@events.request_success.add_listener
def send_notification(**kwargs):
    print("Sending the success notification")


@events.request_failure.add_listener
def send_notification(**kwargs):
    print("Sending the failed notification")


@events.quitting.add_listener
def sla(environment, **kwargs):
    if environment.stats.total.fail_ratio > 0.01:
        logging.error("Test failed due to failure ratio > 0.01%")
        environment.process_exit_code = 1
        print(environment.process_exit_code)

    else:
        environment.process_exit_code = 0
        print(environment.process_exit_code)


class LoadTest(SequentialTaskSet):

    @task
    def home_page(self):
        self.client.get("/", name="T00_SuccessRequests")
        self.client.get("/failed", name="T01_FailRequests")


class TestScenario(HttpUser):
    wait_time = constant(1)
    tasks = [LoadTest]
