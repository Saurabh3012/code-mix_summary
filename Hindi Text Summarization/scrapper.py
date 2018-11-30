from selenium import webdriver
import time
from bs4 import BeautifulSoup
from pymongo import MongoClient
from urllib.parse import quote_plus
from newspaper import Article

uri = "mongodb://%s:%s@192.168.26.120:64646/hindi_summary" % (quote_plus("saurabh"), quote_plus("xxxxxxxx"))
client = MongoClient(uri)
db = client['hindi_summary']
collection = db["summary"]

url = "https://inshorts.com/hi/read/business"

driver = webdriver.PhantomJS("./phantomjs-2.1.1-macosx/bin/phantomjs")
driver.get(url)


html = driver.page_source.encode('utf-8')

page_num = 0


while True:

	if driver.find_elements_by_css_selector('.load-more'):
		driver.find_element_by_css_selector('.load-more').click()
		page_num += 1
		print("getting page number "+str(page_num))
		time.sleep(5)

	if page_num == 2:
		soup = BeautifulSoup(driver.page_source, features="html.parser")
		ids = []
		headlines = []
		summaries = []
		links = []
		news = []

		for i in soup.findAll("span", {"itemprop" : "mainEntityOfPage"}):
			ids.append(i['itemid'].split('-')[-1])
		for i in soup.findAll("span", {"itemprop" : "headline"}):
			headlines.append(i.text)
		for i in soup.findAll("div", {"itemprop" : "articleBody"}):
			summaries.append(i.text)
		for i in soup.findAll("div", {"class" : "read-more"}):
			
			uri_article =  i.a['href']
			article = Article(url)
			article.download()
			if article.html:
				article.parse()
				news.append(article.text)
			else:
				news.append("")

			links.append(i.a['href'])

		# print(ids[0])
		# print(headlines[0])
		# print(summary[0])
		# print(links[0])

		for i in range(len(ids)):
			

			obj = {
				"_id": ids[i],
				"headline": headlines[i],
				"summary": summaries[i],
				"src": links[i],
				"news": news[i]
			}

			collection.insert_one(obj)

		break


# while driver.find_elements_by_css_selector('.load-more'):
#     driver.find_element_by_css_selector('.load-more').click()
#     page_num += 1
#     # if page_num == 2:
#     # 	break
#     # print("HTML: ", driver.page_source)
#     # print("getting page number "+str(page_num))

#     soup = BeautifulSoup(driver.page_source)
article = Article(url)

	
	if article.html:
		article.parse()
		news.append(article.text)

#     headlines = soup.findAll("span", {"itemprop" : "headline"})

#     print(headlines)

#     time.sleep(1)

# html = driver.page_source.encode('utf-8')

