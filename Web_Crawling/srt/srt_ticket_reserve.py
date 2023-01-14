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

id = '1581626207'
pwd = 'q77f9nDEUk*rjX'
date = '20230101'
bordingTime = '18'
startPlatform = '광주송정'
endPlatform = '수서'


# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')
driver.implicitly_wait(30) # 페이지 다 뜰 때 까지 기다림

driver.find_element(By.ID, 'srchDvNm01').send_keys(f'{id}') # 회원번호
driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys(f'{pwd}') # 비밀번호

driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()
driver.implicitly_wait(5)

driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do')
driver.implicitly_wait(5)

# 출발지 입력
dep_stn = driver.find_element(By.ID, 'dptRsStnCdNm')
dep_stn.clear() 
dep_stn.send_keys(f'{startPlatform}')

# 도착지 입력
arr_stn = driver.find_element(By.ID, 'arvRsStnCdNm')
arr_stn.clear()
arr_stn.send_keys(f'{endPlatform}')

# 날짜 드롭다운 리스트 보이게
elm_dptDt = driver.find_element(By.ID, "dptDt")
driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptDt)

# 2021년 10월 01일 기차 선택
Select(driver.find_element(By.ID,"dptDt")).select_by_value(f'{date}')

# 출발 시간
elm_dptTm = driver.find_element(By.ID, "dptTm")
driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptTm)
Select(driver.find_element(By.ID, "dptTm")).select_by_visible_text(f'{bordingTime}')

driver.find_element(By.XPATH,"//input[@value='조회하기']").click()
driver.implicitly_wait(5)

train_list = driver.find_elements(By.CSS_SELECTOR, '#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr')


while True:
    for i in range(1, 3): # 상위 4개 기차 확인
        standard_seat = driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7)").text

        if "예약하기" in standard_seat:
            print("예약 가능")       
            driver.find_element(By.XPATH, f"/html/body/div[1]/div[4]/div/div[3]/div[1]/form/fieldset/div[6]/table/tbody/tr[{i}]/td[7]/a/span").click()
            reserved = True
            bot = telegram.Bot(token = telgm_token)
            bot.sendMessage(chat_id = '1826029768', text="예매 성공")
            break
    if not reserved:
        # 5초 기다리기
        time.sleep(1)
        # 다시 조회하기
        submit = driver.find_element(By.XPATH, "//input[@value='조회하기']")
        driver.execute_script("arguments[0].click();", submit)
        print("새로고침")
        driver.implicitly_wait(10)
        time.sleep(1)
    else:
        break