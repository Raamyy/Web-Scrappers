import requests
from bs4 import BeautifulSoup
from datetime import datetime

source = requests.get("https://github.com/explore")
soup = BeautifulSoup(source.content,'html.parser')

repos = soup.find_all('article',class_="border rounded-1 box-shadow bg-gray-light my-4")

csv_file = open('data.csv','w+')
csv_file.write('scrapped_on,title,repo_owner,repo_name,repo_description,repo_tags,repo_last_updated,repo_language,repo_link,user_link\n')

for repo in repos:
    try:
        node = repo.find('h1').find_all('a')    
        user = node[0].get_text().strip()
        repo_name = node[1].get_text().strip()
        
        title = repo.find('div', class_="f6 text-gray px-3 mt-3").get_text().strip()
        repo_description = repo.find('div', class_='px-3 pt-3').get_text().strip().replace(',',' ')
        tags = map(lambda a_node: a_node.get_text().strip() ,repo.find('div', class_="d-flex flex-wrap border-bottom border-gray-light px-3 pt-2 pb-2").find_all('a'))
        last_updated, language =map(lambda node:' '.join(node.get_text().split()) ,repo.find_all('li'))

        csv_file.write(f'{datetime.now()},{title},{user},{repo_name},{repo_description},{"/".join(list(tags))},{last_updated.replace(","," ")},{language},{f"https://www.github.com/{user}/{repo_name}"},{f"https://www.github.com/{user}"}\n')
    except:
        print(user) # these are not repos, we are targeting repos only
        pass



