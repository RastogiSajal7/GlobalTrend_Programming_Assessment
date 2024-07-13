import requests
from time import sleep

def download_urls(urls):
    results = {}
    max_retries = 3
    backoff_factor = 1

    for url in urls:
        attempt = 0
        success = False

        while attempt < max_retries and not success:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                results[url] = response.text
                success = True
            except requests.exceptions.Timeout:
                print(f"Timeout occurred while trying to access the URL: {url}. Retrying attempt {attempt + 1} of {max_retries}.")
            except requests.exceptions.RequestException as e:
                print(f"Request failed for URL: {url}. Encountered error: {e}. Retrying attempt {attempt + 1} of {max_retries}.")
            except Exception as e:
                print(f"An unexpected error occurred while accessing URL: {url}. Error details: {e}. Retrying attempt {attempt + 1} of {max_retries}.")

            attempt += 1
            if not success and attempt < max_retries:
                sleep(backoff_factor * attempt)

        if not success:
            results[url] = None

    return results

urls = [
    "https://www.globaltrend.co.in",
    "https://fakewebsite.in"  
]

downloaded_content = download_urls(urls)
for url, content in downloaded_content.items():
    if content:
        print(f"Successfully retrieved content from: {url}")
    else:
        print(f"Failed to retrieve content from: {url} after multiple attempts.")
