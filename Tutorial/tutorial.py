from bs4 import BeautifulSoup
import requests
import csv
import winsound
import time



def beepbeep():
        winsound.Beep(500, 150)
        winsound.Beep(1000, 150)
        winsound.Beep(1500, 150)
        winsound.Beep(2000, 200)





source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source,'lxml')

csv_file = open('scraped_data.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Header','Summery','Video'])

for article in soup.find_all('article'):
    try:
        header = article.h2.text
        print("Header:\n\t"+header)

        sammary = article.div.p.text
        print("Sammary:\n\t"+sammary)

        vid = article.find('iframe')['src']
        vid_id = vid.split('/')[4]
        vid_id=vid_id.split('?')[0]
        vid_url = "https://www.youtube.com/watch?v="+vid_id

        csv_writer.writerow([header,sammary,vid_url])
    except Exception as e:
        vid_url="--NO VIDEO--"
        pass

    print("Video URL:\n\t" + vid_url)
csv_file.close()
time.sleep(0.5)
peepeep()
