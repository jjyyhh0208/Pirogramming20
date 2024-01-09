import random

def get_random_vs_pair():
    with open('vs.txt', 'r', encoding='utf-8') as file: 
        lines = file.readlines()
        return random.choice(lines).strip()

def play_egudongseong_game(username, friends):
    players = [{'name': username}] + [{'name': friend} for friend in friends]
    for player in players:
        player['score'] = 0

    for round_number in range(1, 4):
        print("-----------------------------------------------")
        print(f"🚀🚀🚀 {round_number} ROUND START 🚀🚀🚀")
        print("-----------------------------------------------")
        vs_pair = get_random_vs_pair()
        choices = vs_pair.split(' vs ')
        print(f"💗 {vs_pair} - 당신의 선택은? 💗")

        player_choices = {}
        for player in players:
            if player['name'] == username:
                while True:
                    choice = input(f"{username}의 선택: ")
                    if choice in choices:
                        break
                    else:
                        print("잘못된 입력입니다.")
                    
            else:
                choice = random.choice(choices)
            player_choices[player['name']] = choice
            print(f"💗 {player['name']}의 선택: {choice}")

        # 점수 계산
        if len(players) <= 3:
            if len(set(player_choices.values())) == 1:
                print("모든 선택이 일치합니다!")
                for player in players:
                    player['score'] += 3
            else:
                print("선택이 일치하지 않습니다.")
        else:
            teams = [players[i:i+2] for i in range(0, len(players), 2)]
            for i, team in enumerate(teams, start=1):
                print("-----------------------")
                print(f"🍎 {i}팀 차례입니다 🍎")
                team_choices = set()
                for player in team:
                    player_choice = player_choices[player['name']]
                    print(f"💗 {player['name']}의 선택: {player_choice}")
                    team_choices.add(player_choice)
                if len(team_choices) == 1:
                    print(f"🥂🥂🥂 {i}팀 성공 🥂🥂🥂")
                    for player in team:
                        player['score'] += 3
                else:
                    print(f"🍏 {i}팀 실패 🍏")

    print("----------------------------------------------------------------")
    for player in players:
        print(f"🧩 {player['name']}의 이구동성 게임 점수는: {player['score']}점")

    min_score = min(player['score'] for player in players)
    player_lost = [player['name'] for player in players if player['score'] == min_score]

    if player_lost:
        print("----------------------------------------------------------------")
        print(f"🥨 패배자🥨 {', '.join(player_lost)} ")
        print("----------------------------------------------------------------")

    return player_lost