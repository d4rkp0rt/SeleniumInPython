from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

driver = webdriver.Firefox()

driver.get("http://www.helenasflowers.co.uk")
WebDriverWait(driver, 5)
interaction_element = driver.find_element_by_xpath('//*[@id="pnlContent"]/div/p[5]/a')
interaction_element.click()

print('Starting page title is "' + driver.title + '"')

try:
    result = WebDriverWait(driver, 5).until(EC.title_contains("Online Shop"))
    print ("PASS: Title is: " + driver.title)
except:
    print("FAIL: Cannot find 'Online Shop' page title")

interaction_element = driver.find_element_by_xpath('//*[@id="rptProducts_ctl00_ProductSummary1_moreLinkImage"]')
interaction_element.click()

interaction_element = driver.find_element_by_xpath('//*[@id="ProductDetails1_productPriceList_2"]')
interaction_element.click()

interaction_element = driver.find_element_by_xpath('//*[@id="ProductDetails1_imgBuy"]')
interaction_element.click()

try:
    result = WebDriverWait(driver, 5).until(EC.title_contains("Online Shop - Checkout"))
    print("PASS: Title is: " + driver.title)
except:
    print("FAIL: Cannot find 'Online Shop - Checkout' page title")
finally:
    driver.quit()
