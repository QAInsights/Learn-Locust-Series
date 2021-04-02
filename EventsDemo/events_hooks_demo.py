from locust import HttpUser, task, constant
from locust.event import EventHook

send_email_notifications = EventHook()
send_text_notifications = EventHook()


def email(i, j, req_id, message=None, **kwargs):
    print("Sending", message, "in Email for the request", req_id)


send_email_notifications.add_listener(email)


def sms_text(i, j, req_id, message=None, **kwargs):
    print("Sending", message, "in SMS for the request", req_id)


send_text_notifications.add_listener(sms_text)


class LoadTest(HttpUser):
    wait_time = constant(1)

    @task
    def home_page(self):
        with self.client.get("/", name="T00_HomePage", catch_response=True) as response:
            if response.status_code == 200:
                send_email_notifications.fire(i=1, j=2, req_id=1, message="success")
                send_text_notifications.fire(i=1, j=2, req_id=2, message="success")
            else:
                send_email_notifications.fire(i=1, j=2, req_id=1, message="failed")
                send_text_notifications.fire(i=1, j=2, req_id=2, message="failed")

        with self.client.get("/test", name="T10_FailedHomePage", catch_response=True) as response:
            if response.status_code == 200:
                send_email_notifications.fire(i=1, j=2, req_id=3, message="success")
                send_text_notifications.fire(i=1, j=2, req_id=4, message="success")
            else:
                send_email_notifications.fire(i=1, j=2, req_id=3, message="failed")
                send_text_notifications.fire(i=1, j=2, req_id=4, message="failed")
