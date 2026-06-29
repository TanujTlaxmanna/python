import pandas as pd
import requests
from bs4 import BeautifulSoup

print(requests.get('https://www.ambitionbox.com/list-of-companies?page=1'))
print(requests.get('https://www.ambitionbox.com/list-of-companies?page=1').text)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
}
webpage = requests.get('https://www.ambitionbox.com/list-of-companies?page=1', headers = headers).text
print(webpage)

soup =  BeautifulSoup(webpage, 'lxml') # lxml is a html parser

print(soup.prettify())
print(soup.find_all('h1')[0].text)

print(len(soup.find_all('h2')[0].text))
print(soup.find_all('h2')[0].text)

for i in soup.find_all('h2'):
    print(i.text.strip())  # strip will remove all spaces and \n


print(len(soup.find_all('p', class_ = 'rating_star_container')))
print(soup.find_all('p', class_ = 'rating_star_container'))

print(len(soup.find_all('a', class_ = 'review-count')))
print(soup.find_all('a', class_ = 'review-count'))

company = soup.find_all('div', class_ = 'companyCardWrapper__companyName')
print(len(company))

name = []
rating = [] 
reviews = []
ctype = []
hq = []
old = []
employees = []


for i in company:
    # print(i.find('h2').text.strip())
    name.append(i.find('h2').text.strip())
    rating.append(i.find('p', class_ = 'rating_star_container').text.strip())
    rating.append(i.find_all('a', class_ = 'review-count')[0].text.strip())
    ctype.append(i.find_all('p', class_ = 'infoEntity')[0].text.strip())
    hq.append(i.find_all('p', class_ = 'infoEntity')[0].text.strip())
    old.append(i.find_all('p', class_ = 'infoEntity')[0].text.strip())
    employees.append(i.find_all('p', class_ = 'infoEntity')[0].text.strip())


print(name)
print(rating)
print(reviews)

company[0].find_all('p', class_ = 'infoEntity')[0].text.strip()

d = {'name' : name,
     'ratings' : rating,
     'reviews' : reviews,
     'company types' : ctype,
     'headquaters' : hq,
     'how old' : old,
     'employees' : employees}

df = pd.DataFrame(d)
print(df)

final = pd.DataFrame()
for j in range (1,333):

    url = 'https://www.ambitionbox.com/list-of-companies?page={}'.format(j)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
    }
    webpage = requests.get(url, headers = headers).text
    print(webpage)

    soup =  BeautifulSoup(webpage, 'lxml') 
    company = soup.find_all('div', class_ = 'companyCardWrapper__companyName')

    name = []
    rating = [] 
    reviews = []
    ctype = []
    hq = []
    old = []
    employees = []


    for i in company:
        # print(i.find('h2').text.strip())
        name.append(i.find('h2').text.strip())
        rating.append(i.find('p', class_ = 'rating_star_container').text.strip())
        rating.append(i.find_all('a', class_ = 'review-count')[0].text.strip())
        ctype.append(i.find_all('p', class_ = 'infoEntity')[0].text.strip())
        hq.append(i.find_all('p', class_ = 'infoEntity')[0].text.strip())
        old.append(i.find_all('p', class_ = 'infoEntity')[0].text.strip())
        employees.append(i.find_all('p', class_ = 'infoEntity')[0].text.strip())

    d = {'name' : name,
     'ratings' : rating,
     'reviews' : reviews,
     'company types' : ctype,
     'headquaters' : hq,
     'how old' : old,
     'employees' : employees}

    df = pd.DataFrame(d)    

    final = final.append(df, ignore_index = True)