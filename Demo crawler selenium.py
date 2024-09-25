from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
chrome_driver_path = "C:/Program Files (x86)/chromedriver.exe"
service = Service(chrome_driver_path)  
driver = webdriver.Chrome(service=service) 

urls = ["https://www.techwithtim.net/", "https://baomoi.com/#:~:text=Tin%20nhanh%20Vi%E1%BB%87t%20Nam%20v%C3%A0%20th%E1%BA%BF%20gi%E1%BB%9Bi%20h%C3%B4m%20nay,%20li%C3%AAn"]  # Thêm các URL khác nếu cần
results = []

for url in urls:
    driver.get(url)
    title = driver.title
    results.append({"title": title, "url": url})

output_file = "results.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

driver.quit()

