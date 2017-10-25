#Scrape specific part of a website and save the output to a .html file
from lxml import html
import requests
import urllib2

page = requests.get('https://www.fasthosts.co.uk/careers/current-vacancies')
# Use requests.get to retrieve the web page with our data, parse it using the html module and save the results in the content request:

content = html.fromstring(page.content)
# Use page.content rather than page.text because html.fromstring implicitly expects bytes as input

Vacancies = content.xpath('//h1[@class="featuredvacancy__title featuredvacancy__title--invert grid-16 alpha"]/text()')
#This will create a list of Vacancies from the h1 class

f = open('scrapevacancy.html', 'w')
f.write('<br>'.join(map(str, Vacancies)))
f.close
