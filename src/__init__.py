from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)

driver = webdriver.Chrome()
