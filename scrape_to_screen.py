#Scrape specific part of a website and display output to screen
from lxml import html
import requests

page = requests.get('https://www.fasthosts.co.uk/careers/current-vacancies')
# Use requests.get to retrieve the web page with our data, parse it using the html module and save the results in the content request:
content = html.fromstring(page.content)
# Use page.content rather than page.text because html.fromstring implicitly expects bytes as input

Vacancies = content.xpath('//h1[@class="featuredvacancy__title featuredvacancy__title--invert grid-16 alpha"]/text()')
#This will create a list of Vacancies from the h1 class

print Vacancies
