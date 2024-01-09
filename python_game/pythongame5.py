#!pip install BeautifulSoup4
#!pipinstall requests
#슈퍼개미게임 : 임의의 주식이 오늘 올랐는지, 떨어졌는지 선택하면 되는 간단한 게임입니다! 틀리면 마셔~! 
from main import players
import random
import requests
import time
from bs4 import BeautifulSoup as bs

url="https://finance.naver.com/"

header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"} #네이버 페이지 입장용 헤더
response=requests.get(url, headers=header)

soup = bs(response.text, 'html.parser')

top_items_tbody = soup.find('tbody', {'id': '_topItems1'}) #주식 거래 top 

item_names = [a.text for a in top_items_tbody.find_all('a')] #주식 이름 텍스트
item_change = [span.text for span in top_items_tbody.find_all('span')] #주식 상승, 하락 텍스트 가져오기
item_change_value = [tr.find_all('td')[2].text for tr in top_items_tbody.find_all('tr')] # 주식 상승 하락 값

number_range = range(0, len(item_names)-1)
fail_player =[]

def antgame(players, username):
    num_of_random_numbers = len(players)
    random_numbers = random.sample(number_range, num_of_random_numbers)

    print('개미는~뚠뚠!🐜 오늘도~뚠뚠!🐜 열심히~주식~하네~🐜 오늘의 주식이 상승했는지 하강했는지 맞춰보세요!')

    for i in range(len(players)):
        print(f"{players[i]['name']}님 차례입니다")
        print(f"{item_names[random_numbers[i]]}는 오늘 상승했을까요? 하락했을까요?")

        while True:
            try:
                if(players[i]['name']==username):
                    answer=input('1.상승 2.하락 :')
                    if not (answer=='1' or answer =='2'):
                        raise ValueError
                else:
                    answer=random.choice(['1', '2'])
                    if answer=='1':
                        print('상승한다!📈')
                    else:
                        print('하락한다!⬇️')
                if((answer=='1' and item_change[random_numbers[i]]=='상승') or (answer=='2' and item_change[random_numbers[i]]=='하락')):
                    print("정답입니다! 촉이 좋은 개미시군요!!😎")
                    print(f"{item_names[random_numbers[i]]}는 오늘 {item_change_value[random_numbers[i]]} {item_change[random_numbers[i]]}했어\n")
                    break
                else:
                    print("당신은 주식하면 큰일나겠네요!😮")
                    print(f"{item_names[random_numbers[i]]}는 오늘 {item_change_value[random_numbers[i]]} {item_change[random_numbers[i]]}했어")
                    print(f"{players[i]['name']} 한잔해~🍻\n")
                    fail_player.append(players[i]['name'])
                    break
            except ValueError:
                print("1과 2만 입력해주세요!")
        time.sleep(1)
    return fail_player

