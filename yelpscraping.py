import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from tkinter import ttk

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.yelp.com')
driver.implicitly_wait(20)
searchBarOne = driver.find_element(By.ID, "search_description")
searchBarOne.send_keys("Restaurants")
searchBarTwo = driver.find_element(By.ID, "search_location")
searchBarTwo.click()
searchBarTwo.send_keys("Anchorage, AK")
driver.find_element(By.CLASS_NAME, "find-near-button__09f24__XS9AP.css-dew2bp").click()

rating_collection = []
business_names = []
for i in range(3):
    time.sleep(3)
    ratings = driver.find_elements(By.CLASS_NAME,
                                   'five-stars__09f24__mBKym.five-stars--regular__09f24__DgBNj.display--inline-block__09f24__fEDiJ.border-color--default__09f24__NPAKY')
    businesses = driver.find_elements(By.CLASS_NAME, 'css-1m051bw')
    for j in ratings:
        rating_collection.append(j.get_attribute("aria-label"))
    for k in businesses:
        business_names.append(k.text)
    nextButton = driver.find_element(By.CLASS_NAME, "next-link.navigation-button__09f24__m9qRz.css-144i0wq")
    nextButton.click()

print(rating_collection)


print(len(business_names))
print(len(rating_collection))




words = ['Restaurants', 'Anchorage, AK']
for r in business_names:
    if r in words:
        business_names.remove(r)

for r in business_names:
    if r == 'Restaurants':
        business_names.remove("Restaurants")


