import time
from datetime import datetime
from src import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def wait_until_find_xpath(xpath):
    t = True
    failCount = 0
    maxFail = 5

    while t and failCount < maxFail:
        try:
            element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, xpath)))
            t = False
        except:
            t = True
            failCount = failCount + 1
            time.sleep(0.1)
    if (failCount == maxFail):
        return None
    else:
        return element

def wait_until_find_xpaths(xpath):
    t = True
    failCount = 0
    maxFail = 5

    while t and failCount < maxFail:
        try:
            element = driver.find_elements_by_xpath(xpath)
            t = False
        except:
            t = True
            failCount = failCount + 1
            time.sleep(0.1)
    if (failCount == maxFail):
        return None
    else:
        return element


def log(text):
  message = '['+str(datetime.now())+']$ '+ text
  file = open("automation.log","a") 
  file.write(message+'\n')
  file.close()
  print(message)