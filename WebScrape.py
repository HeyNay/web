from bs4 import BeautifulSoup
import requests
url = "https://weather.com/weather/tenday/l/Youngstown+OH?canonicalCityId=2793e44da479328c35f16aaab4bd1a229f11b2dac0caef70d1e9334fbfd08c3b"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
highday = soup.find(class_='DetailsSummary--highTempValue--3Oteu')
lownight = soup.find(class_='DetailsSummary--lowTempValue--3H-7I')
#temprn = soup.find(class_='styles--temperature--3MBn3')
print(soup.title.text)
print("High For Today is", highday.text)
print("Low For the Night is", lownight.text)
#print("Tempature Right Now is", temprn.text)
#for link in soup.find_all('a'):
#    print(link.get('href'))
