from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = 'https://www.draftsharks.com/fantasy-football-news'

path = '../.cache/yay/chromedriver'

service = Service(executable_path=path)

driver = webdriver.Chrome(service=service)
driver.get(website)
