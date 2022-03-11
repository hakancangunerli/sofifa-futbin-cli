from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep, strftime
from bs4 import BeautifulSoup
import requests



input = str(input("Enter player name: "))
# put + between each space on the input
input = input.replace(" ", "%20")
link = "https://www.futbin.com/players?page=1&search=" + input

# use beautiful soup to scrape the page
new_link = link
webdriver = webdriver.Safari()

webdriver.get(new_link)
webdriver.maximize_window()
webdriver.execute_script("window.scrollTo(0, 400)")
sleep(5)
