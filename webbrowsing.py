import tkinter

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
driver.get('https://www.ebay.com/')
driver.implicitly_wait(20)
searchBar=driver.find_element(By.CLASS_NAME, "gh-tb.ui-autocomplete-input")
user_item=input("Enter the item, you want to look on ebay")
searchBar.send_keys(user_item)

driver.find_element(By.CLASS_NAME,"btn.btn-prim.gh-spr").click()
driver.implicitly_wait(10)
# items=driver.find_elements(By.CLASS_NAME,"s-item__details.clearfix")
items=driver.find_elements(By.CLASS_NAME,"s-item__title")



# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Do You Like To Add Extra Features?").grid(column=0, row=0)
# ttk.Button(frm, text="Submit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()





series_sixWatch=[]
other_watches=[]
for item in items:
    if "Apple Watch Series 6" in item.text:
        series_sixWatch.append(item.text)
    else:
        other_watches.append(item.text)

print(series_sixWatch)
print(other_watches)

# driver.maximize_window()
index=2
# items = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'MAIN.template=SEARCH_RESULTS.widgetId=search-results')))







