import random

gamestate = False
drinklimit = 0

#게임 시작시 필요한 정보 받는 함수
def gamestart():
    global gamestate, drinklimit, username
import game_369
import json
import subwayGame
import pythongame5
import game_capital
import egudongseong
#***********여기에 각자 게임 모듈 임포트*********
import time

class NotInRangeError(Exception):
    pass

def gamestart():
    global gamestate, drinklimit, username, npclist
    print("-"*130)
    print("-"*130)
    print("""     
           
           ████████╗███████╗ █████╗ ███╗   ███╗     ██╗    ███████╗██╗   ██╗██╗          ██████╗  █████╗ ███╗   ███╗███████╗
           ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║    ███║    ██╔════╝██║   ██║██║         ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
              ██║   █████╗  ███████║██╔████╔██║    ╚██║    ███████╗██║   ██║██║         ██║  ███╗███████║██╔████╔██║█████╗  
              ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║     ██║    ╚════██║██║   ██║██║         ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
              ██║   ███████╗██║  ██║██║ ╚═╝ ██║     ██║    ███████║╚██████╔╝███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
              ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝    ╚══════╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                                                                                                                                                                                                                                                                                                                                                                                                           
          """)
    print("-"*130)
    print ("""
ᕬ ᕬ                                                       ᕬ ᕬ                                                       ᕬ ᕬ 
(˶ㅇᗜㅇ˶) ⑉♥ 콸콸콸 ~ 콸콸콸 ~ 여러분 입속에 콸콸콸 ~ 🍻  (˶ㅇᗜㅇ˶) ⑉♥ 콸콸콸 ~ 콸콸콸 ~ 여러분 입속에 콸콸콸 ~ 🍻  (˶ㅇᗜㅇ˶) ⑉♥
(つ🍺⊂)                                                   (つ🍺⊂)                                                   (つ🍺⊂)
""")
    print("-"*130)
    start = input("게임을 진행할까요? (y/n) : ")
    if (start == 'y'):
        gamestate = True
    else:
        gamestate = False
        return
        
    while True:
        try:
            username = input('오늘 거하게 취해볼 당신의 이름은? : ')
            if username not in playerlist:
                raise NotInRangeError
            break
        except NotInRangeError:
            print("(우리 팀원이 아닌 거 같은데... 다시 입력해주세요!)")

    npclist = playerlist[:]
    npclist.remove(username)

    while True:
        try:
            print("╔═══════════════════════*.·:·.☽✧    ✦    ✧☾.·:·.*═══════════════════════╗\n")
            print("""                        🍺 소주 기준 당신의 주량은? 🍺
                        🍺 1. 소주 반병(2잔)
                        🍺 2. 소주 반병에서 한병(4잔)
                        🍺 3. 소주 한병에서 한병 반(6잔)
                        🍺 4. 소주 한병 반에서 두병(8잔)
                        🍺 5. 소주 두병 이상(10잔)
""")
            print("╚═══════════════════════*.·:·.☽✧    ✦    ✧☾.·:·.*═══════════════════════╝")
            drinklimit = input("당신의 치사량(주량)은 얼마만큼인가요?(1~5을 선택해주세요) : ")
            drinklimit = int(drinklimit) * 2
            if not (0 < drinklimit <= 10):
                print('보기에서 선택해주세요!')
            else:
                break
        except ValueError:
            print('숫자를 입력해주세요!')

def playerselect(username, drinklimit):
    while True:
        try:
            global playernum, playerlist, players, game_selector
            playernum = int(input('함께 취할 친구들은 얼마나 필요하신가요? (최대 3명까지): '))
            if not (1<=playernum<=3):
                raise NotInRangeError
            random_players = random.sample(npclist, playernum)
            for random_player in random_players:
                random_drink_limit = random.choice([2, 4, 6, 8, 10])
                players.append({'name': random_player, 'drink_limit': random_drink_limit})
                print(f"오늘 함께 취할 친구는 {random_player}입니다! (치사량 :{random_drink_limit})")
            
            game_selector = random_players[:]
            game_selector.append(username)
            players.append({'name': username, 'drink_limit': drinklimit})
            break

        except ValueError:
            print('숫자를 입력해주세요!')
        except NotInRangeError:
            print('1에서 3사이 숫자를 입력해주세요!')

    for player in players:
        player['current_drinks'] = 0

