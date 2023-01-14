from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import telepot
import time

class KTX_Korail():
    def __init__(self):
        super().__init__()

    def login(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.letskorail.com/korail/com/login.do")
        time.sleep(1)
        self.driver.find_element(By.ID, "txtMember").send_keys("내 코레일멤버십번호 입력")
        self.driver.find_element(By.ID, "txtPwd").send_keys("코레일 비밀번호")
        # // 여기서 XPATH 경로에 id 값을 큰따옴표로 묶었기 때문에 해당 XPATH 경로는 작은따옴표로 묶는다.
        self.driver.find_element(By.XPATH, '//*[@id="loginDisplay1"]/ul/li[3]/a/img').click()
        self.driver.find_element(By.CSS_SELECTOR, "#header > div.lnb > div.lnb_m01 > h3 > a > img").click()

def korail_start_city(self, city):
    start_city = self.driver.find_element_by_id("start")
    start_city.clear()
    start_city.send_keys(city)
    start_city.send_keys(Keys.RETURN)

def korail_start_city(self, city):
    start_city = self.driver.find_element(By.ID,"start")
    start_city.clear()
    start_city.send_keys(city)
    start_city.send_keys(Keys.RETURN)

#도착지 입력
def korail_arrival_city(self, city):
    arrival_city = self.driver.find_element(By.ID,"get")
    arrival_city.clear()
    arrival_city.send_keys(city)
    arrival_city.send_keys(Keys.RETURN)

#년 선택
def korail_year_select(self, year):
    year_select = Select(self.driver.find_element(By.ID,"s_year"))
    year_select.select_by_value(year)

#월 선택
def korail_month_select(self, month):
    month_select = Select(self.driver.find_element(By.ID,"s_month"))
    month_select.select_by_value(month)

#일 선택
def korail_day_select(self, day):
    day_select = Select(self.driver.find_element(By.ID,"s_day"))
    day_select.select_by_value(day)

#시간 선택
def korail_hour_select(self, hour):
    hour_select = Select(self.driver.find_element(By.ID,"s_hour"))
    hour_select.select_by_value(hour)