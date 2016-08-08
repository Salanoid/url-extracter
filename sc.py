import urllib
from bs4 import BeautifulSoup
import validators

print('Add website: ')
s = input()

try: 
	connection = urllib.request.urlopen(s)
	soup = BeautifulSoup(connection, 'html.parser')

	for link in soup.find_all('a'):
		if validators.url(link.get('href')) == True:
			print(link.get('href'))

except urllib.error.URLError as e:
	print(e.reason)

