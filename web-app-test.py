# Author ashsepra@gmail.com
# This load test for example
# Scope on load test at wikipedia

import time
from locust import HttpUser, TaskSet, task, between

class LoadTest(TaskSet):

    @task
    def main_page(self):
        self.client.get('/wiki/Halaman_Utama')

    @task(2)
    def perihal_page(self):
        self.client.get('/wiki/Wikipedia:Perihal')


class LoadTest(HttpUser):
    tasks = [LoadTest]
    wait_time = between(5, 10)