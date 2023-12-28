# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
import time

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 https://www.w3schools.com/ 입력
url = "https://deal.11st.co.kr/browsing/DealAction.tmall?method=getShockingDealMain"
browser.get(url)

# - 가능 여부에 대한 OK 받음
pass