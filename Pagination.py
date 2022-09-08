from pydoc import source_synopsis
from bs4 import BeautifulSoup
import requests
import time

def scrape(url: str) -> None:
    max_pages=  2
    current_page=1
    
    while current_page <=max_pages:
        current_url=f'{url}?page={current_page}'
        print(current_url)
        
        raw_html=requests.get(current_url)
        soup = BeautifulSoup(raw_html.text,'html.parser')
        
        
        
        
        
        for list in soup.find_all('div',class_="flex-1"):
            profession=list.find('p',class_="text-lg").text.replace('\n', '')
            company=list.find('p', class_="text-sm").text.replace('\n', '')
            location=list.find('span', class_="mb-3").text.replace('\n', '')
            type=list.find('p',class_="text-gray-500").text.replace('\n', '')
            jobs=[profession , company , location , type]
            print(jobs)
            
        time.sleep(10)
            
        current_page +=1
        
        print('\n\n') # Clearing console up
        
def main() -> int:
    url="https://www.brightermonday.co.ke/jobs"
    scrape(url)
    return 0

if __name__ == '__main__':
    exit(main())