from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep, strftime
from bs4 import BeautifulSoup
import requests



# Initialize webdriver object


input = str(input("Enter player name: "))
   # put + between each space on the input
input = input.replace(" ", "+")
webdriver = webdriver.Safari()
link = "https://sofifa.com/players/?keyword=" + input

# use beautiful soup to scrape the page
soup = BeautifulSoup(requests.get(link).text, "html.parser")
for name in soup.find_all("td", class_="col-name"):
        salary = name.parent.find('a')  # last cell in the row
        new_address = salary['href']
new_link = "https://sofifa.com" + new_address
print(new_link)
webdriver.get(new_link)
webdriver.maximize_window()
sleep(5)
webdriver.close()
