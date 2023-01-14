import telepot
from kor.korail import *
import re


class KTX_Telegram():
    def __init__(self):
        print('텔레그램 시작합니다.')
        self.token = "5710691276:AAG-TYuft-iD2GUnYQUFt4DM6x6YrWyNuJc";
        self.bot = telepot.Bot(self.token)
        #아래 KTX_Korail()은 kor/korail.py 파일의 class명이다. 다음단계에서 생성할 예정이므로 주석처리한다.
        #self.korail = KTX_Korail()
        self.bot.message_loop(self.conversation_telegram)
        while True:
            pass
       
        def conversation_telegram(self, msg):
            print(msg)

def conversation_telegram(self, msg):
    con_text = msg['text']
    chat_id = msg['chat']['id']
    
    if con_text == '로그인':
        self.bot.sendMessage(chat_id = '1826029768', text="로그인중입니다. 잠시만 기다려주세요")
        #아래 korail의 login() 함수는 다음단계에서 진행할 예정이므로 주석처리한다.
        #self.korail.login()
        self.bot.sendMessage(chat_id = '1826029768', text="로그인 완료")
    
    start_city = re.compile("출발*")
    start_city_find = re.compile("[^출발]")
    
    if start_city.match(con_text):
        city_name = start_city_find.findall(con_text)
        city_name = ''.join(city_name)
        self.korail.korail_start_city(city_name)
        #출발지 설정을 위한 정규표현식
    start_city = re.compile("출발*")
    start_city_find = re.compile("[^출발]")

    #목적지 설정을 위한 정규표현식
    arrival_city = re.compile("도착*")
    arrival_city_find = re.compile("[^도착]")

    #년을 선택하기 위한 정규표현식
    year_select = re.compile("202\d{1}년")
    year_select_find = re.compile("[^년]")

    #월을 선택하기 위한 정규표현식
    month_select = re.compile("[0-9]+월")
    month_select_find = re.compile("[^월]")

    #일을 선택하기 위한 정규표현식
    day_select = re.compile("[0-9]+일")
    day_select_find = re.compile("[^일]")

    #시간을 선택하기 위한 정규표현식
    hour_select = re.compile("[0-9]+시")
    hour_select_find = re.compile("[^시]")

    if start_city.match(con_text):
        start_city_name = start_city_find.findall(con_text)
        start_city_name = ''.join(start_city_name)
        self.korail.korail_start_city(start_city_name)

    if arrival_city.match(con_text):
        arrival_city_name = arrival_city_find.findall(con_text)
        arrival_city_name = ''.join(arrival_city_name)
        self.korail.korail_arrival_city(arrival_city_name)

    if year_select.match(con_text):
        year_select_name = year_select_find.findall(con_text)
        year_select_name = ''.join(year_select_name)
        self.korail.korail_year_select(year_select_name)

    if month_select.match(con_text):
        month_select_name = month_select_find.findall(con_text)
        month_select_name = ''.join(month_select_name)
        self.korail.korail_month_select(month_select_name)

    if day_select.match(con_text):
        day_select_name = day_select_find.findall(con_text)
        day_select_name = ''.join(day_select_name)
        self.korail.korail_day_select(day_select_name)

    if hour_select.match(con_text):
        hour_select_name = hour_select_find.findall(con_text)
        hour_select_name = ''.join(hour_select_name)
        self.korail.korail_hour_select(hour_select_name)
    
    if con_text == "검색":
            self.korail.korail_search()

    if con_text == "결과":
        self.token = "BotFather를 통해 봇을 생성했을때 주는 HTTP API token값"
        self.bot = telepot.Bot(self.token)
        # self.bot.sendMessage(chat_id, result)
    



# def sendMessage(self, chat_id, text,
#                 parse_mode=None,
#                 disable_web_page_preview=None,
#                 disable_notification=None,
#                 reply_to_message_id=None,
#                 reply_markup=None):
#     """ See: https://core.telegram.org/bots/api#sendmessage """
#     p = _strip(locals())
#     return self._api_request('sendMessage', _rectify(p))