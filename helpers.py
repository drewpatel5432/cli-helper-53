import time
import random
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=5, backoff_factor=1.0):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            retries += 1
            if retries == max_retries:
                raise NetworkError(f'Failed after {max_retries} retries')
            wait_time = backoff_factor * (2 ** (retries - 1)) + random.uniform(0, 1)
            time.sleep(wait_time)
            print(f'Retrying... {retries}/{max_retries}')