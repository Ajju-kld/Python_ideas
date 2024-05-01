import concurrent.futures
import requests

API_ENDPOINT = "https://api.140.ieeer10.org/api/activity/list"

session = requests.Session()

def send_request(url):
    try:
        response=session.get(url)
        return response.status_code
    except Exception as e:
        print(e)
        return None
    
NUM_USERS=100000
urls=[API_ENDPOINT] * NUM_USERS


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(send_request, urls))
    
successes = sum(1 for result in results if result == 200)
failed_requests = len(results) - successes
print("Results:{NUM_USERS}")
print(f"Successful requests: {successes}")
print(f"Failed requests: {failed_requests}")

    
