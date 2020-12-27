# Author ashsepra@gmail.com
# This load test for example
# Scope on load test at https://api.apiary.io

import time
from locust import HttpUser, TaskSet, task, between
import json

class SubClassTestAppAPI(TaskSet):

    @task
    def create_token(self):
        # Request token
        header_auth_token = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic dGVzdEB0ZXN0LnRlc3Q6dGVzdHRlc3Q='
        }
        request_body_token = 'tokenDescription=What%27s%20this%20token%20for%3F&tokenRegenerate=false'
        with self.client.post(
            '/authorization',
            data = request_body_token,
            headers = header_auth_token,
            catch_response = True
        ) as response_token:
            if response_token.status_code == 201:
                response_token.success()
                res_payload_token = json.loads(response_token.text)
                token = res_payload_token['token']

                # Get the me data with auth token
                with self.client.request(
                    method='GET',
                    url='/me',
                    headers={
                        'Authorization': 'Bearer ' + token
                    },
                    catch_response = True
                ) as response_me:
                    if response_me.status_code == 200:
                        response_me.success()
                    else:
                        response_me.failure('Error request me ' + response_me.text)
            else:
                response_token.failure('Error request token ' + response_token.text)



class MainClassTestAppAPI(HttpUser):
    tasks = [SubClassTestAppAPI]
    wait_time = between(5, 10)