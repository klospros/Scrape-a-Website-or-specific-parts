#Scrape whole webpage and save to a .html file
import urllib2

url = ('https://www.fasthosts.co.uk/careers/current-vacancies')

response = urllib2.urlopen(url)
content = response.read()

f = open('scrapewebsite.html', 'w')
f.write(content)
f.close
