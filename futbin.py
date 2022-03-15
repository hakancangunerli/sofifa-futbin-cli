#NOTE: THIS IS DESIGNED FOR SAFARI WEBDRIVERS ONLY.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep, strftime
from bs4 import BeautifulSoup
import requests
import cloudscraper
import re


def futbin(input):
    global webdriver
    # put + between each space on the input
    input = input.replace(" ", "%20")
    link = "https://www.futbin.com/players?page=1&search=" + input

    # use beautiful soup to scrape the page
    try:
        new_link = link
        webdriver = webdriver.Safari()
    #webdriver.get(new_link)
        webdriver.maximize_window()

        webdriver.execute_script("window.scrollTo(0, 400)")

        scraper = cloudscraper.create_scraper()

    # # this line works scraper.get(new_link).text

    # # i'll have to write this into a file once i obtain the html since cloudfare blocks the request

        temp = scraper.get(new_link).text

    # print temp result to an html file

        with open("futbin.html", "w") as f:
            f.write(temp)

    # get the table from the html file
        soup2 = BeautifulSoup(open("futbin.html"), "html.parser")

        tr_elements = soup2.find_all('table')[0].find_all('tr')
    except IndexError:
        print("You are being blocked by Cloudflare")
        exit()
    with open("tr_elements.html", "w") as f:
        f.write(str(tr_elements))

    dataLog = []
    general_type = '/22/player/'

    with open('tr_elements.html', 'rt') as f:
        data = f.readlines()
    for line in data:
        if general_type in line:
            dataLog.append(line)

    # if the element matches href, then it is the link to the player page
    # put that into a newlist called addressList

    addressList = []
    for i in dataLog:
        if 'href' in i:
            addressList.append(i)

    # from this list, get the number between /player/ and /
    addressNumbers = []
    for i in addressList:
        addressNumbers.append(i[i.find('/player/') + len('/player/')                          :i.find('/', i.find('/player/') + len('/player/'))])


    # the address numbers are the player ids, we don't actually need the player name.

    for i in addressNumbers:
        # open the tab in the new window
        webdriver.execute_script(
            "window.open('https://www.futbin.com/player/" + str(i) + "/', '_blank')")
        sleep(5)
