import threading
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

urls = ['https://docs.langchain.com/oss/python/langchain/overview',
'https://docs.langchain.com/oss/python/langchain/philosophy',
'https://docs.langchain.com/oss/python/langchain/quickstart']

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

with ThreadPoolExecutor(max_workers = 3) as executor:
    executor.map(fetch_content, urls)