def select_game():
    print("""
--------------------------------------------------
            🍺오늘의 Alcohol GAME🍺
--------------------------------------------------

                1. 369 게임
                2. 이구동성 게임
                3. 지하철 게임
                4. 수도 맞히기 게임
                5. 슈퍼개미 게임

--------------------------------------------------
--------------------------------------------------
""")
    while True:
        try:
            game_choice = int(input("실행하고 싶은 게임 번호를 선택해주세요 : "))
            if not (1<=game_choice<=5):
                raise NotInRangeError
            
            print(f"{username}이(가) 고른 다음 게임은 {game_choice}번 게임이야!")

            if game_choice == 1:
                return game_369.gameEngine(username, [player['name'] for player in players])
            elif game_choice == 2:
                return egudongseong.play_egudongseong_game(username, [player['name'] for player in players if player['name'] != username])
            elif game_choice == 3:
                return subwayGame.subwayGame_start(username, [player['name'] for player in players if player['name'] != username])
            elif game_choice == 4:
                return game_capital.capital_game(username, players)
            elif game_choice == 5:
                return pythongame5.antgame(players, username)
                     

        except ValueError:
            print('숫자를 입력해주세요!')
        except NotInRangeError:
            print('1에서 5사이 숫자를 입력해주세요!')

def select_game_auto(cur_selector):
    game_choice = str(random.randint(1, 5))
    print("""
--------------------------------------------------
            🍺오늘의 Alcohol GAME🍺
--------------------------------------------------

                1. 369 게임
                2. 이구동성 게임
                3. 지하철 게임
                4. 수도 맞히기 게임
                5. 슈퍼개미 게임

--------------------------------------------------
--------------------------------------------------
""")
    user_input = input("술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 'exit'를, 계속하고 싶으면 아무 키나 입력해주세요: ")
    if user_input.lower() == 'exit':
        print("게임을 종료합니다.")
        global gamestate
        gamestate = False
        return None
    else:
        print(f"{cur_selector}이(가) 고른 다음 게임은 {game_choice}번 게임이야!")
        if game_choice == '1':
            return game_369.gameEngine(username, [player['name'] for player in players])
        elif game_choice == '2':
            return egudongseong.play_egudongseong_game(username, [player['name'] for player in players if player['name'] != username])
        elif game_choice == '3':
            return subwayGame.subwayGame_start(username, [player['name'] for player in players if player['name'] != username])
        elif game_choice == '4':
            return game_capital.capital_game(username, players)
        elif game_choice == '5':
            return pythongame5.antgame(players, username)
    print("""
---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------


    ███╗   ██╗███████╗██╗    ██╗     ██████╗  █████╗ ███╗   ███╗███████╗    ███████╗████████╗ █████╗ ██████╗ ████████╗██╗
    ████╗  ██║██╔════╝██║    ██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██║
    ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║  ███╗███████║██╔████╔██║█████╗      ███████╗   ██║   ███████║██████╔╝   ██║   ██║
    ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ╚═╝
    ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████║   ██║   ██║  ██║██║  ██║   ██║   ██╗
    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝
                                                                                                             

---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------
""")
    
def drink_phase(players, player_lost):
    for player in players:
        if player['name'] in player_lost:
            print(f"{player['name']}은(는) 술을 마셔 원샷!")
            time.sleep(1)
            player['current_drinks'] += 1

    print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
    for player in players:
        print(f"{player['name']}은(는), 지금까지 {player['current_drinks']}🍺, 치사량까지 {player['drink_limit'] - player['current_drinks']}")
        time.sleep(0.5)
    print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

def check_game_end(players):
    for player in players:
        if player['drink_limit'] <= player['current_drinks']:
            return True
    return False

gamestate = False
drinklimit = 0
username = None
playerlist = ['민주', '하영', '주형', '영헌', '용화']
npclist = []
playernum = 0
players = []
game_selector = []

def main():

    global game_selector, gamestate, players, username

    gamestart() # username / drinklimit
    if gamestate:
        playerselect(username, drinklimit)

    while gamestate:
        try:
            if username in game_selector:
                player_lost = select_game()
                game_selector.remove(username)
                drink_phase(players, player_lost)
                if check_game_end(players):
                    gamestate = False

            elif (game_selector):
                cur_selector = game_selector.pop()
                player_lost = select_game_auto(cur_selector)
                drink_phase(players, player_lost)
                if check_game_end(players):
                    gamestate = False

            else:
                print("한 바퀴 다 돌았네~")
                game_selector = [player['name'] for player in players]
        except TypeError:
            pass
        
    print("""
--------------------------------------------------------------------------
--------------------------------------------------------------------------
          
  
   ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
  ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
  ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
  ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
  ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                
--------------------------------------------------------------------------
--------------------------------------------------------------------------
""")

if __name__ == "__main__":
    main()