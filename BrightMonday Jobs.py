from bs4 import BeautifulSoup
import requests
from csv import writer


url="https://www.brightermonday.co.ke/jobs"
page=requests.get(url)
#print(page)


soup=BeautifulSoup(page.content, 'html.parser')
lists=soup.find_all('div',class_="flex-1")


with open('Jobs.csv', 'w', encoding='utf8', newline='') as a:
    thewriter=writer(a)
    Header=['Profession','Company','Locatiion', 'Type']
    thewriter.writerow(Header)
     
    for list in lists:
        profession=list.find('p',class_="text-lg").text.replace('\n', '')
        company=list.find('p', class_="text-sm").text.replace('\n', '')
        location=list.find('span', class_="mb-3").text.replace('\n', '')
        type=list.find('p',class_="text-gray-500").text.replace('\n', '')
        jobs=[profession , company , location , type]
        #print(jobs)
        thewriter.writerow(jobs)