import time
import requests

class NetworkError(Exception):
    pass

class NetworkHandler:
    def __init__(self, max_retries=3, backoff_factor=2):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def fetch_data(self, url):
        retries = 0
        while retries < self.max_retries:
            try:
                response = requests.get(url)
                response.raise_for_status()
                return response.json()
            except requests.RequestException:
                retries += 1
                wait_time = self.backoff_factor ** retries
                print(f'Retry {retries}/{self.max_retries} in {wait_time} seconds...')
                time.sleep(wait_time)
        raise NetworkError('Max retries exceeded')

if __name__ == '__main__':
    handler = NetworkHandler()
    url = 'https://api.example.com/data'
    try:
        data = handler.fetch_data(url)
        print('Data retrieved:', data)
    except NetworkError as e:
        print(e)