import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=5, backoff=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt == retries - 1:
                raise NetworkError(f'Failed to retrieve {url} after {retries} attempts') from e
            time.sleep(backoff ** attempt)  # Exponential backoff

if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except NetworkError as ne:
        print(ne)