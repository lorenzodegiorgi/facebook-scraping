from selenium import webdriver
import os
from bs4 import BeautifulSoup
from time import sleep
import random
import csv
import logging


logging.basicConfig(level=logging.ERROR)

# CONFIGURATION VARIABLES
LIMIT = 400 # Number of likers in each page
LOADING_PAGE_TIME = 8 # Waiting time to load the new page
MIN_WAITING_TIME = 5 # Min waiting time to load the next page
MAX_WAITING_TIME = 10 # Max waiting time to load the next page
ERROR_WAITING = 10 #Time to wait before a new attempt
LINKS_FILE = "links.txt"


links = open(LINKS_FILE, "r")
file_index = 0

# Driver initialization
driver_path = os.path.abspath('chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=selenium")
browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

def scraping_process(cycles, browser, name_scraped, filename):
    logging.debug('Starting %s cycle', cycles)
    # Due to the limitations of 4500 likes per pages, break the scraping after 75 cycles
    if (cycles > 80):
        return (1, name_scraped)
    sleep(LOADING_PAGE_TIME)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    # Extracting h3 elements that contain all info about the liker
    person_link = soup.find_all('div', class_='_1uja')
    name_scraped += len(person_link)
    logging.debug('Name scraped: %s ', len(person_link))
    logging.debug('Writing CSV file')
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for data in person_link:
            writer.writerow([data.find('a')['href']])

    next_link = browser.find_elements_by_xpath("//a[@class='touchable primary']")
    if len(next_link) > 0:
        removed_div = browser.find_elements_by_xpath("//div[@id='reaction_profile_browser']")
        browser.execute_script("""
                    var element = arguments[0];
                    element.innerHTML = ''
                    """, removed_div[0])
        sleep(random.randint(MIN_WAITING_TIME, MAX_WAITING_TIME))
        next_link[0].click()
        return (0, name_scraped)
    else:
        return (1, name_scraped)

for line in links:
    cycles = 0
    name_scraped = 0
    file_index += 1
    filename = "results_" + str(file_index) + ".csv"
    print(filename)
    if not os.path.exists(filename):
        open(filename, "w+").close()

    # Scraping process
    logging.debug('Scraping initialization')
    browser.get(line)

    logging.debug("Starting scraping: %s", line)

    while 1:
        try:
            state, local_name_scraped = scraping_process(cycles, browser, name_scraped, filename)
            cycles += 1
            name_scraped += local_name_scraped
            if(state == 1): break
        except Exception as e:
            logging.error("An error occurs with %s ", browser.current_url)
            print(e);
            logging.error("%s", e);
            sleep(ERROR_WAITING)
            with open(filename, 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                #Writing on the CSV file that an error occurs in order to make it invalid
                writer.writerow(["AN ERROR OCCURS"]);
                break


links.close()
logging.debug('Total names scraped: %s', name_scraped)
browser.quit()
