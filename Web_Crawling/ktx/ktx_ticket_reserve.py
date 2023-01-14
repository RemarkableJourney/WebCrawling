from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import telegram

reserved = False
telgm_token = '5710691276:AAG-TYuft-iD2GUnYQUFt4DM6x6YrWyNuJc'

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

id = '1773672386'
pwd = '$CWu5.EJUa~dvb'
# date = '20230101'
year = '2023'
month = '01'
day= '20'
bordingTime = '13'
startPlatform = '광명'
endPlatform = '광주송정'


# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.letskorail.com/korail/com/login.do')
driver.implicitly_wait(30) # 페이지 다 뜰 때 까지 기다림

driver.find_element(By.ID, 'txtMember').send_keys(f'{id}') # 회원번호
driver.find_element(By.ID, 'txtPwd').send_keys(f'{pwd}') # 비밀번호

driver.find_element(By.XPATH, '//*[@id="loginDisplay1"]/ul/li[3]/a/img').click()
driver.implicitly_wait(5)

driver.get('https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do')
driver.implicitly_wait(5)

#popup창 닫기
tabs = driver.window_handles
# print(tabs)
driver_count = len(driver.window_handles)
if driver_count != 1:
    driver_count = driver_count - 1
    driver.switch_to.window(driver.window_handles[driver_count]) 
    driver.close()
driver.switch_to.window(driver.window_handles[0])

# 열차 선택
driver.find_element(By.XPATH, '//*[@id="selGoTrainRa00"]').click()
driver.implicitly_wait(5)

# 출발지 입력
dep_stn = driver.find_element(By.ID, 'start')
dep_stn.clear() 
dep_stn.send_keys(f'{startPlatform}')

# 도착지 입력
arr_stn = driver.find_element(By.ID, 'get')
arr_stn.clear()
arr_stn.send_keys(f'{endPlatform}')

# 연도 선택
elm_s_year = driver.find_element(By.ID, "s_year").click()
# driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_s_year)
Select(driver.find_element(By.ID,"s_year")).select_by_value(f'{year}')

# 월 선택
elm_s_month = driver.find_element(By.ID, "s_month").click()
# driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_s_year)
Select(driver.find_element(By.ID,"s_month")).select_by_value(f'{month}')

# 날짜 선택
elm_s_day = driver.find_element(By.ID, "s_day").click()
# driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_s_year)
Select(driver.find_element(By.ID,"s_day")).select_by_value(f'{day}')

# 출발 시간 선택
elm_s_hour = driver.find_element(By.ID, "s_hour").click()
# driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptTm)
Select(driver.find_element(By.ID, "s_hour")).select_by_value(f'{bordingTime}')

# 조회하기
driver.find_element(By.XPATH, '//*[@id="center"]/form/div/p').click()
driver.implicitly_wait(5)

# dialog 닫기
driver.find_element(By.XPATH, '/html/body/div[4]/div[11]/div/button/span').click()
driver.implicitly_wait(5)

#popup창 닫기
tabs = driver.window_handles
# print(tabs)
driver_count = len(driver.window_handles)
if driver_count != 1:
    driver_count = driver_count - 1
    driver.switch_to.window(driver.window_handles[driver_count]) 
    driver.close()
driver.switch_to.window(driver.window_handles[0])

# train_list = driver.find_elements(By.CSS_SELECTOR, '#div.result > table > tbody > tr')
while True:
    for i in range(1, 3): # 상위 4개 기차 확인
        standard_seat = driver.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/div[1]/form[1]/div/div[4]/table[1]/tbody/tr[{i}]/td[6]//img").get_attribute("alt")
        # print(standard_seat)
        if standard_seat == "예약하기":
            print("예약 가능")       
            driver.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/div[1]/form[1]/div/div[4]/table[1]/tbody/tr[{i}]/td[6]/a[1]/img").click()
            reserved = True
            bot = telegram.Bot(token = telgm_token)
            bot.sendMessage(chat_id = '1826029768', text="예매 성공")
            break
    if not reserved:
        # 5초 기다리기
        time.sleep(1)
        # 다시 조회하기
        driver.find_element(By.XPATH, '//*[@id="center"]/div[3]/p/a/img').click()
        driver.implicitly_wait(5)
        # dialog 닫기
        driver.find_element(By.XPATH, '/html/body/div[4]/div[11]/div/button/span').click()
        driver.implicitly_wait(5)

        # popup창 닫기
        tabs = driver.window_handles
        driver_count = len(driver.window_handles)
        if driver_count != 1:
            driver_count = driver_count - 1
            driver.switch_to.window(driver.window_handles[driver_count]) 
            driver.close()
        driver.switch_to.window(driver.window_handles[0])

        print("새로고침")
        driver.implicitly_wait(10)
        time.sleep(1)
    else:
        break