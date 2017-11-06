from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import random
url = "http://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(url).read()

soup = BeautifulSoup(response)

#print soup.title.string

quotes = soup.findAll("p", attrs={"class": "quoteContent"})

i=0
for quote in quotes[:5]:
    i+=1
    print (str(i)+". "+quote.string)


#random
for i in range (0,5):

    new_links = quotes[random.randint(0, len(quotes) - 1)]
    print (str(i + 1) + ". " + new_links.string)



