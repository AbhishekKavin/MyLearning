'''
Real-World Use Case: Multithreading for I/O-Bound Tasks
Scenario: Web Scraping
Description: Web scraping often involves making multiple network requests to fetch data from various web pages. 
Since network I/O operations can be slow and blocking, using multithreading can significantly improve the efficiency of the scraping process by allowing multiple requests to be handled concurrently.
'''

import threading
import requests
from bs4 import BeautifulSoup

urls = ['https://docs.langchain.com/oss/python/langchain/overview',
'https://docs.langchain.com/oss/python/langchain/philosophy',
'https://docs.langchain.com/oss/python/langchain/quickstart']

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads = []

for url in urls:
    thread=threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Completed fetching all URLs.")
