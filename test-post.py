# Author ashsepra@gmail.com
# This load test for example
# Scope on load test at https://jsonplaceholder.typicode.com

import time
from locust import HttpUser, TaskSet, task, between
import random

class SubClassTestAPI(TaskSet):

    @task
    def load_api(self):
        self.client.post('/posts')

    @task(3)
    def load_request(self):
        self.client.request(
            method = 'POST',
            url = '/posts/' + str(random.randrange(1, 10))
        )

class MainClassTestAPI(HttpUser):
    tasks = [SubClassTestAPI]
    wait_time = between(5, 10)