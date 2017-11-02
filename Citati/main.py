from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import random
url = "http://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(url).read()

soup = BeautifulSoup(response)

#print soup.title.string

quotes = soup.findAll("p", attrs={"class": "quoteContent"})

j=0
for quote in quotes:
    if j<5:
        print (str(j+1)+". "+quote.string)
    else:
        break
    j += 1

#random

j=0
for quote in quotes:
    if j<5:
        new_links = quotes[random.randint(0, len(quotes) - 1)]
        print (str(j+1)+". "+new_links.string)
    else:
        break
    j += 1
