import json
import random

def subwayGame_start(user, friends):
    with open('sub.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    line_num_dict = {}

    for entry in data:
        line_num = entry.get("line_num", "")
        station_nm = entry.get("station_nm", "")

        if line_num in line_num_dict:
            line_num_dict[line_num].append(station_nm)
        else:
            line_num_dict[line_num] = [station_nm]
    print("▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱")
    print("🚇 지하철~지하철~지하철~지하철 🚇 🤔 몇호선~몇호선~몇호선~몇호선~ 🤔")
    print("▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱")
    random_line_num = random.choice(list(line_num_dict.keys()))
    print(f"[{random_line_num}]")

    used_stations = set()

    incorrect_users = []
    
    players = initialize_players(user, friends)

    while True:
        for player in players:

            if player['name'] == user:
                selected_station = input(f"{player['name']}, 어떤 역을 선택하시겠습니까?🤔 ")
            else:
                if random.random() < 0.2: #틀릴확률 20%
                    other_line_nums = [line_num for line_num in line_num_dict.keys() if line_num != random_line_num]
                    selected_line_num = random.choice(other_line_nums)
                    selected_station = random.choice(line_num_dict[selected_line_num])
                    print(f"{player['name']}, 🚅 {selected_station}🚅 을(를) 선택했습니다.")
                else:
                    selected_station = random.choice(line_num_dict[random_line_num])
                    print(f"{player['name']}, 🚅 {selected_station}🚅 을(를) 선택했습니다.")



            if selected_station in used_stations:
                print("어❓❓ 🤣 바보샷ㅋ 🍻 🤣 바보샷ㅋ 🍻")
                incorrect_users.append(player['name'])
                return incorrect_users

            if selected_station not in line_num_dict[random_line_num]:
                print(f"🤪 아 누가 술을 마셔 🤪 {player['name']}(이)가 술을마셔~ 🍻 원~ 샷~ ☠️")
                incorrect_users.append(player['name'])
                return incorrect_users

            else :
                print("통과~")
            used_stations.add(selected_station)
            player['current_station'] = selected_station
            
            if not used_stations:
                print("모든 역을 다 선택하셨습니다. 게임 종료!")
                return incorrect_users

def initialize_players(user, friends):
    player_names = [user] + friends
    players = []
    for i, player_name in enumerate(player_names, start=1):
        player = {
            "id": i,
            "name": player_name,
            "current_station": None
        }
        players.append(player)

    return players