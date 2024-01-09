import random
import time

def count369(i):
    return str(i).count('3') + str(i).count('6') + str(i).count('9')

def gameEngine(player_name, player_list):
    random.shuffle(player_list)
    my_position = player_list.index(player_name)
    num_of_players = len(player_list)
    print("플레이 순서는"," ➭ ".join(player_list),"야~")
    print("3️⃣ ~ 6️⃣  9️⃣  3️⃣  6️⃣  9️⃣!")
    time.sleep(0.5)
    print("3️⃣ ~ 6️⃣  9️⃣  3️⃣  6️⃣  9️⃣!")
    print("-"*50)

    # 순서 / 숫자 / NPC의 실패확률
    order = 0
    i = 1
    fail_prob = 0.015

    while True:
        clap = count369(i)
        if order == my_position:
            answer = input()
            answer_clap_count = answer.count('짝')
            answer_in_clap = '👏'*answer_clap_count
            if  clap > 0 and answer.count('짝') != clap:
                print(f"{player_name} : {answer_in_clap}...")
                time.sleep(1)
                print(f"{player_name} : 앗! 실수했다...")
                return [player_name]
            elif clap == 0 and answer != str(i):
                 print(f"{answer_in_clap}...")
                 time.sleep(1)
                 print(f"{player_name} : 아... 실수했다..")
                 return [player_name]
            elif clap > 0:
                print(f"{player_name} :", answer_in_clap)
            else:
                print(f"{player_name} :", answer)

        else:
            if clap:
                if random.random() > fail_prob * (clap+1):
                    print(f'{player_list[order]} :','👏'*clap)
                else:
                    print(f'{player_list[order]} :','👏'*(clap-1),"...")
                    time.sleep(1)
                    print(f'{player_list[order]} : 앗, 실수했다...')
                    return [player_list[order]]
            else:
                if random.random() > fail_prob:
                    print(f'{player_list[order]} : {i}')
                else:
                    time.sleep(1)
                    print(f"{player_list[order]} :어... 다음이 뭐였더라?")
                    return [player_list[order]]
            
        order += 1
        order = order % num_of_players
        i += 1
        time.sleep(0.5)