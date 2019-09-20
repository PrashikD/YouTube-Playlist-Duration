import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/playlist?list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj'
head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
req = requests.get(url, headers=head)

soup = BeautifulSoup(req.text, "html5lib")

hours = 0
minutes = 0
seconds = 0

timestamps = soup.find_all('span', class_=["style-scope", "ytd-thumbnail-overlay-time-status-renderer"])

print(len(timestamps))
durations = []
for x in timestamps:
    durations.append(x.span.text)


for x in durations:
    if x.count(':') == 1:
        minutes += int(x.split(':')[0])
        seconds += int(x.split(':')[1])
    if x.count(':') == 2:
        hours += int(x.split(':')[0])
        minutes += int(x.split(':')[1])
        seconds += int(x.split(':')[2])

full_hours = 0
full_minutes = 0
full_seconds = hours*3600 + minutes*60 + seconds

full_hours = full_seconds//3600
full_minutes = (full_seconds - (3600*full_hours))//60
full_seconds = (full_seconds - (3600*full_hours) - (full_minutes*60))

print(f'Total Duration of the Playlist is {full_hours} hours, {full_minutes} minutes and {full_seconds} seconds')
