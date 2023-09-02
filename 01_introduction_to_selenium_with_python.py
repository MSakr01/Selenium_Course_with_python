# ----------------------------------------
# -- pip install selenium==4.12.0
# -- pip install webdriver-manager
# ----------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# executable_path = "C:\Program Files\chromedriver.exe"
# service = Service(executable_path=executable_path)

# Install Webdriver
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

# open url
driver.get("https://youtube.com/")
driver.get("https://google.com/")

sleep(10)

