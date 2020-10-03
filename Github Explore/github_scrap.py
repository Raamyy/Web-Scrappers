import requests
from bs4 import BeautifulSoup

source = requests.get("https://github.com/explore")
soup = BeautifulSoup(source.content,'html.parser')

repos = soup.find_all('article',class_="border rounded-1 box-shadow bg-gray-light my-4")

for repo in repos:
    node = repo.find('h1').find_all('a')
    user = node[0].get_text().strip()
    try:
        repo_name = node[1].get_text().strip()
        print(user+"/"+repo_name)
    except:
        print(user)



