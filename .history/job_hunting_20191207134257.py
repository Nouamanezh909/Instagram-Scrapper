import requests
from bs4 import BeautifulSoup
from Scrapp_info import Info_Scrapper
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# defining url
global start_url

# indeed url only for 'morocco' jobs
start_url = "https://ma.indeed.com"

# path for chrome webdrive (change this path accordding to my pc)
driver = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver")

# search string

job_title = str(input("what job type you looking for?!! " + "\n"))
# fire (target url)

driver.get(start_url)

# associate the search with indeed search

element = driver.find_element_by_xpath('//*[@id="text-input-what"]')
element.send_keys(job_title)

# befor hitting enter pause for 3
time.sleep(3)
job_title.send_keys(Keys.ENTER)





#getting users posts

# all_posts == []

# def Scrapp_posts(post_link):
# 	# locate tag with number of followers
# 	soup = BeautifulSoup(start_url, 'html.parser')
# 	data = soup.text
# 	find_attribute = data.find_all('meta', attrs={'property': 'og:description'})
# 	followers = find_attribute[0]

# 	#giving spesific number to small profiles
# 	#small_profile = 100
# 	# mediocre_profile = 500
# 	# viral_profile = 1000

# 	find_posts  = driver.find_element_by_class_name('v1Nh3')
# 	find_posts.find_element_by_css_selector('a').get_attribute('href')

# 	driver = webdrive.Chrome("C:\\Users\\nouamane\\Downloads\\chromedriver")
